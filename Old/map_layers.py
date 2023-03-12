import folium
import pandas as pd
import streamlit as st
from folium.plugins import HeatMap, MarkerCluster
from streamlit_folium import st_folium

st.title('Mapping Potholes Test')

map_geo = folium.Map(location=[57.8,14.14], zoom_start=10, width=1200)

folium.raster_layers.WmsTileLayer(url ='https://maps3.sgu.se/geoserver/jord/ows?',
                layers = 'SE.GOV.SGU.JORD.TACKNINGSKARTA.25K',
                transparent = False, 
                control = True,
                fmt="image/png",
                name = 'SGU',
                attr = 'im seeing this',
                overlay = True,
                show = True,
                CRS = 'EPSG:900913',
                version = '1.3.0',
                ).add_to(map_geo)

folium.LayerControl().add_to(map_geo)

st_folium(map_geo, height=400, width=2000)