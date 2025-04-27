# ui/property_cards.py

import streamlit as st

def display_property_cards(properties):
    st.subheader("🏡 Property Matches")

    for idx, prop in enumerate(properties):
        with st.expander(f"🔍 {prop.get('headline', 'No Title')}"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"📍 **Address:** {prop.get('address', 'Unknown')}")
                st.write(f"🏠 **Type:** {prop.get('propertyType', 'Unknown')}")
            with col2:
                st.write(f"💲 **Price:** {prop.get('price', 'N/A')}")
            
            # Save button inside the modal
            if st.button(f"⭐ Save to Favorites", key=f"save_{idx}"):
                if "favorites" not in st.session_state:
                    st.session_state.favorites = []
                st.session_state.favorites.append(prop)
                st.success("Property saved to favorites!")
