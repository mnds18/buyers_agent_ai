# pages/0_🧠_Onboarding_Wizard.py

import streamlit as st

st.set_page_config(page_title="Onboarding Wizard", layout="wide")
st.title("🧠 Welcome to Buyers Agent AI - Onboarding Wizard")

st.markdown("Help us understand your investment goals!")

# Step 1: Basic Info
st.subheader("👤 Personal Details")
full_name = st.text_input("Full Name")
email = st.text_input("Email Address")

# Step 2: Investment Goals
st.subheader("🎯 Investment Preferences")
budget = st.number_input("Max Budget (AUD)", min_value=200000, max_value=3000000, step=50000, value=750000)
investment_goal = st.selectbox("Primary Goal", ["High Growth", "High Yield", "Balanced"])
timeline = st.selectbox("Investment Timeline", ["Short-term (1-3 years)", "Medium-term (3-7 years)", "Long-term (7+ years)"])
experience_level = st.selectbox("Investment Experience", ["First-time Buyer", "Some Experience", "Experienced Investor"])

# Save profile
if st.button("🚀 Save and Start Using Platform"):
    st.session_state.user_profile = {
        "name": full_name,
        "email": email,
        "budget": budget,
        "goal": investment_goal,
        "timeline": timeline,
        "experience": experience_level
    }
    st.success("✅ Profile Saved! Use sidebar to navigate now.")

st.markdown("---")
st.caption("Buyers Agent AI | Personalizing your investment journey 🚀")
