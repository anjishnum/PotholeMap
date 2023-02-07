import folium
import pandas as pd
import streamlit as st
from folium.plugins import HeatMap, MarkerCluster
from streamlit_folium import st_folium

st.title('Mapping Potholes')

ret = st.selectbox("Map Type", ('scatter', 'heatmap', 'satellite', 'street view'), index=0)
# print(ret)
map = folium.Map(location=[51.521709, -0.212653], zoom_start=13)
# Read potholes data from csv.
df_acc = pd.read_csv('test-cv.csv', dtype=object)
df_acc = df_acc.sample(20)

clean_df = df_acc[['Latitude', 'Longitude']]
clean_df = clean_df.dropna(axis=0, subset=['Latitude','Longitude'])
clean_data = [[row['Latitude'],row['Longitude']] for _, row in clean_df.iterrows()]

data = pd.DataFrame(df_acc, columns=['Latitude', 'Longitude'])
# print(data[0:5])
# print(data)
# Ensure you're handing it floats
df_acc['Latitude'] = df_acc['Latitude'].astype(float)
df_acc['Longitude'] = df_acc['Longitude'].astype(float)

if ret == 'heatmap':
    HeatMap(clean_data).add_to(map)

elif ret == 'scatter':
    map = folium.Map(location=[51.521709, -0.212653], zoom_start=13)
    MarkerCluster(clean_df).add_to(map)
    

elif ret == 'satellite':
    map = map

st_data = st_folium(map, height=400, width=1920)