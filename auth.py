import os
import requests

def get_access_token():
    print("Obtaining access token...")
    try:
        response = requests.post(
            f"https://{os.getenv('INSTANCE_URL')}/auth/token?tenant={os.getenv('TENANT')}",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "client_credentials",
                "scope": "all",
                "client_id": os.getenv("CLIENT_ID"),
                "client_secret": os.getenv("CLIENT_SECRET")
            }
        )
        response.raise_for_status()
        data = response.json()

        return data['access_token']
    except requests.RequestException as e:
        print("Error with obtaining access token: ", e)
        return None
