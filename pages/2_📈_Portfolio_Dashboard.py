# ui/dashboard.py

import sys
import os
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from agents.portfolio_tracker_agent import load_portfolio, get_portfolio_summary
from simulations.portfolio_growth_simulator import simulate_growth
import pandas as pd

st.set_page_config(page_title="Portfolio Dashboard", layout="wide")
st.title("🏡 Portfolio Dashboard")

# --- Load Portfolio Data ---
portfolio_df = load_portfolio()
summary = get_portfolio_summary()

if portfolio_df.empty:
    st.warning("🚫 No properties in your portfolio yet. Start adding some from the Property Matches page!")
else:
    # --- Portfolio KPIs ---
    st.markdown("## 📊 Portfolio Overview")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="🏡 Total Portfolio Value", value=f"${summary['Total Portfolio Value']:,.0f}")
    with col2:
        st.metric(label="📄 Total Properties Owned", value=summary["Total Properties"])

    st.markdown("---")

    # --- Growth Simulations ---
    st.markdown("## 📈 Simulate Future Portfolio Growth")

    col_growth1, col_growth2 = st.columns(2)

    with col_growth1:
        years = st.selectbox("Select Growth Simulation Years", options=[5, 10, 15], index=1)
    with col_growth2:
        annual_growth_rate = st.slider("Expected Annual Growth Rate (%)", min_value=2.0, max_value=10.0, value=5.0)

    simulation_result = simulate_growth(years=years, annual_growth_rate=annual_growth_rate/100)

    if simulation_result:
        st.success(f"📈 In {years} years, your portfolio could grow to approximately **${simulation_result['Projected Portfolio Value']:,.0f}** at {simulation_result['Annual Growth Rate']} annual growth.")

    st.markdown("---")

    # --- Table of Properties ---
    st.markdown("## 📋 Current Properties in Portfolio")
    st.dataframe(portfolio_df)

    # --- Export Portfolio to CSV ---
    csv = portfolio_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Portfolio as CSV",
        data=csv,
        file_name='portfolio_snapshot.csv',
        mime='text/csv',
    )

    st.markdown("## 📈 Portfolio Value Over Time")

    years = list(range(2024, 2029))
    values = [summary['Total Portfolio Value'] * (1.05 ** i) for i in range(5)]  # Assume 5% growth per year

    fig, ax = plt.subplots()
    ax.plot(years, values, marker='o')
    ax.set_xlabel("Year")
    ax.set_ylabel("Projected Value ($)")
    ax.set_title("Projected Portfolio Value Growth")

    st.pyplot(fig)