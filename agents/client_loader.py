# agents/client_loader.py

import json
import os
import random

def load_dummy_clients():
    data_file = os.path.join("data", "dummy_clients.json")
    with open(data_file, "r") as f:
        clients = json.load(f)
    return clients

def get_random_client():
    clients = load_dummy_clients()
    return random.choice(clients)

if __name__ == "__main__":
    # Quick Test
    client = get_random_client()
    print(client)
