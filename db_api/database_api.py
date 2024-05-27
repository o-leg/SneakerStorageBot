import requests

from config import DB_API_URL, DB_API_AUTH_TOKEN


def perform_request(body=None):
    if body is None:
        body = dict()

    url = DB_API_URL
    headers = {
        "Authorization": DB_API_AUTH_TOKEN
    }

    response = requests.post(url, headers=headers, json=body)

    # Handle the response
    if response.status_code == 200:
        # Successful request
        return response.json()
    return {}
