# simulations/portfolio_growth_simulator.py

import pandas as pd
import os

PORTFOLIO_FILE_PATH = os.path.join("data", "user_portfolio.csv")

def load_portfolio():
    if os.path.exists(PORTFOLIO_FILE_PATH):
        df = pd.read_csv(PORTFOLIO_FILE_PATH)
    else:
        df = pd.DataFrame(columns=["Property_Name", "Address", "Price", "Purchase_Date"])
    return df

def simulate_growth(years=5, annual_growth_rate=0.05):
    df = load_portfolio()
    if df.empty:
        return None

    # Calculate future values
    df["Projected_Value"] = df["Price"] * ((1 + annual_growth_rate) ** years)
    total_projected_value = df["Projected_Value"].sum()

    return {
        "Years": years,
        "Annual Growth Rate": f"{annual_growth_rate*100:.2f}%",
        "Projected Portfolio Value": round(total_projected_value, 2),
        "Properties": df.to_dict(orient="records")
    }

if __name__ == "__main__":
    print(simulate_growth(years=10, annual_growth_rate=0.07))
