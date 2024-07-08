import sys
import types
from pprint import pprint
from typing import NoReturn

import click
import semaphore_client
from semaphore_client.rest import ApiException
from wtforglib.options import Options, basic_options

from semaphore_client_cli.config import cfg
from semaphore_client_cli.constants import VERSION

CONTEXT_SETTINGS = types.MappingProxyType({"help_option_names": ["-h", "--help"]})


@click.command()
def ping() -> NoReturn:
    """Ping semaphore server."""
    # create an instance of the API class
    api_instance = semaphore_client.DefaultApi()

    try:
        # PING test
        api_response = api_instance.ping_get()
        pprint(api_response)
        rtn = 0
    except ApiException as ex:
        click.echo("Exception when calling DefaultApi->ping_get: {0}".format(ex))
        rtn = 1
    sys.exit(rtn)


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option("-c", "--config", required=False, default="", help="Specify config file")
@click.option("-d", "--debug", count=True, default=0, help="bump debug level")
@click.option("-t", "--test/--no-test", default=False, help="specify test mode")
@click.option("-v", "--verbose", count=True, default=0, help="bump verbose level")
@click.version_option(VERSION)
def main(config: str, debug: int, test: bool, verbose: int) -> int:
    """Provides single interface to several common Linux package managers."""
    od = basic_options(debug, test, verbose)
    od["config"] = config
    cfg.app_config.initialize(Options(od), cfg.log_level)
    return 0


main.add_command(ping)

if __name__ == "__main__":
    sys.exit(main())  # pragma no cover
