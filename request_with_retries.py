# Goal is to do a requests and handle timeout when doing the request
# I believe requests handle correctly timeouts establishing the connection 
# but not when the connection is already establish
import requests
import time
import traceback
import sys

def do_request_with_retries(request, max_retries):
    retries = 0
    response = None
    while retries < max_retries:
        try:
            response = requests.get(request)
            break
        except Exception as e:
            retries += 1
            print("[!] Uh! {str(e)}", file=sys.stderr)
            # A bit intense, but useful
            traceback.print_exc()
            # Exponential backoff
            time.sleep(2 ** retries)
    if retries == max_retries:
        return False
    # Do something with response
    return response.json()

do_request_with_retries("https://www.google.com", 10)