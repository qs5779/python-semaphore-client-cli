"""Top level module ping in semaphore_client_cli package."""

import time
import semaphore_client
from semaphore_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = semaphore_client.DefaultApi()

try:
    # PING test
    api_response = api_instance.ping_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ping_get: %s\n" % e)
