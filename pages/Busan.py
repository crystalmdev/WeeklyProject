import streamlit as st
import numpy as np
from PIL import Image

st.header('Busan 예시: 참고용')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Lotte World Adventure Busan', '2번 장소', '3', '4', '5'])

with tab1:
    st.subheader('Lotte World Adventure Busan')
    with st.container(height=100):
        st.markdown('''Lotte World Adventure Busan was founded in 2023~~~ also it is well known for 
        its popular ~~~~ 해당 장소 간단 설명 / 구글 번역기 돌려도 됨! / 문법 확인하고 싶으면 'Grammarly' 사이트 사용하시면 됩니다''')
    st.divider()

    col1, col2 = st.columns([1,1])

    with col1:
        st.markdown('**Introduction**')
        st.image(Image.open('./img/lotte.jpg'),
                 use_column_width=True)

    with col2:
        st.markdown('**Similar Destinations**')
        row1 = st.columns(2)
        row2 = st.columns(2)

        rec_place = ['Lotte World Seoul', 'etc', 'etc', 'etc']
        rec_place_img = ['./img/ltseoul.png', './img/everland.jpeg', './img/gjworld.jpeg', './img/carrbay.jpeg']
        rec_caption = ['theme park located in seoul... etc 기타 간단한 영어 설명 - 번역기 돌려도 됨', 'theme park located in seoul... etc', 'theme park located in seoul... etc', 'theme park located in seoul... etc']

        for i, col in enumerate(row1 + row2):
            tile = col.expander(rec_place[i])
            tile.image(Image.open(rec_place_img[i]),
                 caption=rec_caption[i],
                 use_column_width=True)

    # expander = st.expander('expander')
    # expander.write('expander')
    st.divider()


    col1, col2 = st.columns([1,1])

    with col1:
        st.markdown('**WordCloud**')
        st.text('(based on Korean blog reviews)')
        st.image(Image.open('./img/wordcloud.png'),
                 use_column_width=True)
    with col2:
        st.markdown('**Top 20 Keywords**')
        st.text('(based on Korean blog reviews)')
        st.image(Image.open('./img/graph.png'),
                 use_column_width=True)


tab2.subheader('Second Location')
st.divider()
