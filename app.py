import folium
import streamlit as st
from folium.plugins import HeatMap, MarkerCluster, Search
from streamlit_folium import st_folium
import random
import numpy as np
import base64

def plot_marker(map_obj, img_path, location=[13.014138, 77.632786]):
    # Get base64 encoded image data.
    with open(img_path, 'rb') as f:
            b64_img = base64.b64encode(f.read()).decode()

    # html iFrame.
    html = '<img src="data:image/png;base64,{}">'.format(b64_img)
    iframe = folium.IFrame(html, width=(6*75)+20, height=(4*75)+20)
    popup = folium.Popup(iframe, max_width=2650)
    folium.Marker(location=location, popup=popup).add_to(map_obj)
        

# Streamlit app initialize.
st.title('Indian Cities Mapping')
# Define folium map plugin with location and zoom value.
map = folium.Map(location=[13.014138, 77.632786], zoom_start=13)

# Add markers according to location.
plot_marker(map, 'images/plots.png', location=[13.014138, 77.632786])

# Keep on adding for other locations.
plot_marker(map, 'images/mangalore.png', location=[12.897591, 74.854924])

# View folium map in streamlit.
st_data = st_folium(map, height=400, width=1920)