# agents/market_data_agent.py

import json
import os
import random


USE_DUMMY_DATA = True  # Same control flag as in property sourcing

def load_dummy_properties():
    data_file = os.path.join("data", "dummy_properties.json")
    with open(data_file, "r") as f:
        properties = json.load(f)
    return properties

def fetch_market_data(location):
    if USE_DUMMY_DATA:
        print("🟢 Using Dummy Market Data")
        all_properties = load_dummy_properties()
        matching_props = [
            p for p in all_properties
            if location.lower() in p["address"].lower()
        ]

        # 🔥 ADD THIS FALLBACK
        if not matching_props:
            print(f"⚠️ No direct matches for {location}, using all properties for fallback.")
            matching_props = all_properties  # fallback to all properties

        if not matching_props:
            return None

        avg_price = sum(p["price"] for p in matching_props) / len(matching_props)
        rental_yield = round(random.uniform(3.0, 6.0), 2)

        market_info = {
            "location": location,
            "average_price": round(avg_price, 2),
            "average_rental_yield": f"{rental_yield}%",
            "number_of_listings": len(matching_props)
        }
        return market_info
    else:
        print("🔴 Live Market Data fetching not configured yet")
        return None


if __name__ == "__main__":
    data = fetch_market_data("Newcastle")
    print(data)
