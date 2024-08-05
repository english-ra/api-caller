import os
import requests
import time
from auth import get_access_token

def api_caller(access_token, call):
    response_code = None
    try_count = 0
    retry_limit = 3

    while (response_code in {429, 401} or try_count == 0) and try_count < retry_limit:
        try_count += 1
        if try_count != 1:
            print(f"Retrying... (Attempt: {try_count})")
        try:
            response = requests.request(
                method=call['method'],
                url=f"https://{os.getenv('INSTANCE_URL')}/api/{call['endpoint']}",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {access_token}"
                },
                json=call['payload']
            )

            response_code = response.status_code
            print(f"Response status: {response.status_code} {response.reason}")

            if response_code == 429:
                print("Rate limit reached. Retrying in 1 minute...")
                time.sleep(60)
                continue

            if response_code == 401:
                print("Token needs regenerating")
                access_token = get_access_token()
                continue

            # response.raise_for_status()
            return response.json()

        except requests.RequestException as error:
            print("Failed to fetch tickets:", error)
