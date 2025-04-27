# pages/1_🏡_Property_Search.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from orchestration.run_pipeline import run_buyers_agent_pipeline
from agents.chat_agent import chat_with_agent
from agents.client_loader import load_dummy_clients
from agents.suburb_ranking_agent import recommend_suburbs
from ui.property_cards import display_property_cards
from fpdf import FPDF
import folium
from streamlit_folium import st_folium

# Setup page
st.set_page_config(page_title="Property Search", layout="wide")
st.title("🏡 Property Search - Find Investment Opportunities")

# Initialize session state
for key in ["messages", "favorites", "search_results"]:
    if key not in st.session_state:
        st.session_state[key] = []

# Sidebar - Chat Interface
st.sidebar.title("💬 Chat with Buyers Agent AI")
user_query = st.sidebar.text_input("Ask me anything about properties:")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    response = chat_with_agent(user_query)
    st.session_state.messages.append({"role": "agent", "content": response})

for message in st.session_state.messages:
    if message["role"] == "user":
        st.sidebar.markdown(f"**🧑 You:** {message['content']}")
    else:
        st.sidebar.success(f"🤖 {message['content']}")

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []

# Sidebar - Smart Filters
st.sidebar.title("🔎 Smart Property Search")

# Load dummy ABS-like data
state_region_map = {
    "NSW": ["Sydney - Inner City", "Newcastle and Lake Macquarie", "Wollongong", "Central Coast"],
    "VIC": ["Melbourne - Inner", "Geelong", "Ballarat"],
    "QLD": ["Brisbane Inner City", "Gold Coast", "Sunshine Coast"],
    "SA": ["Adelaide - Central", "Mount Gambier"],
    "WA": ["Perth - Inner", "Mandurah"],
}

selected_state = st.sidebar.selectbox("Select State", options=list(state_region_map.keys()), index=0)

# If State is selected, show Region
region_options = state_region_map.get(selected_state, [])
selected_region = st.sidebar.selectbox("Select Region (SA4/SA3)", options=["(I don't know)"] + region_options)

# (Optional) Map Picker
st.sidebar.markdown("---")
st.sidebar.write("Or select a location directly on map:")

m = folium.Map(location=[-25.2744, 133.7751], zoom_start=4)
map_selection = st_folium(m, width=300, height=400)

selected_latlon = None
if map_selection and map_selection.get("last_clicked"):
    latlon = map_selection["last_clicked"]
    selected_latlon = (latlon["lat"], latlon["lng"])
    st.sidebar.success(f"Map Selected: Lat {selected_latlon[0]:.4f}, Lon {selected_latlon[1]:.4f}")

# Load clients
clients = load_dummy_clients()
client_names = [client["name"] for client in clients]

selected_client_name = st.sidebar.selectbox("Select Dummy Client", ["(Manual Entry)"] + client_names)

with st.sidebar.form("property_filters"):
    if selected_client_name == "(Manual Entry)":
        selected_budget = st.number_input("Budget (AUD)", min_value=200000, max_value=3000000, step=50000, value=1000000)
        selected_goal = st.selectbox("Investment Goal", ["high_growth", "high_yield"])
    else:
        selected_client = next(c for c in clients if c["name"] == selected_client_name)
        selected_budget = selected_client["budget"]
        selected_goal = selected_client["investment_goal"]

        st.markdown(f"**Budget:** ${selected_budget:,}")
        st.markdown(f"**Goal:** {selected_goal.replace('_', ' ').title()}")

    submitted = st.form_submit_button("Find Properties")

# Main Area
st.header("🔹 Property Results")

# If form submitted
if submitted:
    # Handle "I don't know" case
    if selected_region == "(I don't know)":
        st.info("🔎 You didn't select a region. Recommending top suburbs based on your goal...")
        recommendations = recommend_suburbs(goal=selected_goal, top_n=5)
        selected_location = recommendations[0]["Suburb"]
        st.success(f"✅ Based on your profile, we recommend starting with **{selected_location}**.")
    elif selected_latlon:
        selected_location = f"Lat {selected_latlon[0]:.2f}, Lon {selected_latlon[1]:.2f}"
        st.success(f"✅ Using map selected location: {selected_location}")
    else:
        selected_location = selected_region

    results = run_buyers_agent_pipeline(
        budget=selected_budget,
        location=selected_location,
        investment_goal=selected_goal
    )

    st.success(f"Showing results for **{selected_location}** under ${selected_budget:,} targeting {selected_goal.replace('_', ' ').title()}!")

    st.markdown("---")

    if results and "Properties" in results:
        top_properties = results["Properties"][:5]
        st.session_state.search_results = [
            {
                "headline": prop.get("name", "No Title"),
                "address": prop.get("address", "Unknown Address"),
                "price": prop.get("price", "N/A"),
                "propertyType": prop.get("propertyType", "Unknown Type"),
                "latitude": prop.get("latitude", None),
                "longitude": prop.get("longitude", None)
            }
            for prop in top_properties
        ]

        display_property_cards(st.session_state.search_results)
    else:
        st.warning("No properties found. Try adjusting your search filters.")

# If not submitted but there are search results, display them
elif st.session_state.search_results:
    display_property_cards(st.session_state.search_results)
else:
    st.info("Please select your preferences from the sidebar and click 'Find Properties'.")

