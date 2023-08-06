import re
import shelve
import webbrowser
from datetime import datetime, timezone
from uuid import UUID

import attr
import click
import click_completion
import inquirer
import pkg_resources
import pyfiglet
import ruamel.yaml
import sentry_sdk
from click import ClickException, Choice
from click.types import StringParamType
from click_completion import completion_configuration
from tabulate import tabulate

from hackgame import api, docs, STATE_FILE, auth
from hackgame.api import SERVER_HOSTS
from hackgame.cli.api_wrapper import ClickRaisingObjectEndpoint, CLIObjectEndpoint
from hackgame.cli.identifier_cache import IdentifierCache, ShelfIdentifierCache
from hackgame.cli.update_notice import hackgame_update_notice
from hackgame.models import (
    Account,
    Player,
    AccessToken,
    World,
    Network,
    Connection,
    Program,
    Ice,
    ActionResult,
)

sentry_sdk.init(
    dsn="https://5ad4eb55f86c484689222b392aac75dd@sentry.rachsharp.co.uk/6",
    release=pkg_resources.get_distribution("hackgame").version,
    environment="DEV",
    request_bodies="always",
    with_locals=True,
)

click_completion.init()


@attr.s(auto_attribs=True)
class ClickObj(object):
    state: dict
    client: api.HackgameClient
    cache: IdentifierCache
    nesting: int = 0


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


def get_context_obj(state_file: str):
    try:
        shelf = shelve.open(state_file, writeback=True)
    except OSError as e:
        if e.errno == 35:
            raise click.ClickException(
                "hackgame is currently running in another process"
            )
        else:
            raise

    if "cache_storage" not in shelf:
        shelf["cache_storage"] = {}
    cache_storage = shelf["cache_storage"]

    cache = ShelfIdentifierCache(cache_storage)
    player_token = shelf.get("player_token", None)
    game_token = shelf.get("game_token", None)
    client = api.HackgameClient(
        player_token=player_token,
        host=shelf.get("server_host", SERVER_HOSTS["dev"]),
        token=game_token,
        endpoint_cls=CLIObjectEndpoint,
        # endpoint kwargs,
        cache=cache,
    )

    with sentry_sdk.configure_scope() as scope:
        scope.user = {
            "id": game_token
        }

    return ClickObj(state=shelf, client=client, cache=cache,)


@click.group(context_settings=CONTEXT_SETTINGS, help=docs.HACKGAME_HELP)
@click.pass_context
@click.option(
    "--state-file",
    type=click.STRING,
    default=str(STATE_FILE),
    help=docs.STATE_FILE_HELP,
)
def cli(context, state_file):

    update_message = hackgame_update_notice()
    if update_message:
        click.echo(update_message)

    if context.obj is None:
        context.obj = get_context_obj(state_file)
    else:
        context.obj.nesting += 1


@cli.resultcallback()
@click.pass_context
def process_result(context, result, **kwargs):
    if context.obj.nesting == 0:
        context.obj.state.close()
    else:
        context.obj.nesting -= 1


@cli.command()
@click.pass_context
@click.option("--token", default=None)
def login(context, token):
    """Authenticate with the Hackgame Server"""
    state = context.obj.state
    if not token:
        host = state.get("server_host", SERVER_HOSTS["dev"])
        webbrowser.open(f"{host}/players/_cli_authentication/")
        token = auth.wait_for_token_reply()
    state["player_token"] = token
    click.echo("connected.")


@cli.command()
@click.pass_context
def shell(context):
    """Interactive Hackgame Shell"""
    click.echo(pyfiglet.Figlet(font="slant").renderText("hackgame"))

    click.echo("Type 'exit' to finish")
    click.echo()

    loop = True
    while loop:
        _messages = context.invoke(messages)
        user_input = click.prompt(prompt_suffix="$ ", text="")
        if user_input in ["quit", "exit"]:
            loop = False
        else:
            try:
                cli.main(
                    args=re.split(r"\s+", user_input.strip()),
                    standalone_mode=False,
                    obj=context.obj,
                )
            except click.UsageError as e:
                click.echo(str(e))
            except Exception as e:
                print(e)

    click.echo()
    click.echo("shutting down...")


class ObjectTypeParamType(click.ParamType):
    name = "object_type"

    lookup = {
        "account": Account,
        "player": Player,
        "token": AccessToken,
        "world": World,
        "network": Network,
        "connection": Connection,
        "program": Program,
        "ice": Ice,
    }

    def convert(self, value, param, ctx):

        try:
            return self.lookup[value]
        except KeyError:

            error_message = f"expected name of an object type, got {value}"
            objs = "\n".join([f"\t{name}" for name in self.lookup])
            error_help = f"valid OBJECT_TYPEs are:"
            self.fail(
                f"{error_message}\n\n{error_help}\n{objs}", param, ctx,
            )

    def complete(self, ctx, incomplete):
        match = completion_configuration.match_incomplete
        return [(key, "???") for key in self.lookup if match(key, incomplete)]


def is_valid_uuid(uuid_to_test, version=4):
    """
    Check if uuid_to_test is a valid UUID.

    Parameters
    ----------
    uuid_to_test : str
    version : {1, 2, 3, 4}

    Returns
    -------
    `True` if uuid_to_test is a valid UUID, otherwise `False`.

    Examples
    --------
    >>> is_valid_uuid('c9bf9e57-1685-4c89-bafb-ff5af830be8a')
    True
    >>> is_valid_uuid('c9bf9e58')
    False
    """
    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False

    return str(uuid_obj) == uuid_to_test


class IdentifierParamType(StringParamType):
    """A regular String input, but can use Identifier Cache for Auto-Complete."""

    def convert(self, value, param, ctx):
        if is_valid_uuid(value):
            return value

        object_type = ctx.params.get("object_type", None)
        cache: IdentifierCache = ctx.obj.cache

        matches = cache.lookup(value, object_type=object_type)
        if len(matches) == 0:
            self.fail("not a valid uuid and no matches found in cache for handle")
        elif len(matches) == 1:
            return list(matches)[0].public_uuid
        else:
            questions = [
                inquirer.List(
                    "object",
                    message="select the object that you meant",
                    choices=[m.handle for m in matches],
                ),
            ]
            answers = inquirer.prompt(questions)
            match = [m for m in matches if m.handle == answers["object"]][0]
            return match.public_uuid

    def complete(self, ctx, incomplete):
        if ctx.obj is None:
            ctx.obj = get_context_obj(str(STATE_FILE))

        object_type = ctx.params.get("object_type", None)

        cache: IdentifierCache = ctx.obj.cache
        matches = cache.lookup(incomplete, object_type=object_type)
        return [(m.handle, m.public_uuid) for m in matches]


class KeyValueParamType(click.ParamType):
    name = "key_value"

    def convert(self, value, param, ctx):
        try:
            key, value = value.split("=")
            return key, value
        except ValueError:
            error_message = f"expected key/value pair separated " f"by =, got {value}"
            self.fail(
                error_message, param, ctx,
            )


IDENTIFIER_TYPE = IdentifierParamType()
OBJECT_TYPE = ObjectTypeParamType()
KEY_VALUE = KeyValueParamType()


def _output(object_type, objects, output_format):
    click.echo()
    if output_format == "yaml":
        for obj in objects:
            click.echo(
                ruamel.yaml.safe_dump(attr.asdict(obj), default_flow_style=False)
            )
    elif output_format == "table":
        click.echo(
            tabulate(
                headers=object_type.headers(),
                tabular_data=[r.as_row() for r in objects],
            )
        )
    click.echo()


@cli.command()
@click.argument("object_type", type=OBJECT_TYPE)
@click.argument("public_uuid", type=IDENTIFIER_TYPE, default=None, required=False)
@click.option("--output", "-o", type=click.Choice(["table", "yaml"]), default="table")
@click.pass_context
def get(context, object_type, public_uuid, output):
    """
    Get public info about Objects in Hackgame
    """
    client = context.obj.client
    if public_uuid is not None:
        results = [client[object_type].get(public_uuid)]
    else:
        results = client[object_type].list()

    _output(object_type, results, output)


def create_account_flow(client: api.HackgameClient):
    handle = click.prompt("handle")
    networks = client.networks.list()

    questions = [
        inquirer.List(
            "network",
            message="Select a starting network",
            choices=[n.handle for n in networks],
        ),
    ]

    answers = inquirer.prompt(questions)
    network = [n for n in networks if n.handle == answers["network"]][0]
    return handle, network.public_uuid


def create_connection_flow(client: api.HackgameClient):
    handle = click.prompt("handle")
    target = click.prompt("target")
    return handle, target


def _echo_action_result(action_result: ActionResult):
    click.echo(
        f"success: {action_result.success}, status_code: {action_result.status_code}"
    )
    for message in action_result.messages:
        click.echo(message)
    for error in action_result.errors:
        click.echo(error.message)

    click.echo()
    click.echo(ruamel.yaml.safe_dump(action_result.data, default_flow_style=False))
    click.echo()


@cli.command()
@click.argument("object_type", type=OBJECT_TYPE)
@click.argument("public_uuid", type=IDENTIFIER_TYPE, default=None, required=False)
@click.argument("data", type=KEY_VALUE, nargs=-1)
@click.pass_context
def post(context, object_type, public_uuid, data):
    """Send requests to Objects"""
    client = context.obj.client
    _data = {k: v for k, v in data}
    action_result = client[object_type].post(public_uuid, _data)
    _echo_action_result(action_result)


@cli.command()
@click.argument("object_type", type=OBJECT_TYPE)
@click.argument("public_uuid", type=IDENTIFIER_TYPE, default=None, required=False)
@click.argument("data", type=KEY_VALUE, nargs=-1)
@click.pass_context
def transfer(context, object_type, public_uuid, data):
    """Send things"""
    client = context.obj.client
    _data = {k: v for k, v in data}
    action_result = client[object_type].transfer(public_uuid, _data)
    _echo_action_result(action_result)


@cli.command()
@click.argument("object_type", type=OBJECT_TYPE)
@click.option("--output", "-o", type=click.Choice(["table", "yaml"]), default="table")
@click.pass_context
def create(context, object_type, output):
    """Create new Objects"""
    client = context.obj.client
    if object_type == Account:
        handle, network_uuid = create_account_flow(client)
        obj = client[object_type].create(
            data={"handle": handle, "router": network_uuid}
        )
    elif object_type == Connection:
        handle, target = create_connection_flow(client)
        obj = client[object_type].create(data={"handle": handle, "target": target,})
    else:
        raise ClickException("not yet implemented")

    _output(object_type, [obj], output)


@cli.command()
@click.argument("object_type", type=OBJECT_TYPE)
@click.argument("public_uuid", type=IDENTIFIER_TYPE)
@click.pass_context
def proxy(context, object_type, public_uuid):
    """Change the Object your Token allows you to act as"""
    client = context.obj.client
    action_result = client[object_type].proxy(public_uuid)
    _echo_action_result(action_result)


@cli.command()
@click.argument("object_type", type=OBJECT_TYPE)
@click.argument("public_uuid", type=IDENTIFIER_TYPE)
@click.pass_context
def describe(context, object_type, public_uuid):
    """Get private info from an Object"""
    client = context.obj.client
    action_result = client[object_type].describe(public_uuid)
    _echo_action_result(action_result)


def use_token_flow(client: api.HackgameClient):

    tokens = client.tokens.list()

    questions = [
        inquirer.List(
            "token", message="Select a token", choices=[t.handle for t in tokens],
        ),
    ]

    answers = inquirer.prompt(questions)
    token = [t for t in tokens if t.handle == answers["token"]][0]
    return token.public_uuid


def create_account_flow(client: api.HackgameClient):
    handle = click.prompt("handle")
    networks = client.networks.list()

    questions = [
        inquirer.List(
            "network",
            message="Select a starting network",
            choices=[n.handle for n in networks],
        ),
    ]

    answers = inquirer.prompt(questions)
    network = [n for n in networks if n.handle == answers["network"]][0]
    return handle, network.public_uuid


@cli.command()
@click.argument("object_type", type=OBJECT_TYPE)
@click.argument("public_uuid", type=IDENTIFIER_TYPE, default=None, required=False)
@click.pass_context
def use(context, object_type, public_uuid):
    """Configure your current token"""
    state = context.obj.state
    client = context.obj.client
    if not issubclass(object_type, AccessToken):
        raise ClickException("`use` is only needed for setting token right now")

    if public_uuid is None:
        public_uuid = use_token_flow(client)

    token_obj = client.tokens.get(public_uuid=public_uuid)
    if token_obj:
        click.echo(f"using token {token_obj.handle}")
    else:
        raise ClickException(f"couldn't find token {public_uuid}")
    state["game_token"] = public_uuid


@cli.command(hidden=True)
@click.argument("name", type=click.Choice([k for k in SERVER_HOSTS]))
@click.pass_context
def use_server(context, name):
    """Configure Environment for hackgame (e.g. working locally)"""
    state = context.obj.state
    address = SERVER_HOSTS[name]
    state["server_host"] = address


@cli.command(hidden=True)
@click.pass_context
def show_state(context):
    state = context.obj.state
    click.echo(ruamel.yaml.dump(dict(state.items()), default_flow_style=False))


@cli.command()
@click.pass_context
def status(context):
    client = context.obj.client
    token = context.obj.state.get("game_token", None)
    if token is None:
        click.echo("you haven't set a token via `use`")
    else:
        token_obj = client.tokens.get(public_uuid=token)
        _output(AccessToken, [token_obj], output_format="yaml")


@cli.command()
@click.pass_context
def messages(context):
    """Receive any messages you are waiting for"""
    client = context.obj.client
    state = context.obj.state

    messages_after = state.get("messages_after", None)

    now = datetime.now(timezone.utc)
    _messages = client.messages(after=messages_after)
    [click.echo(m) for m in _messages]
    state["messages_after"] = now

    return _messages


@cli.command()
@click.pass_context
def help(context):
    """Get information about commands and what they do"""
    click.echo(cli.get_help(ctx=context))


@cli.command()
@click.option(
    "--shell",
    help="Shell to install auto-completion for",
    type=Choice(["bash", "fish"]),
)
def autocomplete(shell=None):
    """Install Shell Auto-completion"""
    shell, path = click_completion.core.install(shell=shell)
    click.echo("%s completion installed in %s" % (shell, path))


# for command in [get, proxy, use, create]:
#     command.short_help = command.help
#     command.help += docs.OBJECT_TYPE_HELP


if __name__ == "__main__":
    cli()
