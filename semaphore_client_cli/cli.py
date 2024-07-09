import sys
import types
from pprint import pprint
from typing import NoReturn

import click
import semaphore_client
from semaphore_client.api.authentication_api import AuthenticationApi
from semaphore_client.rest import ApiException
from wtforglib.options import Options, basic_options

from semaphore_client_cli.config import app_cfg, cfg
from semaphore_client_cli.constants import VERSION

CONTEXT_SETTINGS = types.MappingProxyType({"help_option_names": ["-h", "--help"]})


@click.command()
def next() -> NoReturn:
    config = semaphore_client.Configuration()
    auth = AuthenticationApi()
    login_body = semaphore_client.Login(auth=config.username, password=config.password)
    res = auth.auth_login_post(login_body)


@click.command()
def start() -> NoReturn:
    """Start task on semaphore server."""
    # Configure API key authorization: bearer
    configuration = semaphore_client.Configuration()
    configuration.api_key["Authorization"] = "YOUR_API_KEY"
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # configuration.api_key_prefix['Authorization'] = 'Bearer'
    # Configure API key authorization: cookie
    configuration = semaphore_client.Configuration()
    configuration.api_key["Cookie"] = "YOUR_API_KEY"
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # configuration.api_key_prefix['Cookie'] = 'Bearer'

    # create an instance of the API class
    api_instance = semaphore_client.ProjectApi(
        semaphore_client.ApiClient(configuration)
    )
    project_id = 1  # int | Project ID
    task = semaphore_client.Task()  # Task |

    try:
        # Starts a job
        api_response = api_instance.project_project_id_tasks_post(project_id, task)
        pprint(api_response)
        rtn = 0
    except ApiException as e:
        print(
            "Exception when calling ProjectApi->project_project_id_tasks_post: %s\n" % e
        )
        rtn = 1

    # ### Parameters

    # Name | Type | Description  | Notes
    # ------------- | ------------- | ------------- | -------------
    #  **project_id** | **int**| Project ID |
    #  **task** | [**Task**](Task.md)|  |

    # ### Return type

    # [**Task**](Task.md)

    # ### Authorization

    # [bearer](../README.md#bearer), [cookie](../README.md#cookie)

    # ### HTTP request headers

    #  - **Content-Type**: application/json
    #  - **Accept**: application/json, text/plain; charset=utf-8
    sys.exit(rtn)


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
    app_cfg.initialize(Options(od), cfg.log_level)
    return 0


main.add_command(next)
main.add_command(ping)

if __name__ == "__main__":
    sys.exit(main())  # pragma no cover
