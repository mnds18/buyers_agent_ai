# scripts/seed_portfolio.py

import pandas as pd
import os

portfolio_path = os.path.join("data", "user_portfolio.csv")

# Dummy purchased properties
dummy_properties = [
    {"Property_Name": "Modern 3BR House", "Address": "123 Sample St, Newcastle NSW", "Price": 750000, "Purchase_Date": "2023-07-15"},
    {"Property_Name": "Luxury 2BR Apartment", "Address": "45 King St, Melbourne VIC", "Price": 650000, "Purchase_Date": "2024-01-10"},
    {"Property_Name": "Family Home 4BR", "Address": "78 Coastal Ave, Sunshine Coast QLD", "Price": 820000, "Purchase_Date": "2024-03-05"}
]

df = pd.DataFrame(dummy_properties)
df.to_csv(portfolio_path, index=False)

print("✅ Dummy portfolio seeded successfully.")
