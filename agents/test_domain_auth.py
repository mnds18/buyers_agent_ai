# test_domain_auth.py

import os
import requests
import base64

# Load your environment variables
DOMAIN_CLIENT_ID = os.getenv("DOMAIN_CLIENT_ID")
DOMAIN_CLIENT_SECRET = os.getenv("DOMAIN_CLIENT_SECRET")

def get_domain_access_token():
    url = "https://auth.domain.com.au/v1/connect/token"
    credentials = f"{DOMAIN_CLIENT_ID}:{DOMAIN_CLIENT_SECRET}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "client_credentials",
        "scope": "api_listings_read"
    }

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

if __name__ == "__main__":
    token = get_domain_access_token()
    print("\n✅ Successfully fetched Access Token:\n")
    print(token)
