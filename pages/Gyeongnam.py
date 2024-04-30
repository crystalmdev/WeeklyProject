import streamlit as st
from PIL import Image

st.header('Gyeongnam')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Geochang Iris Garden', 'Hapcheon Image Theme Park', 'SpaTheSpace',\
                                        'Dongpirang Village', 'Skyline Luge Tongyeong'])

with tab1:
    st.subheader('Geochang Iris Garden')
    with st.container(height=200):
        st.markdown('''
            Geochang Iris Garden is located in Wolpyeong-ri, Namsang-myeon, and was located in a submerged area when the Hapcheon Dam was built in 1988.
    This is the place where farmers have been growing rice.
    In Geochang-gun, an ecological garden that matches the waterside scenery of the Hwanggang River, a national river, was created to reduce agricultural pollution sources.
    Geochang Iris Garden was created to protect river water quality and revitalize the local economy through tourism resources.
    Iris is a plant that purifies water and has the traditional custom and practicality of washing one's hair on Danot Day.
    Iris has a beautiful appearance, as its name comes from the meaning of 'blooming more beautiful flowers than irises.'
    It is a very beautiful flower.
    In the spring, more than 1 million irises planted form a beautiful colony, and in the summer, the theme is lotus, water lily, and hydrangea.
    There are four seasons with the theme of chrysanthemums and maple leaves in the fall, and silver grass and reeds around the tropical botanical garden, reservoir, and wetlands in the winter.
        ''')
    st.divider()

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('**Introduction**')
        st.image(Image.open('./img/인화/woljeong_bridge.jpg'),
                 use_column_width=True)