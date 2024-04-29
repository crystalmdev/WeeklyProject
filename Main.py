import streamlit as st
import pandas as pd
import folium
# import folium.plugins import MarkerCluster
import numpy as np
import re

st.set_page_config(
    page_title='Korea Travel Guide 🌎',
    page_icon='🗺️',
    layout='wide',
    initial_sidebar_state='auto')

locs = {'Seoul' : [37.540705, 126.956764],
    'Incheon' : [37.469221, 126.573234],
    'Gwangju' : [35.126033, 126.831302],
    'Daegu' : [35.798838, 128.583052],
    'Ulsan' : [35.519301, 129.239078],
    'Daejeon' : [36.321655, 127.378953],
    'Busan' : [35.198362, 129.053922],
    'Gyeonggi-do' : [37.567167, 127.190292],
    'Sejong': [36.5040736, 127.2494855],
    'Gangwon' : [37.555837, 128.209315],
    'Chungnam' : [36.557229, 126.779757],
    'Chungbuk' : [36.628503, 127.929344],
    'Gyeongbuk' : [36.248647, 128.664734],
    'Gyeongnam' : [35.259787, 128.664734],
    'jeonbuk' : [35.716705, 127.144185],
    'Jeonnam' : [34.819400, 126.893113],
    'jeju' : [33.364805, 126.542671]}

st.title('Korea Travel Guide 🌎')
st.header('Korea Map 🗺️')
selected_city = st.selectbox('Select the city you plan to travel',
               options = list(locs.keys()),
                index = 0)


df_loc = pd.DataFrame(locs).T
df_loc.columns = ['lat', 'lon']
zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=9)

if selected_city:
    st.map(df_loc.loc[[selected_city]], size=30, color='#00ff00', zoom = zoom_level)


lotte = [35.1961130003038, 129.213344761055]