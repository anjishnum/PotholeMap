import streamlit as st
import folium
from streamlit_folium import st_folium
import base64
import matplotlib.pyplot as plt

def plot():
    # return jpeg image of the plot
    pass

def cvt_base64():
    # return iframe
    pass

st.title('my first streamlit app')

ret = st.selectbox('select map type',('terrain','contour'))
print(ret)

map = folium.Map(location=[22.269, 79.717], zoom_start=5, tiles='OpenStreetMap')





# add popup image
html = '''1st line<br>
2nd line<br>
3rd line'''

iframe = folium.IFrame(html,
                       width=100,
                       height=100)

popup = folium.Popup(iframe,
                     max_width=100)

folium.Marker(location=[12.97,77.59],popup=popup).add_to(map)

# Circle marker for Bengaluru
folium.Circle(
    location=[12.97,77.59],
    radius=30000,
    popup='Bengaluru',
    color='#428bca',
    fill=True,
    fill_color='#428bca'
).add_to(map)

st_data = st_folium(map, height=400, width=1920)

