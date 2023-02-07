import folium
import pandas as pd
import streamlit as st
from folium.plugins import HeatMap, MarkerCluster
from streamlit_folium import st_folium

map = folium.Map(location=[51.521709, -0.212653], zoom_start=13)


def plot_dot(point):
    folium.CircleMarker(location=[point.Latitude, point.Longitude],
                        radius=4,
                        weight=2, 
                        color='red',
                        fill= True,
                        fill_color='red').add_to(map)


st.title('Mapping Potholes')

ret = st.selectbox("Map Type", ('scatter', 'heatmap', 'satellite', 'test'), index=0)
print(ret)

# Read potholes data from csv.
df_acc = pd.read_csv('test-cv.csv', dtype=object)

data = pd.DataFrame(df_acc, columns=['Latitude', 'Longitude'])

df_acc['Latitude'] = df_acc['Latitude'].astype(float)
df_acc['Longitude'] = df_acc['Longitude'].astype(float)

clean_df = df_acc[['Latitude', 'Longitude']]
clean_df = clean_df.dropna(axis=0, subset=['Latitude','Longitude'])
clean_data = [[row['Latitude'],row['Longitude']] for index, row in clean_df.iterrows()]

# if ret == 'heatmap':
#     HeatMap(clean_data).add_to(map)

# elif ret == 'scatter':
#     data.apply(plot_dot, axis=1)
    

# elif ret == "Reactive":
#     MarkerCluster(clean_data).add_to(map)


# Test code.
HeatMap(clean_data).add_to(map)
data.apply(plot_dot, axis=1)
MarkerCluster(clean_data).add_to(map)
folium.LayerControl().add_to(map)

st_data = st_folium(map, height=400, width=1920)