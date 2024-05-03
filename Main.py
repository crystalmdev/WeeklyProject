import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium, folium_static
from folium.plugins import MiniMap
import streamlit.components.v1 as components


df = pd.read_csv('data/관광지_위경도(최종3).csv')

st.set_page_config(
    page_title='Korea Travel Guide 🌎',
    page_icon='🗺️',
    layout='wide',
    initial_sidebar_state='auto')

locs = {
    'Korea' : [36.429, 127.977],
    'Seoul' : [37.540705, 126.956764],
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

kor = { 'Seoul' : ['서울', 11], 'Incheon' : ['인천', 11],
    'Gwangju' : ['광주', 11], 'Daegu' : ['대구', 11],
    'Ulsan' : ['울산', 11], 'Daejeon' : ['대전', 11],
    'Busan' : ['부산', 11], 'Gyeonggi-do' : ['경기도', 9],
    'Sejong': ['세종', 11], 'Gangwon' : ['강원', 9],
    'Chungnam' : ['충남', 9], 'Chungbuk' : ['충북', 9],
    'Gyeongbuk' : ['경북', 9], 'Gyeongnam' : ['경남', 9],
    'jeonbuk' : ['전북', 9], 'Jeonnam' : ['전남', 9], 'jeju' : ['제주', 9]}

dests = {
        'Seoul': ['Seoul Botanic Park', 'Lotte World', 'Gyeongbokgung Palace', 'Seokchonhosu Lake', "Seoul Children's Grand Park"],
         'Sejong': ['Sejong National Arboretum', 'Dodori Park', 'Gobok Reservoir', 'Jochiwon Theme Street', 'Sejong Attige'],
        'Busan' : ['Gwangalli beach', 'Lotte World Busan', 'Haeundae Beach', 'Dadaepo Beach', 'Haeundae Street food alley'],
        'Incheon' : ['Wolmido Island', 'Incheon Chinatown', 'Incheon Grand Park', 'Wolmi Theme Park', 'Songwol-dong Fairy Tale Village ']
}

st.title('Korea Travel Guide 🌎')
# st.header('Korea Map 🗺️')

st.text('사이트 소개글 넣기')

col1, col2= st.columns(2)

with col1:
    selected_city = st.selectbox(
        "Select the city/state you plan to travel",
        list(locs.keys()))

with col2:
    if selected_city == 'Korea':
        selected_dest = st.selectbox(
            "Select the destination you plan to travel",
            [item for sublist in dests.values() for item in sublist])
    elif selected_city in dests:
        selected_dest = st.selectbox(
            "Select the destination you plan to travel",
            dests[selected_city])

if selected_dest in [item for sublist in dests.values() for item in sublist]:
        for key, value_list in dests.items():
            if selected_dest in value_list:
                 st.page_link(f'pages/{key}.py', label=f'📍click for more info about :red[**{selected_dest}**]')

df_loc = pd.DataFrame(locs).T
df_loc.columns = ['lat', 'lon']
# zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=9)

if selected_city:
    if selected_city == 'Korea':
        zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=7)
        my_map = folium.Map(location=df_loc.loc[selected_city], zoom_start=zoom_level,
                            tiles='https://tiles.stadiamaps.com/tiles/osm_bright/{z}/{x}/{y}{r}.png',
                            attr='Stadia Maps'
                            )
        marker_cluster = MarkerCluster().add_to(my_map)
        for name, lat2, lon2 in zip(df['관광지'], df['위도'], df['경도']):
            folium.Marker([lat2, lon2],
                          popup=name,
                          tooltip=name,
                          icon=folium.Icon(icon='info-sign')
                          ).add_to(marker_cluster)

    elif selected_city in locs:
        df = df[df['지자체'].str.contains(kor[selected_city][0])]
        zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=kor[selected_city][1])
        my_map = folium.Map(location=df_loc.loc[selected_city], zoom_start=zoom_level,
                            tiles='https://tiles.stadiamaps.com/tiles/osm_bright/{z}/{x}/{y}{r}.png',
                            attr='Stadia Maps'
                            )
        for name, lat2, lon2 in zip(df['관광지'], df['위도'], df['경도']):
            folium.Marker([lat2, lon2],
                          popup=name,
                          tooltip=name,
                          icon=folium.Icon(icon='info-sign')
                          ).add_to(my_map)

    minimap = MiniMap(width=100, height=100)
    minimap.add_to(my_map)

    folium_static(my_map, width=1000, height=800)