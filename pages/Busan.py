import streamlit as st
import numpy as np
from PIL import Image

st.header('Busan 🌎')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['롯데월드 어드벤처 부산', '해운대 해수욕장', '서면', '기타', '등등'])
with tab1:
    st.subheader('롯데월드 어드벤처 부산')

    col1, col2 = st.columns([1,1])

    with col1:
        st.text('관광지 소개')
        st.image(Image.open('./img/lotte.jpg'),
                 caption='롯데월드 어드벤처 부산',
                 use_column_width=True)

    with col2:
        st.text('유사 관광지 추천')
        row1 = st.columns(2)
        row2 = st.columns(2)

        rec_place = ['롯데월드 서울', '에버랜드', '경주월드', '캐리비안베이']
        rec_place_img = ['./img/ltseoul.png', './img/everland.jpeg', './img/gjworld.jpeg', './img/carrbay.jpeg']
        rec_caption = ['서울에 위치한 롯데월드 테마파크', '용인에 위치한 테마파크', '경주에 위치한 테마파크', '용인에 위치한 워터파크']

        for i, col in enumerate(row1 + row2):
            tile = col.expander(rec_place[i])
            tile.image(Image.open(rec_place_img[i]),
                 caption=rec_caption[i],
                 use_column_width=True)

    # expander = st.expander('expander')
    # expander.write('expander')

    col1, col2 = st.columns([1,1])

    with col1:
        st.image(Image.open('./img/wordcloud.png'),
                 use_column_width=True)
    with col2:
        st.image(Image.open('./img/graph.png'),
                 use_column_width=True)


    st.divider()

    col1, col2, col3 = st.columns([1,2,2],
                                  gap='medium') #1:2:2의 비율로 화면 분할
    data = np.random.rand(10,1)

    with col1:
        st.subheader('영역1')
        st.metric('점수', 55, 0.5)

    with col2:
        st.line_chart(data)

    with col3:
        st.bar_chart(data)


tab2.subheader('해운대 해수욕장')