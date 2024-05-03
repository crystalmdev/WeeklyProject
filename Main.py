import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium, folium_static
from folium.plugins import MiniMap


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

st.title('Korea Travel Guide 🌎')
# st.header('Korea Map 🗺️')
selected_city = st.selectbox('Select the city you plan to travel',
               options = list(locs.keys()),
                index = 0)



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

    elif selected_city == 'Seoul':
        df = df[df['지자체'].str.contains('서울')]
        zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=11)
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

    elif selected_city == 'Incheon':
        df = df[df['지자체'].str.contains('인천')]
        zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=11)
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

    elif selected_city == 'Gwangju':
        df = df[df['지자체'].str.contains('광주')]
        zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=11)
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

    elif selected_city == 'Daegu':
        df = df[df['지자체'].str.contains('대구')]
        zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=11)
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

    elif selected_city == 'Ulsan':
        df = df[df['지자체'].str.contains('울산')]
        zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=11)
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

    elif selected_city == 'Daejeon':
        df = df[df['지자체'].str.contains('대전')]
        zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=11)
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

    elif selected_city == 'Busan':
        df = df[df['지자체'].str.contains('부산')]
        zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=11)
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

    elif selected_city == 'Gyeonggi-do':
        df = df[df['지자체'].str.contains('경기')]
        zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=9)
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

    elif selected_city == 'Sejong':
        df = df[df['지자체'].str.contains('세종')]
        zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=11)
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

    elif selected_city == 'Gangwon':
        df = df[df['지자체'].str.contains('강원')]
        zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=8)
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

    elif selected_city == 'Chungnam':
        df = df[df['지자체'].str.contains('충남')]
        zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=8)
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

    elif selected_city == 'Chungbuk':
        df = df[df['지자체'].str.contains('충북')]
        zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=8)
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

    elif selected_city == 'Gyeongbuk':
        df = df[df['지자체'].str.contains('경북')]
        zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=8)
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

    elif selected_city == 'Gyeongnam':
        df = df[df['지자체'].str.contains('경남')]
        zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=8)
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

    elif selected_city == 'jeonbuk':
        df = df[df['지자체'].str.contains('전북')]
        zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=8)
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

    elif selected_city == 'Jeonnam':
        df = df[df['지자체'].str.contains('전남')]
        zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=8)
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

    elif selected_city == 'jeju':
        df = df[df['지자체'].str.contains('제주')]
        zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=8)
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

    else:
        zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=20, value=10)
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

    # st_folium(my_map)
    folium_static(my_map, width=600, height=400)

# lotte = [35.1961130003038, 129.213344761055]

# st.map()



