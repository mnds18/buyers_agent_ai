# agents/domain_api_agent.py

import requests
import os
import base64

DOMAIN_CLIENT_ID = os.getenv("DOMAIN_CLIENT_ID")
DOMAIN_CLIENT_SECRET = os.getenv("DOMAIN_CLIENT_SECRET")

# Get OAuth2 Token
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

# Search properties
def search_properties(location="Sydney", max_price=1000000):
    token = get_domain_access_token()

    url = "https://api.domain.com.au/v1/listings/residential/_search"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    body = {
        "listingType": "Sale",
        "maxPrice": max_price,
        "propertyTypes": ["House", "ApartmentUnitFlat"],
        "locations": [
            {
                "state": "NSW",
                "region": location
            }
        ],
        "pageSize": 5
    }

    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()

    listings = response.json()
    return listings
