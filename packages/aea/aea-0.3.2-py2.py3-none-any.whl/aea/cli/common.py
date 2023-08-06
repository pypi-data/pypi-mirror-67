# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""Implementation of the common utils of the aea cli."""
import logging
import logging.config
import os
import re
import shutil
from collections import OrderedDict
from functools import update_wrapper
from pathlib import Path
from typing import Callable, Dict, List, Optional, cast

import click

import jsonschema  # type: ignore
from jsonschema import ValidationError

import yaml

from aea import AEA_DIR
from aea.cli.loggers import default_logging_config
from aea.configurations.base import (
    AgentConfig,
    DEFAULT_AEA_CONFIG_FILE,
    Dependencies,
    PackageType,
    PublicId,
    _check_aea_version,
    _compare_fingerprints,
    _get_default_configuration_file_name_from_type,
)
from aea.configurations.loader import ConfigLoader, ConfigLoaders
from aea.crypto.ethereum import ETHEREUM
from aea.crypto.fetchai import FETCHAI
from aea.crypto.helpers import (
    ETHEREUM_PRIVATE_KEY_FILE,
    FETCHAI_PRIVATE_KEY_FILE,
    _create_ethereum_private_key,
    _create_fetchai_private_key,
    _try_validate_ethereum_private_key_path,
    _try_validate_fet_private_key_path,
)
from aea.crypto.wallet import SUPPORTED_CRYPTOS

logger = logging.getLogger("aea")
logger = default_logging_config(logger)

AEA_LOGO = "    _     _____     _    \r\n   / \\   | ____|   / \\   \r\n  / _ \\  |  _|    / _ \\  \r\n / ___ \\ | |___  / ___ \\ \r\n/_/   \\_\\|_____|/_/   \\_\\\r\n                         \r\n"
AUTHOR_KEY = "author"
CLI_CONFIG_PATH = os.path.join(os.path.expanduser("~"), ".aea", "cli_config.yaml")
NOT_PERMITTED_AUTHORS = [
    "skills",
    "connections",
    "protocols",
    "contracts",
    "vendor",
    "packages",
    "aea",
]


from_string_to_type = dict(str=str, int=int, bool=bool, float=float)


class Context:
    """A class to keep configuration of the cli tool."""

    agent_config: AgentConfig

    def __init__(self, cwd: str = ".", verbosity: str = "INFO"):
        """Init the context."""
        self.config = dict()  # type: Dict
        self.cwd = cwd
        self.verbosity = verbosity
        self.clean_paths: List = []

    @property
    def agent_loader(self) -> ConfigLoader:
        """Get the agent loader."""
        return ConfigLoader.from_configuration_type(PackageType.AGENT)

    @property
    def protocol_loader(self) -> ConfigLoader:
        """Get the protocol loader."""
        return ConfigLoader.from_configuration_type(PackageType.PROTOCOL)

    @property
    def connection_loader(self) -> ConfigLoader:
        """Get the connection loader."""
        return ConfigLoader.from_configuration_type(PackageType.CONNECTION)

    @property
    def skill_loader(self) -> ConfigLoader:
        """Get the skill loader."""
        return ConfigLoader.from_configuration_type(PackageType.SKILL)

    @property
    def contract_loader(self) -> ConfigLoader:
        """Get the contract loader."""
        return ConfigLoader.from_configuration_type(PackageType.CONTRACT)

    def set_config(self, key, value) -> None:
        """
        Set a config.

        :param key: the key for the configuration.
        :param value: the value associated with the key.
        :return: None
        """
        self.config[key] = value
        logger.debug("  config[{}] = {}".format(key, value))

    @staticmethod
    def _get_item_dependencies(item_type, public_id: PublicId) -> Dependencies:
        """Get the dependencies from item type and public id."""
        item_type_plural = item_type + "s"
        default_config_file_name = _get_default_configuration_file_name_from_type(
            item_type
        )
        path = Path(
            "vendor",
            public_id.author,
            item_type_plural,
            public_id.name,
            default_config_file_name,
        )
        if not path.exists():
            path = Path(item_type_plural, public_id.name, default_config_file_name)
        config_loader = ConfigLoader.from_configuration_type(item_type)
        config = config_loader.load(path.open())
        deps = cast(Dependencies, config.dependencies)
        return deps

    def get_dependencies(self) -> Dependencies:
        """Aggregate the dependencies from every component.

        :return a list of dependency version specification. e.g. ["gym >= 1.0.0"]
        """
        dependencies = {}  # type: Dependencies
        for protocol_id in self.agent_config.protocols:
            dependencies.update(self._get_item_dependencies("protocol", protocol_id))

        for connection_id in self.agent_config.connections:
            dependencies.update(
                self._get_item_dependencies("connection", connection_id)
            )

        for skill_id in self.agent_config.skills:
            dependencies.update(self._get_item_dependencies("skill", skill_id))

        for contract_id in self.agent_config.contracts:
            dependencies.update(self._get_item_dependencies("contract", contract_id))

        return dependencies


pass_ctx = click.make_pass_decorator(Context)


def try_to_load_agent_config(
    ctx: Context, is_exit_on_except: bool = True, agent_src_path: str = None
) -> None:
    """
    Load agent config to a click context object.

    :param ctx: click command context object.
    :param is_exit_on_except: bool option to exit on exception (default = True).
    :param agent_src_path: path to an agent dir if needed to load a custom config.

    :return None
    """
    if agent_src_path is None:
        agent_src_path = ctx.cwd

    try:
        path = Path(os.path.join(agent_src_path, DEFAULT_AEA_CONFIG_FILE))
        with path.open(mode="r", encoding="utf-8") as fp:
            ctx.agent_config = ctx.agent_loader.load(fp)
            logging.config.dictConfig(ctx.agent_config.logging_config)
    except FileNotFoundError:
        if is_exit_on_except:
            raise click.ClickException(
                "Agent configuration file '{}' not found in the current directory.".format(
                    DEFAULT_AEA_CONFIG_FILE
                )
            )
    except jsonschema.exceptions.ValidationError:
        if is_exit_on_except:
            raise click.ClickException(
                "Agent configuration file '{}' is invalid. Please check the documentation.".format(
                    DEFAULT_AEA_CONFIG_FILE
                )
            )


def _verify_or_create_private_keys(ctx: Context) -> None:
    """
    Verify or create private keys.

    :param ctx: Context
    """
    path = Path(DEFAULT_AEA_CONFIG_FILE)
    agent_loader = ConfigLoader("aea-config_schema.json", AgentConfig)
    fp = path.open(mode="r", encoding="utf-8")
    aea_conf = agent_loader.load(fp)

    for identifier, _value in aea_conf.private_key_paths.read_all():
        if identifier not in SUPPORTED_CRYPTOS:
            ValueError("Unsupported identifier in private key paths.")

    fetchai_private_key_path = aea_conf.private_key_paths.read(FETCHAI)
    if fetchai_private_key_path is None:
        _create_fetchai_private_key()
        aea_conf.private_key_paths.update(FETCHAI, FETCHAI_PRIVATE_KEY_FILE)
    else:
        try:
            _try_validate_fet_private_key_path(fetchai_private_key_path)
        except FileNotFoundError:  # pragma: no cover
            raise click.ClickException(
                "File {} for private key {} not found.".format(
                    repr(fetchai_private_key_path), FETCHAI,
                )
            )

    ethereum_private_key_path = aea_conf.private_key_paths.read(ETHEREUM)
    if ethereum_private_key_path is None:
        _create_ethereum_private_key()
        aea_conf.private_key_paths.update(ETHEREUM, ETHEREUM_PRIVATE_KEY_FILE)
    else:
        try:
            _try_validate_ethereum_private_key_path(ethereum_private_key_path)
        except FileNotFoundError:  # pragma: no cover
            raise click.ClickException(
                "File {} for private key {} not found.".format(
                    repr(ethereum_private_key_path), ETHEREUM,
                )
            )

    # update aea config
    path = Path(DEFAULT_AEA_CONFIG_FILE)
    fp = path.open(mode="w", encoding="utf-8")
    agent_loader.dump(aea_conf, fp)
    ctx.agent_config = aea_conf


def _format_items(items):
    """Format list of items (protocols/connections) to a string for CLI output."""
    list_str = ""
    for item in items:
        list_str += (
            "{line}\n"
            "Public ID: {public_id}\n"
            "Name: {name}\n"
            "Description: {description}\n"
            "Author: {author}\n"
            "Version: {version}\n"
            "{line}\n".format(
                name=item["name"],
                public_id=item["public_id"],
                description=item["description"],
                author=item["author"],
                version=item["version"],
                line="-" * 30,
            )
        )
    return list_str


def _retrieve_details(name: str, loader: ConfigLoader, config_filepath: str) -> Dict:
    """Return description of a protocol, skill, connection."""
    config = loader.load(open(str(config_filepath)))
    item_name = config.agent_name if isinstance(config, AgentConfig) else config.name
    assert item_name == name, "Item names do not match!"
    return {
        "public_id": str(config.public_id),
        "name": item_name,
        "author": config.author,
        "description": config.description,
        "version": config.version,
    }


class AEAConfigException(Exception):
    """Exception about AEA configuration."""


class ConnectionsOption(click.Option):
    """Click option for the --connections option in 'aea run'."""

    def type_cast_value(self, ctx, value) -> Optional[List[PublicId]]:
        """
        Parse the list of string passed through command line.

        E.g. from 'stub,local' to ['stub', 'local'].

        :param ctx: the click context
        :param value: the list of connection names, as a string.
        :return:
        """
        if value is None:
            return None
        try:

            def arg_strip(s):
                return s.strip(" '\"")

            input_connection_ids = [
                arg_strip(s) for s in value.split(",") if arg_strip(s) != ""
            ]

            # remove duplicates, while preserving the order
            result = OrderedDict()  # type: OrderedDict[PublicId, None]
            for connection_id_string in input_connection_ids:
                connection_public_id = PublicId.from_str(connection_id_string)
                result[connection_public_id] = None
            return list(result.keys())
        except Exception:  # pragma: no cover
            raise click.BadParameter(value)


class PublicIdParameter(click.ParamType):
    """Define a public id parameter for Click applications."""

    def __init__(self, *args, **kwargs):
        """
        Initialize the Public Id parameter.

        Just forwards arguments to parent constructor.
        """
        super().__init__(*args, **kwargs)

    def get_metavar(self, param):
        """Return the metavar default for this param if it provides one."""
        return "PUBLIC_ID"

    def convert(self, value, param, ctx):
        """Convert the value. This is not invoked for values that are `None` (the missing value)."""
        try:
            return PublicId.from_str(value)
        except ValueError:
            self.fail(value, param, ctx)


class AgentDirectory(click.Path):
    """A click.Path, but with further checks  applications."""

    def __init__(self):
        """Initialize the agent directory parameter."""
        super().__init__(
            exists=True, file_okay=False, dir_okay=True, readable=True, writable=False
        )

    def get_metavar(self, param):
        """Return the metavar default for this param if it provides one."""
        return "AGENT_DIRECTORY"

    def convert(self, value, param, ctx):
        """Convert the value. This is not invoked for values that are `None` (the missing value)."""
        cwd = os.getcwd()
        path = Path(value)
        try:
            # check that the target folder is an AEA project.
            os.chdir(path)
            fp = open(DEFAULT_AEA_CONFIG_FILE, mode="r", encoding="utf-8")
            ctx.obj.agent_config = ctx.obj.agent_loader.load(fp)
            try_to_load_agent_config(ctx.obj)
            # everything ok - return the parameter to the command
            return value
        except Exception:
            raise click.ClickException(
                "The name provided is not a path to an AEA project."
            )
        finally:
            os.chdir(cwd)


def _validate_package_name(package_name: str):
    """Check that the package name matches the pattern r"[a-zA-Z_][a-zA-Z0-9_]*".

    >>> _validate_package_name("this_is_a_good_package_name")
    >>> _validate_package_name("this-is-not")
    Traceback (most recent call last):
    ...
    click.exceptions.BadParameter: this-is-not is not a valid package name.
    """
    if re.fullmatch(PublicId.PACKAGE_NAME_REGEX, package_name) is None:
        raise click.BadParameter("{} is not a valid package name.".format(package_name))


def _is_valid_author_handle(author: str) -> bool:
    """
    Check that the author matches the pattern r"[a-zA-Z_][a-zA-Z0-9_]*".

    >>> _is_valid_author_handle("this_is_a_good_author_name")
    ...
    True
    >>> _is_valid_author_handle("this-is-not")
    ...
    False
    """
    if re.fullmatch(PublicId.AUTHOR_REGEX, author) is None:
        return False
    return True


def _is_permitted_author_handle(author: str) -> bool:
    """
    Check that the author handle is permitted.

    :param author: the author
    :retun: bool
    """
    result = author not in NOT_PERMITTED_AUTHORS
    return result


def _try_get_item_source_path(
    path: str, author_name: Optional[str], item_type_plural: str, item_name: str
) -> str:
    """
    Get the item source path.

    :param path: the source path root
    :param author_name: the name of the author of the item
    :param item_type_plural: the item type (plural)
    :param item_name: the item name

    :return: the item source path
    """
    if author_name is None:
        source_path = os.path.join(path, item_type_plural, item_name)
    else:
        source_path = os.path.join(path, author_name, item_type_plural, item_name)
    if not os.path.exists(source_path):
        raise click.ClickException(
            'Item "{}" not found in source folder.'.format(item_name)
        )
    return source_path


def _try_get_item_target_path(
    path: str, author_name: str, item_type_plural: str, item_name: str
) -> str:
    """
    Get the item target path.

    :param path: the target path root
    :param author_name the author name
    :param item_type_plural: the item type (plural)
    :param item_name: the item name

    :return: the item target path
    """
    target_path = os.path.join(path, author_name, item_type_plural, item_name)
    if os.path.exists(target_path):
        raise click.ClickException(
            'Item "{}" already exists in target folder.'.format(item_name)
        )
    return target_path


def get_package_dest_path(
    ctx: Context, author_name: str, item_type_plural: str, item_name: str
) -> str:
    """
    Get a destenation path for a package.

    :param ctx: context.
    :param author_name: package author name.
    :param item_type_plural: plural of item type.
    :param item_name: package name.

    :return: destenation path for package.
    """
    return os.path.join(ctx.cwd, "vendor", author_name, item_type_plural, item_name)


def _copy_package_directory(
    ctx: Context,
    package_path: Path,
    item_type: str,
    item_name: str,
    author_name: str,
    dest: str,
) -> Path:
    """
     Copy a package directory to the agent vendor resources.

    :param ctx: the CLI context .
    :param package_path: the path to the package to be added.
    :param item_type: the type of the package.
    :param item_name: the name of the package.
    :param author_name: the author of the package.

    :return: copied folder target path.
    :raises SystemExit: if the copy raises an exception.
    """
    # copy the item package into the agent's supported packages.
    item_type_plural = item_type + "s"
    src = str(package_path.absolute())
    logger.debug("Copying {} modules. src={} dst={}".format(item_type, src, dest))
    try:
        shutil.copytree(src, dest)
    except Exception as e:
        raise click.ClickException(str(e))

    Path(ctx.cwd, "vendor", author_name, item_type_plural, "__init__.py").touch()
    return Path(dest)


def _find_item_locally(ctx, item_type, item_public_id) -> Path:
    """
    Find an item in the local registry.

    :param ctx: the CLI context.
    :param item_type: the type of the item to load. One of: protocols, connections, skills
    :param item_public_id: the public id of the item to find.
    :return: path to the package directory (either in registry or in aea directory).
    :raises SystemExit: if the search fails.
    """
    item_type_plural = item_type + "s"
    item_name = item_public_id.name

    # check in registry
    registry_path = os.path.join(ctx.cwd, ctx.agent_config.registry_path)
    package_path = Path(
        registry_path, item_public_id.author, item_type_plural, item_name
    )
    config_file_name = _get_default_configuration_file_name_from_type(item_type)
    item_configuration_filepath = package_path / config_file_name
    if not item_configuration_filepath.exists():
        raise click.ClickException(
            "Cannot find {}: '{}'.".format(item_type, item_public_id)
        )

    # try to load the item configuration file
    try:
        item_configuration_loader = ConfigLoader.from_configuration_type(
            PackageType(item_type)
        )
        item_configuration = item_configuration_loader.load(
            item_configuration_filepath.open()
        )
    except ValidationError as e:
        raise click.ClickException(
            "{} configuration file not valid: {}".format(item_type.capitalize(), str(e))
        )

    # check that the configuration file of the found package matches the expected author and version.
    version = item_configuration.version
    author = item_configuration.author
    if item_public_id.author != author or item_public_id.version != version:
        raise click.ClickException(
            "Cannot find {} with author and version specified.".format(item_type)
        )

    return package_path


def _find_item_in_distribution(ctx, item_type, item_public_id) -> Path:
    """
    Find an item in the AEA directory.

    :param ctx: the CLI context.
    :param item_type: the type of the item to load. One of: protocols, connections, skills
    :param item_public_id: the public id of the item to find.
    :return: path to the package directory (either in registry or in aea directory).
    :raises SystemExit: if the search fails.
    """
    item_type_plural = item_type + "s"
    item_name = item_public_id.name

    # check in aea dir
    registry_path = AEA_DIR
    package_path = Path(registry_path, item_type_plural, item_name)
    config_file_name = _get_default_configuration_file_name_from_type(item_type)
    item_configuration_filepath = package_path / config_file_name
    if not item_configuration_filepath.exists():
        raise click.ClickException(
            "Cannot find {}: '{}'.".format(item_type, item_public_id)
        )

    # try to load the item configuration file
    try:
        item_configuration_loader = ConfigLoader.from_configuration_type(
            PackageType(item_type)
        )
        item_configuration = item_configuration_loader.load(
            item_configuration_filepath.open()
        )
    except ValidationError as e:
        raise click.ClickException(
            "{} configuration file not valid: {}".format(item_type.capitalize(), str(e))
        )

    # check that the configuration file of the found package matches the expected author and version.
    version = item_configuration.version
    author = item_configuration.author
    if item_public_id.author != author or item_public_id.version != version:
        raise click.ClickException(
            "Cannot find {} with author and version specified.".format(item_type)
        )

    return package_path


def _validate_config_consistency(ctx: Context):
    """
    Validate fingerprints for every agent component.

    :raise ValueError: if there is a missing configuration file.
                       or if the configuration file is not valid.
                       or if the fingerprints do not match
    """

    packages_public_ids_to_types = dict(
        [
            *map(lambda x: (x, PackageType.PROTOCOL), ctx.agent_config.protocols),
            *map(lambda x: (x, PackageType.CONNECTION), ctx.agent_config.connections,),
            *map(lambda x: (x, PackageType.SKILL), ctx.agent_config.skills),
            *map(lambda x: (x, PackageType.CONTRACT), ctx.agent_config.contracts),
        ]
    )  # type: Dict[PublicId, PackageType]

    for public_id, item_type in packages_public_ids_to_types.items():

        # find the configuration file.
        try:
            # either in vendor/ or in personal packages.
            # we give precedence to custom agent components (i.e. not vendorized).
            package_directory = Path(item_type.to_plural(), public_id.name)
            is_vendor = False
            if not package_directory.exists():
                package_directory = Path(
                    "vendor", public_id.author, item_type.to_plural(), public_id.name
                )
                is_vendor = True
            # we fail if none of the two alternative works.
            assert package_directory.exists(), "Package directory does not exist!"

            loader = ConfigLoaders.from_package_type(item_type)
            config_file_name = _get_default_configuration_file_name_from_type(item_type)
            configuration_file_path = package_directory / config_file_name
            assert (
                configuration_file_path.exists()
            ), "Configuration file path does not exist!"
        except Exception:
            raise ValueError("Cannot find {}: '{}'".format(item_type.value, public_id))

        # load the configuration file.
        try:
            package_configuration = loader.load(configuration_file_path.open("r"))
        except ValidationError as e:
            raise ValueError(
                "{} configuration file not valid: {}".format(
                    item_type.value.capitalize(), str(e)
                )
            )

        _check_aea_version(package_configuration)
        _compare_fingerprints(
            package_configuration, package_directory, is_vendor, item_type
        )


def _check_aea_project(args):
    try:
        click_context = args[0]
        ctx = cast(Context, click_context.obj)
        try_to_load_agent_config(ctx)
        skip_consistency_check = ctx.config["skip_consistency_check"]
        if not skip_consistency_check:
            _validate_config_consistency(ctx)
    except Exception as e:
        raise click.ClickException(str(e))


def check_aea_project(f):
    """
    Decorator that checks the consistency of the project.

    - try to load agent configuration file
    - iterate over all the agent packages and check for consistency.
    """

    def wrapper(*args, **kwargs):
        _check_aea_project(args)
        return f(*args, **kwargs)

    return update_wrapper(wrapper, f)


def _init_cli_config() -> None:
    """
    Create cli config folder and file.

    :return: None
    """
    conf_dir = os.path.dirname(CLI_CONFIG_PATH)
    if not os.path.exists(conf_dir):
        os.makedirs(conf_dir)
    with open(CLI_CONFIG_PATH, "w+") as f:
        yaml.dump({}, f, default_flow_style=False)


def _update_cli_config(dict_conf: Dict) -> None:
    """
    Update CLI config and write to yaml file.

    :param dict_conf: dict config to write.

    :return: None
    """
    config = _get_or_create_cli_config()
    config.update(dict_conf)
    with open(CLI_CONFIG_PATH, "w") as f:
        yaml.dump(config, f, default_flow_style=False)


def _get_or_create_cli_config() -> Dict:
    """
    Read or create CLI config from yaml file.

    :return: dict CLI config.
    """
    try:
        return _load_yaml(CLI_CONFIG_PATH)
    except FileNotFoundError:
        _init_cli_config()
    return _load_yaml(CLI_CONFIG_PATH)


def _load_yaml(filepath: str) -> Dict:
    """
    Read content from yaml file.

    :param filepath: str path to yaml file.

    :return: dict YAML content
    """
    with open(filepath, "r") as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise click.ClickException(
                "Loading yaml config from {} failed: {}".format(filepath, e)
            )


def validate_author_name(author: Optional[str] = None) -> str:
    """
    Validate an author name.

    :param author: the author name (optional)
    """
    is_acceptable_author = False
    if (
        author is not None
        and _is_valid_author_handle(author)
        and _is_permitted_author_handle(author)
    ):
        is_acceptable_author = True
        valid_author = author
    while not is_acceptable_author:
        author_prompt = click.prompt(
            "Please enter the author handle you would like to use", type=str
        )
        valid_author = author_prompt
        if _is_valid_author_handle(author_prompt) and _is_permitted_author_handle(
            author_prompt
        ):
            is_acceptable_author = True
        elif not _is_valid_author_handle(author_prompt):
            is_acceptable_author = False
            click.echo(
                "Not a valid author handle. Please try again. "
                "Author handles must satisfy the following regex: {}".format(
                    PublicId.AUTHOR_REGEX
                )
            )
        elif not _is_permitted_author_handle(author_prompt):
            is_acceptable_author = False
            click.echo(
                "Not a permitted author handle. The following author handles are not allowed: {}".format(
                    NOT_PERMITTED_AUTHORS
                )
            )

    return valid_author


def _rmdirs(*paths: str) -> None:
    """
    Remove directories.

    :param paths: paths to folders to remove.

    :return: None
    """
    for path in paths:
        if os.path.exists(path):
            shutil.rmtree(path)


def clean_after(func: Callable) -> Callable:
    """
    Decorate a function to remove created folders after ClickException raise.

    :param func: a method to decorate.

    :return: decorated method.
    """

    def wrapper(click_context, *args, **kwargs):
        """
        Call a source method, remove dirs listed in ctx.clean_paths if ClickException is raised.

        :param click_context: click context object.

        :raises ClickException: if caught re-raises it.

        :return: source method output.
        """
        ctx = cast(Context, click_context.obj)
        try:
            return func(click_context, *args, **kwargs)
        except click.ClickException as e:
            _rmdirs(*ctx.clean_paths)
            raise e

    return wrapper
