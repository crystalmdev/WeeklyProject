import streamlit as st
from PIL import Image
import numpy as np # TEST


st.header('Busan')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Gwangalli beach', 'Lotte World Busan', 'Haeundae Beach', 'Dadaepo Beach', 'Haeundae Street food alley'])

# --------------------------(광안리해수욕장)-------------------------

with tab1:
    st.subheader('Gwangalli beach')
    col1, col2, col3, col4 = st.columns([1.5,1.3,1,1])
    with col1:
        st.markdown('**How To Get There:**')
    with col2:
        st.page_link('https://www.google.co.kr/maps/place/%EA%B4%91%EC%95%88%EB%A6%AC%ED%95%B4%EC%88%98%EC%9A%95%EC%9E%A5/data=!3m1!4b1!4m6!3m5!1s0x3568ed2f27c70ec7:0xff6df0e14d9216fb!8m2!3d35.1531696!4d129.118666!16s%2Fm%2F03hp9yc?hl=ko&entry=ttu',
                     label='Google Map', icon='🗺️')
    with col3:
        st.page_link('https://www.letskorail.com/ebizbf/EbizbfForeign_pr16100.do?gubun=1',
                     label='Train', icon='🚃')
    with col4:
        st.page_link('https://www.kobus.co.kr/main.do',
                     label='bus', icon='🚌')

    with st.container(height=190):
        st.markdown('''Located to the west of Haeundae Beach, Gwangalli Beach 
        is 1.4 kilometers long and 25~110 meters wide, and is famous for its 
        fine sand. Gwangalli area is filled with delicious restaurants
         and romantic cafes, as well as stores selling famous fashion brands. 
         Many people come in the evening to take in the bright lights of Gwangandaegyo Bridge, stretching across 
         the horizon.''')
    st.divider()

    col1, col2 = st.columns([1,1])

    with col1:
        st.markdown('**Introduction**')
        st.image(Image.open('./img/수정/광안리해수욕장.jpeg'),
                 use_column_width=True)

    with col2:
        st.markdown('**Similar Destinations**')
        row1 = st.columns(2)
        row2 = st.columns(2)

        rec_place = ['Lotte World Seoul', 'etc', 'etc', 'etc']
        rec_place_img = ['./img/예시/ltseoul.png', './img/예시/everland.jpeg', './img/예시/gjworld.jpeg', './img/예시/carrbay.jpeg']
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
        st.image(Image.open('./img/예시/wordcloud.png'),
                 use_column_width=True)
    with col2:
        st.markdown('**Top 20 Keywords**')
        st.text('(based on Korean blog reviews)')
        st.image(Image.open('./img/예시/graph.png'),
                 use_column_width=True)

# --------------------------(롯데월드 어드밴처 부산)-------------------------

with tab2:
    st.subheader('Lotte World Busan')
    st.link_button('Google Map', 'https://www.google.co.kr/maps/place/%ED%95%B4%EC%9A%B4%EB%8C%80%ED%95%B4%EC%88%98%EC%9A%95%EC%9E%A5/data=!3m1!4b1!4m6!3m5!1s0x35688d5c0efe075f:0x9963b1d5c163ac98!8m2!3d35.1586975!4d129.1603842!16s%2Fm%2F03bx6xl?hl=ko&entry=ttu')
    # st.markdown('**Train: 3hrs 24 min / Bus: 5hrs 2 min** (departure from seoul)')
    with st.container(height=150):
        st.markdown('''Lotte World Adventure Busan, 
        offers visitors to experience fun and exciting performances 
        and parades. It consists of six themed zones.  At the heart of the fairy village, 
        Tinker Falls Zone, is the Talking Tree, which uses animatronic technology 
        to tell the story of six themes in the park.''')
    st.divider()

    col1, col2 = st.columns([1,1])

    with col1:
        st.markdown('**Introduction**')
        st.image(Image.open('./img/수정/롯데월드부산.jpg'),
                 use_column_width=True)

    with col2:
        st.markdown('**Similar Destinations**')
        row1 = st.columns(2)
        row2 = st.columns(2)

        rec_place = ['Lotte World Seoul', 'etc', 'etc', 'etc']
        rec_place_img = ['./img/예시/ltseoul.png', './img/예시/everland.jpeg', './img/예시/gjworld.jpeg', './img/예시/carrbay.jpeg']
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
        st.image(Image.open('./img/예시/wordcloud.png'),
                 use_column_width=True)
    with col2:
        st.markdown('**Top 20 Keywords**')
        st.text('(based on Korean blog reviews)')
        st.image(Image.open('./img/예시/graph.png'),
                 use_column_width=True)

# --------------------------(해운대해수욕장)-------------------------

with tab3:
    st.subheader('Haeundae Beach')
    st.link_button('Google Map', 'https://www.google.co.kr/maps/place/%ED%95%B4%EC%9A%B4%EB%8C%80%ED%95%B4%EC%88%98%EC%9A%95%EC%9E%A5/data=!3m1!4b1!4m6!3m5!1s0x35688d5c0efe075f:0x9963b1d5c163ac98!8m2!3d35.1586975!4d129.1603842!16s%2Fm%2F03bx6xl?hl=ko&entry=ttu')
    with st.container(height=130):
        st.markdown('''Haeundae Beach is the most famous beach 
        in Busan. The white sand beach is roughly 1.5 kilometers long, 
        over a 30- to 50-meter wide area, creating a beautiful coastline 
        before a shallow bay, making it perfect for swimming.''')
    st.divider()

    col1, col2 = st.columns([1,1])

    with col1:
        st.markdown('**Introduction**')
        st.image(Image.open('./img/예시/lotte.jpg'),
                 use_column_width=True)

    with col2:
        st.markdown('**Similar Destinations**')
        row1 = st.columns(2)
        row2 = st.columns(2)

        rec_place = ['Lotte World Seoul', 'etc', 'etc', 'etc']
        rec_place_img = ['./img/예시/ltseoul.png', './img/예시/everland.jpeg', './img/예시/gjworld.jpeg', './img/예시/carrbay.jpeg']
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
        st.image(Image.open('./img/예시/wordcloud.png'),
                 use_column_width=True)
    with col2:
        st.markdown('**Top 20 Keywords**')
        st.text('(based on Korean blog reviews)')
        st.image(Image.open('./img/예시/graph.png'),
                 use_column_width=True)


# --------------------------(다대포해수욕장)-------------------------

with tab4:
    st.subheader('Dadaepo Beach')
    st.link_button('Google Map', 'https://www.google.co.kr/maps/place/%ED%95%B4%EC%9A%B4%EB%8C%80%ED%95%B4%EC%88%98%EC%9A%95%EC%9E%A5/data=!3m1!4b1!4m6!3m5!1s0x35688d5c0efe075f:0x9963b1d5c163ac98!8m2!3d35.1586975!4d129.1603842!16s%2Fm%2F03bx6xl?hl=ko&entry=ttu')
    with st.container(height=200):
        st.markdown('''Dadaepo Beach features shallow water and a wide sand 
        beach suitable for children. Water activities can be enjoyed at 
        the beach such as paddleboarding, kiteboarding and more. More visitors 
        have been attracted after the addition of a coastal park and walking paths. 
        At the entrance of the beach, there is a grand plaza with a large-scale 
        musical floor fountain. Visitors can enjoy the fountain from late-April 
        to October.''')
    st.divider()

    col1, col2 = st.columns([1,1])

    with col1:
        st.markdown('**Introduction**')
        st.image(Image.open('./img/예시/lotte.jpg'),
                 use_column_width=True)

    with col2:
        st.markdown('**Similar Destinations**')
        row1 = st.columns(2)
        row2 = st.columns(2)

        rec_place = ['Lotte World Seoul', 'etc', 'etc', 'etc']
        rec_place_img = ['./img/예시/ltseoul.png', './img/예시/everland.jpeg', './img/예시/gjworld.jpeg', './img/예시/carrbay.jpeg']
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
        st.image(Image.open('./img/예시/wordcloud.png'),
                 use_column_width=True)
    with col2:
        st.markdown('**Top 20 Keywords**')
        st.text('(based on Korean blog reviews)')
        st.image(Image.open('./img/예시/graph.png'),
                 use_column_width=True)

# --------------------------(해운대 포장마차촌)-------------------------

with tab5:
    st.subheader('Haeundae Street food alley')
    st.link_button('Google Map', 'https://www.google.co.kr/maps/place/%ED%95%B4%EC%9A%B4%EB%8C%80%ED%95%B4%EC%88%98%EC%9A%95%EC%9E%A5/data=!3m1!4b1!4m6!3m5!1s0x35688d5c0efe075f:0x9963b1d5c163ac98!8m2!3d35.1586975!4d129.1603842!16s%2Fm%2F03bx6xl?hl=ko&entry=ttu')
    with st.container(height=190):
        st.markdown('''Bada Maeul Pojang Macha Chon, or Ocean City Street Food Alley, 
        is located behind Haeundae Beach and has been in operation for over 20 years. 
        The Ocean City Street Food Alley has over 40 street carts. It was especially 
        famous for its lobster dishes, which included a large steamed lobster and 
        lobster ramyeon, among other freshly caught seafood.''')
    st.divider()

    col1, col2 = st.columns([1,1])

    with col1:
        st.markdown('**Introduction**')
        st.image(Image.open('./img/예시/lotte.jpg'),
                 use_column_width=True)

    with col2:
        st.markdown('**Similar Destinations**')
        row1 = st.columns(2)
        row2 = st.columns(2)

        rec_place = ['Lotte World Seoul', 'etc', 'etc', 'etc']
        rec_place_img = ['./img/예시/ltseoul.png', './img/예시/everland.jpeg', './img/예시/gjworld.jpeg', './img/예시/carrbay.jpeg']
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
        st.image(Image.open('./img/예시/wordcloud.png'),
                 use_column_width=True)
    with col2:
        st.markdown('**Top 20 Keywords**')
        st.text('(based on Korean blog reviews)')
        st.image(Image.open('./img/예시/graph.png'),
                 use_column_width=True)