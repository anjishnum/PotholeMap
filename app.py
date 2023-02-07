import folium
import pandas as pd
import streamlit as st
from folium.plugins import HeatMap
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

ret = st.selectbox("Map Type", ('scatter', 'heatmap', 'satellite', 'street view'), index=0)
print(ret)

# Read potholes data from csv.
df_acc = pd.read_csv('test-cv.csv', dtype=object)

data = pd.DataFrame(df_acc, columns=['Latitude', 'Longitude'])
# print(data[0:5])
# print(data)
# Ensure you're handing it floats
df_acc['Latitude'] = df_acc['Latitude'].astype(float)
df_acc['Longitude'] = df_acc['Longitude'].astype(float)

if ret == 'heatmap':
    heat_df = df_acc[['Latitude', 'Longitude']]
    heat_df = heat_df.dropna(axis=0, subset=['Latitude','Longitude'])
    heat_data = [[row['Latitude'],row['Longitude']] for index, row in heat_df.iterrows()]
    HeatMap(heat_data).add_to(map)

elif ret == 'scatter':
    data.apply(plot_dot, axis=1)
    # m.fit_bounds(m.get_bounds())

elif ret == 'satellite':
    map = folium.Map(location=[51.521709, -0.212653], zoom_start=13, tiles='Stamen Terrain')

else:
    pass

st_data = st_folium(map, height=400, width=1920)