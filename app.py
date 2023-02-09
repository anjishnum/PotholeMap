import folium
import pandas as pd
import streamlit as st
from folium.plugins import HeatMap, MarkerCluster, Search
from streamlit_folium import st_folium
import random
import numpy as np
import base64


# Fix randomization.
SEED = 42
np.random.seed(SEED)
random.seed(SEED)

# Read potholes data from csv.
df_acc = pd.read_csv('test-cv.csv', dtype=object)
df_acc = df_acc.sample(10)

# Convert series data to DataFrame.
data = pd.DataFrame(df_acc, columns=['Latitude', 'Longitude'])

# Assert Convert to Float.
df_acc['Latitude'] = df_acc['Latitude'].astype(float)
df_acc['Longitude'] = df_acc['Longitude'].astype(float)

clean_df = df_acc[['Latitude', 'Longitude', 'Diameter', 'Date']]

# Clean NAN values.
clean_df = clean_df.dropna(axis=0, subset=['Latitude','Longitude', 'Diameter', 'Date'])

# Get locations as a list of lists.
clean_data = [[row['Latitude'], row['Longitude'], row['Diameter'], row['Date']] for index, row in clean_df.iterrows()]

# Get clean location.
clean_data_loc = [[row['Latitude'], row['Longitude']] for index, row in clean_df.iterrows()]

# Streamlit app initialize.
st.title('Mapping Potholes')

# Define selectbox for map layers.
ret = st.selectbox("Map Type", ('scatter', 'heatmap', 'clusters'), index=0)

# Define selectbox on the sidebar for choosing map types.
sel_opt= st.sidebar.selectbox('Map Style', ('Street View', 'Satellite', 'Water Color', 'High Contrast Toner'))

# Types of views.
if sel_opt == 'Street View':
    selected_tiles = 'OpenStreetMap'
elif sel_opt == 'Satellite':
    selected_tiles = 'stamen terrain'
elif sel_opt == 'Water Color':
    selected_tiles = 'stamen water color'
elif sel_opt == 'High Contrast Toner':
    selected_tiles = 'stamen toner'

# Define folium map plugin with location and zoom value.
map = folium.Map(location=[51.5075932,-0.1455952], zoom_start=14, tiles=selected_tiles)

# Define a marker cluster.
marker_cluster = MarkerCluster().add_to(map)

# Function for scatter plot.
def plot_dot(point):
    folium.CircleMarker(location=[point.Latitude, point.Longitude],
                        radius=4,
                        weight=2, 
                        color='red',
                        fill= True,
                        fill_color='red').add_to(map)



if ret == 'heatmap':
    HeatMap(clean_data_loc).add_to(map)

elif ret == 'scatter':
    data.apply(plot_dot, axis=1)
    
elif ret == "clusters":
    for point in clean_data:
        lat, lon, dia, date = point
        folium.Marker(location=[lat, lon],
                    popup=f"Pothole \n Diameter: {dia} ft, \n Date: {date} , \n Location: {lat}, {lon}").add_to(marker_cluster)
    
# View folium map in streamlit.
st_data = st_folium(map, height=400, width=1920)