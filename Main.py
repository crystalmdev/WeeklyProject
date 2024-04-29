import streamlit as st
import pandas as pd
import folium
# import folium.plugins import MarkerCluster
import numpy as np
import time # 이종혁


st.set_page_config(
    page_title='Korea Travel Guide 🌎',
    page_icon='🗺️',
    layout='wide',
    initial_sidebar_state='auto')

locs = {'서울시' : [37.540705, 126.956764],
    '인천광역시' : [37.469221, 126.573234],
    '광주광역시' : [35.126033, 126.831302],
    '대구광역시' : [35.798838, 128.583052],
    '울산광역시' : [35.519301, 129.239078],
    '대전광역시' : [36.321655, 127.378953],
    '부산광역시' : [35.198362, 129.053922],
    '경기도' : [37.567167, 127.190292],
    '세종시': [36.5040736, 127.2494855],
    '강원도' : [37.555837, 128.209315],
    '충청남도' : [36.557229, 126.779757],
    '충청북도' : [36.628503, 127.929344],
    '경상북도' : [36.248647, 128.664734],
    '경상남도' : [35.259787, 128.664734],
    '전라북도' : [35.716705, 127.144185],
    '전라남도' : [34.819400, 126.893113],
    '제주도' : [33.364805, 126.542671]}

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