# pages/5_🗺️_Passive_Income_Heatmaps.py

import sys
import os
import streamlit as st
import folium
import json
from streamlit_folium import st_folium

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

st.set_page_config(page_title="Passive Income Heatmaps", layout="wide")
st.title("🗺️ Passive Income Heatmaps")

# Load dummy properties
dummy_properties_path = os.path.join("data", "dummy_properties.json")
with open(dummy_properties_path, "r") as f:
    properties = json.load(f)

st.markdown("### Top Suburbs by Rental Yield")

m = folium.Map(location=[-25.2744, 133.7751], zoom_start=5)

for prop in properties:
    lat = prop.get("latitude")
    lon = prop.get("longitude")
    if lat and lon:
        popup = f"{prop['name']}<br>Rent: ${prop['weekly_rent']}/wk"
        rent_to_price = (prop["weekly_rent"] * 52) / prop["price"]
        if rent_to_price > 0.06:
            color = "green"
        elif rent_to_price > 0.045:
            color = "orange"
        else:
            color = "red"
        folium.CircleMarker(
            location=[lat, lon],
            radius=5,
            popup=popup,
            color=color,
            fill=True,
            fill_opacity=0.7
        ).add_to(m)

st_folium(m, width=900, height=600)
