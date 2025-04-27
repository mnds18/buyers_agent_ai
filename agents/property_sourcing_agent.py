# agents/property_sourcing_agent.py

import json
import os

# Try importing Domain API searcher
try:
    from agents.domain_api_agent import search_properties as domain_search_properties
except ImportError:
    domain_search_properties = None

# Switch to easily control dummy vs live
USE_DUMMY_DATA = True

def load_dummy_properties():
    data_file = os.path.join("data", "dummy_properties.json")
    with open(data_file, "r") as f:
        properties = json.load(f)
    return properties

def source_properties(location, budget):
    if USE_DUMMY_DATA:
        print("🟢 Using Dummy Property Data")
        all_properties = load_dummy_properties()
        filtered = [
            p for p in all_properties
            if location.lower() in p["address"].lower()
            and p["price"] <= budget
        ]
        return filtered[:10]  # Return top 10 matches
    else:
        print("🔴 Using Live Domain API Data")
        if domain_search_properties:
            return domain_search_properties(location=location, max_price=budget)
        else:
            raise Exception("Domain API integration not available or configured.")

if __name__ == "__main__":
    # Test run
    props = source_properties(location="Newcastle", budget=800000)
    for p in props:
        print(p)
