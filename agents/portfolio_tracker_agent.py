# agents/portfolio_tracker_agent.py

import pandas as pd
import os

PORTFOLIO_FILE_PATH = os.path.join("data", "user_portfolio.csv")

def load_portfolio():
    if os.path.exists(PORTFOLIO_FILE_PATH):
        df = pd.read_csv(PORTFOLIO_FILE_PATH)
    else:
        df = pd.DataFrame(columns=["Property_Name", "Address", "Price", "Purchase_Date"])
    return df

def add_property_to_portfolio(property_info):
    df = load_portfolio()
    new_entry = {
        "Property_Name": property_info.get("headline", "Unknown"),
        "Address": property_info.get("address", "Unknown"),
        "Price": property_info.get("price", 0),
        "Purchase_Date": pd.Timestamp.now().strftime("%Y-%m-%d")
    }
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(PORTFOLIO_FILE_PATH, index=False)

def get_portfolio_summary():
    df = load_portfolio()
    total_value = df["Price"].sum()
    property_count = len(df)
    return {"Total Portfolio Value": total_value, "Total Properties": property_count}

if __name__ == "__main__":
    # Test
    test_property = {
        "headline": "Modern 3BR Townhouse",
        "address": "123 Test St, Brisbane",
        "price": 750000
    }
    add_property_to_portfolio(test_property)
    print(get_portfolio_summary())
