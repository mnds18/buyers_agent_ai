# scripts/generate_dummy_properties.py

import random
import json
import os
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

# Dummy suburb data
suburbs_data = [
    {"suburb": "Sydney", "state": "NSW", "lat": -33.8688, "lon": 151.2093},
    {"suburb": "Newcastle", "state": "NSW", "lat": -32.9283, "lon": 151.7817},
    {"suburb": "Wollongong", "state": "NSW", "lat": -34.4278, "lon": 150.8931},
    {"suburb": "Melbourne", "state": "VIC", "lat": -37.8136, "lon": 144.9631},
    {"suburb": "Geelong", "state": "VIC", "lat": -38.1499, "lon": 144.3617},
    {"suburb": "Brisbane", "state": "QLD", "lat": -27.4698, "lon": 153.0251},
    {"suburb": "Gold Coast", "state": "QLD", "lat": -28.0167, "lon": 153.4},
    {"suburb": "Sunshine Coast", "state": "QLD", "lat": -26.65, "lon": 153.0667},
    {"suburb": "Adelaide", "state": "SA", "lat": -34.9285, "lon": 138.6007},
    {"suburb": "Perth", "state": "WA", "lat": -31.9505, "lon": 115.8605},
    {"suburb": "Canberra", "state": "ACT", "lat": -35.2809, "lon": 149.13},
    {"suburb": "Darwin", "state": "NT", "lat": -12.4634, "lon": 130.8456},
    {"suburb": "Hobart", "state": "TAS", "lat": -42.8821, "lon": 147.3272},
]

property_types = ["House", "Apartment"]

def generate_dummy_properties(n=750):
    properties = []
    for _ in range(n):
        suburb_info = random.choice(suburbs_data)

        prop_type = random.choice(property_types)
        bedrooms = random.choice([1, 2, 3, 4, 5]) if prop_type == "House" else random.choice([1, 2])
        bathrooms = random.choice([1, 2, 3])

        # Price ranges
        if suburb_info["state"] in ["NSW", "VIC"]:
            price = random.randint(600000, 2000000)
        elif suburb_info["state"] == "QLD":
            price = random.randint(400000, 1500000)
        else:
            price = random.randint(350000, 1200000)

        # 🔥 Smart Rent Calculation
        # Assume rental yield between 4% - 6% p.a.
        expected_yield = suburb_info.get("Yield_Percentage", random.uniform(0.04, 0.06))
        annual_rent = price * expected_yield
        weekly_rent = annual_rent / 52
        weekly_rent = int(round(weekly_rent / 10.0) * 10)

        lat = suburb_info["lat"] + random.uniform(-0.01, 0.01)
        lon = suburb_info["lon"] + random.uniform(-0.01, 0.01)

        address = f"{fake.street_address()}, {suburb_info['suburb']} {suburb_info['state']}"

        properties.append({
            "name": f"{bedrooms}BR {prop_type} in {suburb_info['suburb']}",
            "address": address,
            "price": price,
            "weekly_rent": weekly_rent,  # 🆕 ADDED
            "propertyType": prop_type,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "latitude": round(lat, 6),
            "longitude": round(lon, 6)
        })
    return properties

def save_properties(properties):
    output_path = os.path.join("data", "dummy_properties.json")
    with open(output_path, "w") as f:
        json.dump(properties, f, indent=4)
    print(f"✅ Saved {len(properties)} properties with rent info to {output_path}")

if __name__ == "__main__":
    properties = generate_dummy_properties(750)
    save_properties(properties)
