# pages/4_💰_Rental_Income_Dashboard.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from agents.portfolio_tracker_agent import load_portfolio
from simulations.portfolio_growth_simulator import simulate_growth
import json
import matplotlib.pyplot as plt

# Setup page
st.set_page_config(page_title="Rental Income Dashboard", layout="wide")
st.title("💰 Rental Income Dashboard")

# Load Portfolio
portfolio_df = load_portfolio()

# Load dummy properties to extract weekly rents
dummy_properties_path = os.path.join("data", "dummy_properties.json")
if os.path.exists(dummy_properties_path):
    with open(dummy_properties_path, "r") as f:
        all_properties = json.load(f)
else:
    all_properties = []

# Helper to match property address and fetch rent
def get_weekly_rent(address):
    for prop in all_properties:
        if address.split(",")[1].strip() in prop["address"]:
            return prop.get("weekly_rent", 0)
    return 0

if portfolio_df.empty:
    st.warning("🚫 No properties in your portfolio yet. Add some properties first!")
else:
    st.markdown("## 🏠 Your Rental Portfolio")

    # Add Rental Income Columns
    portfolio_df["Weekly_Rent"] = portfolio_df["Address"].apply(get_weekly_rent)
    portfolio_df["Annual_Rent"] = portfolio_df["Weekly_Rent"] * 52
    portfolio_df["Rental_Yield_%"] = (portfolio_df["Annual_Rent"] / portfolio_df["Price"]) * 100

    # Show portfolio with rental incomes
    st.dataframe(portfolio_df[["Property_Name", "Address", "Price", "Weekly_Rent", "Annual_Rent", "Rental_Yield_%"]])

    st.markdown("---")

    # --- KPI Summary ---
    total_weekly_income = portfolio_df["Weekly_Rent"].sum()
    total_monthly_income = total_weekly_income * 4
    total_annual_income = portfolio_df["Annual_Rent"].sum()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="📅 Total Monthly Rental Income", value=f"${total_monthly_income:,.0f}")

    with col2:
        st.metric(label="📅 Total Annual Rental Income", value=f"${total_annual_income:,.0f}")

    with col3:
        avg_yield = portfolio_df["Rental_Yield_%"].mean()
        st.metric(label="🏠 Average Rental Yield", value=f"{avg_yield:.2f}%")

    st.markdown("---")

    # --- Passive Income Goal Progress Chart ---
    st.markdown("## 🎯 Progress Toward Passive Income Goal")

    passive_income_goal = st.slider("Set your Passive Income Goal (Monthly)", min_value=1000, max_value=20000, step=500, value=5000)

    goal_progress = (total_monthly_income / passive_income_goal) * 100
    goal_progress = min(goal_progress, 100)  # Cap at 100%

    fig, ax = plt.subplots(figsize=(6,3))
    ax.barh(["Progress"], [goal_progress], color="green")
    ax.set_xlim(0, 100)
    ax.set_xlabel("Progress %")
    ax.set_title("Progress Towards Passive Income Target")

    st.pyplot(fig)

    st.success(f"✅ You have achieved {goal_progress:.2f}% of your passive income goal of ${passive_income_goal:,}/month.")

st.markdown("---")
st.caption("Powered by Buyers Agent AI | Financial Freedom Made Smarter 🚀")
