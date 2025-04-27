# generate_dummy_data.py

import random
import json
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

# Major Australian cities and regions
cities = [
    "Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Canberra", "Hobart", "Darwin",
    "Newcastle", "Wollongong", "Geelong", "Gold Coast", "Sunshine Coast", "Townsville", "Cairns"
]

# Simple suburb to lat/lon map (approximate)
city_lat_lon = {
    "Sydney": (-33.8688, 151.2093),
    "Melbourne": (-37.8136, 144.9631),
    "Brisbane": (-27.4698, 153.0251),
    "Perth": (-31.9505, 115.8605),
    "Adelaide": (-34.9285, 138.6007),
    "Canberra": (-35.2809, 149.13),
    "Hobart": (-42.8821, 147.3272),
    "Darwin": (-12.4634, 130.8456),
    "Newcastle": (-32.9283, 151.7817),
    "Wollongong": (-34.4278, 150.8931),
    "Geelong": (-38.1499, 144.3617),
    "Gold Coast": (-28.0167, 153.4),
    "Sunshine Coast": (-26.65, 153.0667),
    "Townsville": (-19.2589, 146.8169),
    "Cairns": (-16.9186, 145.7781)
}

property_types = ["House", "Apartment"]
investment_goals = ["high_growth", "high_yield"]

# Generate dummy properties
def generate_properties(n=1000):
    properties = []
    for _ in range(n):
        city = random.choice(cities)
        lat, lon = city_lat_lon[city]
        # Randomize a bit around the city lat/lon
        lat += random.uniform(-0.05, 0.05)
        lon += random.uniform(-0.05, 0.05)

        prop_type = random.choice(property_types)
        if prop_type == "House":
            bedrooms = random.choice([2, 3, 4, 5])
            bathrooms = random.choice([1, 2, 3])
        else:  # Apartment
            bedrooms = random.choice([1, 2])
            bathrooms = random.choice([1, 2])

        price = random.randint(
            400000 if city not in ["Sydney", "Melbourne"] else 600000,
            2000000 if city in ["Sydney", "Melbourne"] else 1200000
        )

        street_address = fake.street_address()
        headline = f"{random.choice(['Modern', 'Spacious', 'Luxurious', 'Cozy', 'Elegant'])} {bedrooms}BR {prop_type} in {city}"

        properties.append({
            "name": headline,
            "address": f"{street_address}, {city}, Australia",
            "price": price,
            "propertyType": prop_type,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "latitude": round(lat, 6),
            "longitude": round(lon, 6)
        })
    return properties

# Generate dummy clients
def generate_clients(n=200):
    clients = []
    for _ in range(n):
        name = fake.name()
        age = random.randint(21, 75)
        budget = random.randint(400000, 2000000)
        preferred_location = random.choice(cities)
        clients.append({
            "name": name,
            "age": age,
            "investment_goal": random.choice(investment_goals),
            "preferred_property_type": random.choice(property_types),
            "budget": budget,
            "preferred_location": preferred_location
        })
    return clients

def main():
    properties = generate_properties(1000)
    clients = generate_clients(200)

    with open("data/dummy_properties.json", "w") as f:
        json.dump(properties, f, indent=4)

    with open("data/dummy_clients.json", "w") as f:
        json.dump(clients, f, indent=4)

    print("✅ Dummy data generated successfully!")
    print(f"🏡 {len(properties)} properties saved to data/dummy_properties.json")
    print(f"👥 {len(clients)} clients saved to data/dummy_clients.json")

if __name__ == "__main__":
    main()
