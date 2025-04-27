# agents/property_fetcher.py

import os
import requests
import base64

def get_domain_access_token():
    DOMAIN_CLIENT_ID = os.getenv("DOMAIN_CLIENT_ID")
    DOMAIN_CLIENT_SECRET = os.getenv("DOMAIN_CLIENT_SECRET")

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

def search_properties(location="Sydney", max_price=1000000):
    token = get_domain_access_token()

    url = "https://api.domain.com.au/v1/listings/residential/_search"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    body = {
        "listingType": "Sale",
        "propertyTypes": ["House", "ApartmentUnitFlat"],
        "locations": [
            {
                "state": "NSW",
                "region": location
            }
        ],
        "maxPrice": max_price,
        "pageSize": 5
    }

    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    listings = response.json()

    # Transform response into simpler format
    properties = []
    for listing in listings:
        properties.append({
            "headline": listing.get("headline", "No Title"),
            "price": listing.get("priceDetails", {}).get("displayPrice", "N/A"),
            "address": listing.get("propertyDetails", {}).get("displayableAddress", "Unknown Address"),
            "propertyType": listing.get("propertyDetails", {}).get("propertyType", "Unknown Type"),
        })

    return properties

if __name__ == "__main__":
    props = search_properties(location="Newcastle", max_price=750000)
    for p in props:
        print(p)
