import sys
import types
import urllib
from http.cookiejar import parse_ns_headers
from pprint import pprint
from typing import NoReturn

import click
from loguru import logger
from semaphore_client import Login
from semaphore_client.api_client import ApiClient
from semaphore_client.configuration import Configuration
from semaphore_client.api.authentication_api import AuthenticationApi
from semaphore_client.rest import ApiException
from wtforglib.options import Options, basic_options

from semaphore_client_cli.config import app_cfg, cfg
from semaphore_client_cli.constants import VERSION

CONTEXT_SETTINGS = types.MappingProxyType({"help_option_names": ["-h", "--help"]})



def authenticate(config: Configuration) -> tuple[str, int]:
    """Authenticate on semaphore server.

    :param config: The configuration object
    :type config: Configuration
    :return: 0 if successful, 2 if unsuccessful
    :rtype: int
    """
    client = ApiClient(config)
    auth = AuthenticationApi(client)
    login_body = Login(auth=config.username, password=config.password)
    auth.auth_login_post(login_body)
    cookie = client.last_response.getheader('Set-Cookie')
    if not cookie:
        return "", 2
    parsed = parse_ns_headers([cookie])
    for vv in parsed:
        # pprint(vv)
        # pprint(vv[0])
        pprint(vv[0][0])
        # pprint(vv[0][0][0])
        if vv[0][0] == "semaphore":
            return vv[0][1], 0
    return "", 3

@click.command()
def next() -> NoReturn:
    config = Configuration()
    cookie, rtn = authenticate(config)
    if rtn != 0:
        sys.exit(rtn)
    logger.debug("Auth Cookie: {0}".format(cookie))
    config.api_key["Cookie"] = cookie
    config.api_key_prefix['Cookie'] = 'Bearer'
    config.api_key["Authorization"] = cookie
    config.api_key_prefix['Authorization'] = 'Bearer'
    client = ApiClient(config)
    auth = AuthenticationApi(client)
    auth.user_tokens_get()
    sys.exit(rtn)


@click.command()
def start() -> NoReturn:
    """Start task on semaphore server."""
    config = Configuration()
    cookie, rtn = authenticate(config)
    if rtn != 0:
        sys.exit(rtn)
    # Configure API key authorization: bearer
    configuration = Configuration()
    # configuration.api_key["Authorization"] = "YOUR_API_KEY"
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # configuration.api_key_prefix['Authorization'] = 'Bearer'
    # Configure API key authorization: cookie
    configuration.api_key["Cookie"] = cookie
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
