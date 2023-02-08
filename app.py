import folium
import pandas as pd
import streamlit as st
from folium.plugins import HeatMap, MarkerCluster, Search
from streamlit_folium import st_folium

st.title('Mapping Potholes')

ret = st.selectbox("Map Type", ('scatter', 'heatmap', 'clusters'), index=0)

sel_opt= st.sidebar.selectbox('Map Style', ('Street View', 'Satellite', 'Water Color', 'High Contrast Toner'))

if sel_opt == 'Street View':
    selected_tiles = 'OpenStreetMap'
elif sel_opt == 'Satellite':
    selected_tiles = 'stamen terrain'
elif sel_opt == 'Water Color':
    selected_tiles = 'stamen water color'
elif sel_opt == 'High Contrast Toner':
    selected_tiles = 'stamen toner'


map = folium.Map(location=[51.5075932,-0.1455952], zoom_start=14, tiles=selected_tiles)


def plot_dot(point):
    folium.CircleMarker(location=[point.Latitude, point.Longitude],
                        radius=4,
                        weight=2, 
                        color='red',
                        fill= True,
                        fill_color='red').add_to(map)

# Read potholes data from csv.
df_acc = pd.read_csv('test-cv.csv', dtype=object)

data = pd.DataFrame(df_acc, columns=['Latitude', 'Longitude'])

df_acc['Latitude'] = df_acc['Latitude'].astype(float)
df_acc['Longitude'] = df_acc['Longitude'].astype(float)

clean_df = df_acc[['Latitude', 'Longitude']]
clean_df = clean_df.dropna(axis=0, subset=['Latitude','Longitude'])
clean_data = [[row['Latitude'],row['Longitude']] for index, row in clean_df.iterrows()]

if ret == 'heatmap':
    HeatMap(clean_data).add_to(map)

elif ret == 'scatter':
    data.apply(plot_dot, axis=1)
    
elif ret == "clusters":
    MarkerCluster(clean_data).add_to(map)

st_data = st_folium(map, height=400, width=1920)