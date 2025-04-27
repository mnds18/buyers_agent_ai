# pages/3_🎯_Portfolio_Strategy_Coach.py

import sys
import os
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from agents.portfolio_tracker_agent import load_portfolio
from simulations.portfolio_growth_simulator import simulate_growth

st.set_page_config(page_title="Portfolio Strategy Coach", layout="wide")
st.title("🎯 Portfolio Strategy Coach")

# --- Load Portfolio
portfolio_df = load_portfolio()

if portfolio_df.empty:
    st.warning("🚫 No properties in your portfolio yet. Add some properties first!")
else:
    # --- Current Portfolio Summary ---
    total_properties = len(portfolio_df)
    total_value = portfolio_df["Price"].sum()

    st.markdown("## 🧠 Your Current Investment Profile")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="🏡 Total Properties", value=total_properties)
    with col2:
        st.metric(label="💲 Total Portfolio Value", value=f"${total_value:,.0f}")

    st.markdown("---")

    # --- Simple Strategy Coaching Logic ---
    st.markdown("## 🛤️ Recommended Next Action")

    if total_properties <= 1 and total_value < 1000000:
        st.success("🛒 **Recommendation:** Consider purchasing another investment property within 6-12 months to build momentum.")
    elif total_properties >= 2 and total_value < 1500000:
        st.info("💰 **Recommendation:** Focus on stabilizing rental income, reduce debt, and prepare for next strategic purchase.")
    elif total_value >= 1500000:
        st.warning("🏦 **Recommendation:** You may be eligible for refinancing to unlock equity and accelerate portfolio growth.")

    st.markdown("---")

    st.markdown("## 📈 Portfolio Value Over Time")

    years = list(range(2024, 2029))
    values = [total_value* (1.05 ** i) for i in range(5)]  # Assume 5% growth per year

    fig, ax = plt.subplots()
    ax.plot(years, values, marker='o')
    ax.set_xlabel("Year")
    ax.set_ylabel("Projected Value ($)")
    ax.set_title("Projected Portfolio Value Growth")

    st.pyplot(fig)

    # --- Future Growth Simulation (If User Buys Another Property) ---
    st.markdown("## 🚀 Simulate Growing Faster by Adding a Property")

    additional_investment = st.number_input("Simulate Buying Additional Property ($)", min_value=100000, max_value=2000000, step=50000, value=500000)

    if st.button("📈 Simulate Future Growth Scenario"):
        new_total_investment = total_value + additional_investment
        simulated = simulate_growth(years=5, annual_growth_rate=0.06)  # Assume 6% growth
        projected_with_additional = simulated["Projected Portfolio Value"] + (additional_investment * (1.06)**5)

        st.success(f"📈 After buying an additional ${additional_investment:,} property, in 5 years your portfolio could be worth approximately **${projected_with_additional:,.0f}**!")

st.markdown("---")

st.caption("Powered by Buyers Agent AI | Guiding Your Financial Freedom Journey")
