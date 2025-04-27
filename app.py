# app.py

import streamlit as st
from streamlit_extras.app_logo import add_logo  # Optional: for sidebar branding
import sys
import os

# (Optional) Fix path if needed
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

st.set_page_config(
    page_title="Buyers Agent AI",
    page_icon="🏡",
    layout="wide",
)

# --- Landing Page Design ---
st.title("🏡 Buyers Agent AI")
st.subheader("Find, Plan, and Grow Your Property Portfolio Smarter")

st.markdown("""
Welcome to **Buyers Agent AI** — your personal AI-powered property buying assistant!

Whether you're:
- 🏠 A first-time investor
- 💼 A portfolio builder
- 📈 Looking for data-driven suburb recommendations
- 🎯 Wanting to simulate your future wealth

We've got you covered with powerful tools — **at a fraction of traditional buyers agent costs.**

---
""")

# --- Quick Start Buttons ---

st.markdown("### 🚀 Quick Start")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔎 Start Property Search"):
        st.switch_page("pages/1_🏡_Property_Search.py")

with col2:
    if st.button("📊 View Portfolio Dashboard"):
        st.switch_page("pages/2_📈_Portfolio_Dashboard.py")

with col3:
    if st.button("🎯 Get Strategy Advice"):
        st.switch_page("pages/3_🎯_Portfolio_Strategy_Coach.py")

st.markdown("---")

# --- How it Works Section ---

st.markdown("### 📋 How It Works")

st.markdown("""
1. **Find the Best Suburbs:** Using AI-powered DSR data analysis
2. **Save Properties:** Build your shortlist
3. **Grow Your Portfolio:** Track growth, simulate future wealth
4. **Strategize:** Get smart next-move advice
""")

st.markdown("---")

# --- Footer ---
st.caption("© 2025 Buyers Agent AI | Built for Smart Investors 🚀")
