import folium
import streamlit as st
from folium.plugins import HeatMap, MarkerCluster, Search
from streamlit_folium import st_folium
import random
import numpy as np
import base64

def encode_img(img_path):
    with open(img_path, "rb") as f:
        encoded_str = base64.b64decode(f.read())
    
    return encoded_str


# Get base64 encoded image data.
b64_img = encode_img("plots.png")

# html iFrame.
html = '<img src="data:image/png;base64,{}">'.format
iframe = folium.IFrame(html(b64_img), width=(7*75)+20, height=(4*75)+20)
popup = folium.Popup(iframe, max_width=2650)


# Streamlit app initialize.
st.title('Mapping Potholes')

# Define folium map plugin with location and zoom value.
map = folium.Map(location=[51.5075932,-0.1455952], zoom_start=13)

folium.Marker(location=[13.014138, 77.632786], popup=popup).add_to(map)

    
# View folium map in streamlit.
st_data = st_folium(map, height=400, width=1920)