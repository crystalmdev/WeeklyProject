import streamlit as st
from PIL import Image
import numpy as np # TEST
st.header('Sejong')
list = ['Sejong National Arboretum', '도도리파크', '고복저수지', '조치원테마거리', '아띠쥬']
tab1, tab2, tab3, tab4, tab5 = st.tabs(list)

def tabs(tabnum, name, googlelink, intro, image1, image2, image3):
    with (tabnum):
        st.subheader(name)
        col1, col2, col3, col4 = st.columns([1.5,1.3,1,1])
        with col1:
            st.markdown('**How To Get There:**')
        with col2:
            st.page_link(googlelink, label='Google Map', icon='🗺️')
        with col3:
            st.page_link('https://www.letskorail.com/ebizbf/EbizbfForeign_pr16100.do?gubun=1',
                         label='Train', icon='🚃')
        with col4:
            st.page_link('https://www.kobus.co.kr/main.do',
                         label='bus', icon='🚌')

        # st.markdown('**Introduction**')
        with st.container(height=200):
            st.markdown(intro)
        st.divider()

        col1, col2 = st.columns([1,1])

        with col1:
            st.markdown('**Image**')
            st.image(Image.open(image1),
                     use_column_width=True)

        with col2:
            st.markdown('**You may also like 😃**')
            row1 = st.columns(2)
            row2 = st.columns(2)
            for i, col in enumerate(row1 + row2):
                tile = col.expander(rec_place[i])
                tile.image(Image.open(rec_place_img[i]),
                     caption=rec_caption[i],
                     use_column_width=True)

        st.divider()

        col1, col2 = st.columns([1,1])

        with col1:
            st.markdown('**Top Keywords about the Destination**')
            st.text('(based on Korean blog reviews)')
            st.image(Image.open(image2),
                     use_column_width=True)
        with col2:
            st.markdown('**스타차트로 변경**')
            st.text('(based on Korean blog reviews)')
            st.image(Image.open(image3),
                     use_column_width=True)

# --------------------------(국립세종수목원)-------------------------
#관광지명
name = list[0]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EA%B4%91%EC%95%88%EB%A6%AC%ED%95%B4%EC%88%98%EC%9A%95%EC%9E%A5/data=!3m2!1e3!4b1!4m6!3m5!1s0x3568ed2f27c70ec7:0xff6df0e14d9216fb!8m2!3d35.1531696!4d129.118666!16s%2Fm%2F03hp9yc?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''The Sejong National Arboretum, which is about to open as the first urban arboretum in Korea, was built on an area of ​​65 ha adjacent to the Sejong Government Complex, where several government ministries are located. It is possible to see 2,834 species of 1.72 million plants (including 45,958 trees) under various themes such as the nation's largest four-season greenhouse, traditional Korean garden, Cheongryujiwon for study, and bonsai garden. It is another national arboretum established following the Baekdudaegan National Arboretum following the National Arboretum Expansion Plan for conserving and developing genetic tree resources by climate and vegetation zone.'''
#추천 장소 4곳
rec_place = ['금강수목원', '베어트리파크', '밀마루전망대', '금강자연휴양림']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/예시/ltseoul.png', './img/예시/everland.jpeg', './img/예시/gjworld.jpeg', './img/예시/carrbay.jpeg']
#추천 장소 설명 4개
rec_caption = ['theme park located in seoul... etc 기타 간단한 영어 설명 - 번역기 돌려도 됨', 'theme park located in seoul... etc',
               'theme park located in seoul... etc', 'theme park located in seoul... etc']
# 관광지 Image
image1 = './img/수정/광안리해수욕장.jpeg'
#Wordcloud
image2 = './img/인화/대릉원 워드클라우드.png'
#그래프
image3 = './img/예시/graph.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab1, name, googlelink, intro, image1, image2, image3)

# --------------------------(도도리파크)-------------------------
#관광지명
name = list[1]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EA%B4%91%EC%95%88%EB%A6%AC%ED%95%B4%EC%88%98%EC%9A%95%EC%9E%A5/data=!3m2!1e3!4b1!4m6!3m5!1s0x3568ed2f27c70ec7:0xff6df0e14d9216fb!8m2!3d35.1531696!4d129.118666!16s%2Fm%2F03hp9yc?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Lotte World Adventure opened in Busan, where visitors can experience fun and exciting performances and parades. Busan Lotte World is built in Busan and has convenient access using public transportation, leading to many visitors since the first day of its opening. Lotte World Adventure Busan consists of six themed zones. At the heart of the fairy village, Tinker Falls Zone, is the Talking Tree, which uses animatronic technology to tell the story of six themes in the park. Rory Castle in the Royal Garden Zone, located at the highest point in Lotte World, is designed to look like it is floating on water, and visitors can enjoy the view of Busan and the sea in front of Gijang at a glance. Other rides, especially the Giant Digger and Giant Splash, have already received word-of-mouth excitement. As such, there are not only attractions for adults, but also amusement rides for families with young children. It is placed indoors so that children can safely enjoy it regardless of the weather. The parade, the highlight of the amusement park, runs twice a day for about 30 minutes.'''
#추천 장소 4곳
rec_place = ['조치원 테마거리', '금강수목원', '조치원역광장', '국립세종수목원 민속식물원']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/예시/ltseoul.png', './img/예시/everland.jpeg', './img/예시/gjworld.jpeg', './img/예시/carrbay.jpeg']
#추천 장소 설명 4개
rec_caption = ['theme park located in seoul... etc 기타 간단한 영어 설명 - 번역기 돌려도 됨', 'theme park located in seoul... etc',
               'theme park located in seoul... etc', 'theme park located in seoul... etc']
# 관광지 Image 1
image1 = './img/수정/롯데월드부산.jpg'
#Wordcloud Image 2
image2 = './img/인화/대릉원 워드클라우드.png'
#그래프 Image 3
image3 = './img/예시/graph.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab2, name, googlelink, intro, image1, image2, image3)

# --------------------------(고복저수지)-------------------------
#관광지명
name = list[2]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EA%B4%91%EC%95%88%EB%A6%AC%ED%95%B4%EC%88%98%EC%9A%95%EC%9E%A5/data=!3m2!1e3!4b1!4m6!3m5!1s0x3568ed2f27c70ec7:0xff6df0e14d9216fb!8m2!3d35.1531696!4d129.118666!16s%2Fm%2F03hp9yc?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Haeundae Beach is the most famous beach in Busan. The white sand beach is roughly 1.5 kilometers long, over a 30- to 50-meter wide area, creating a beautiful coastline before a shallow bay, making it perfect for swimming. People flock to Haeundae Beach every summer. All kinds of accommodations from luxury hotels to private guesthouses have developed in the area around the beach, making this the perfect summer vacation spot. Haeundae Beach is also famous for various cultural events and festivals held throughout the year. Other facilities in the area include Dongbaekseom Island, Busan Aquarium, a yachting dock, BEXCO, driving courses and more.'''
#추천 장소 4곳
rec_place = ['고복자연공원', '금강수목원', '도담동먹자골목', '비학산']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/예시/ltseoul.png', './img/예시/everland.jpeg', './img/예시/gjworld.jpeg', './img/예시/carrbay.jpeg']
#추천 장소 설명 4개
rec_caption = ['theme park located in seoul... etc 기타 간단한 영어 설명 - 번역기 돌려도 됨', 'theme park located in seoul... etc',
               'theme park located in seoul... etc', 'theme park located in seoul... etc']
# 관광지 Image 1
image1 = './img/수정/해운대해수욕장.jpeg'
#Wordcloud Image 2
image2 = './img/인화/대릉원 워드클라우드.png'
#그래프 Image 3
image3 = './img/예시/graph.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab3, name, googlelink, intro, image1, image2, image3)

# --------------------------(조치원테마거리)-------------------------
#관광지명
name = list[3]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EA%B4%91%EC%95%88%EB%A6%AC%ED%95%B4%EC%88%98%EC%9A%95%EC%9E%A5/data=!3m2!1e3!4b1!4m6!3m5!1s0x3568ed2f27c70ec7:0xff6df0e14d9216fb!8m2!3d35.1531696!4d129.118666!16s%2Fm%2F03hp9yc?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Dadaepo Beach is made from sands deposited by the Nakdonggang River. It features shallow water and a wide sand beach suitable for children. Water activities can be enjoyed at the beach such as paddleboarding, kiteboarding and more. More visitors have been attracted after the addition of a coastal park and walking paths. At the entrance of the beach, there is a grand plaza with a large-scale musical floor fountain. Visitors can enjoy the musical fountain from late-April to October.'''
#추천 장소 4곳
rec_place = ['조치원역광장', '조천변벛꽃길', '베어트리파크', '고복저수지']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/예시/ltseoul.png', './img/예시/everland.jpeg', './img/예시/gjworld.jpeg', './img/예시/carrbay.jpeg']
#추천 장소 설명 4개
rec_caption = ['theme park located in seoul... etc 기타 간단한 영어 설명 - 번역기 돌려도 됨', 'theme park located in seoul... etc',
               'theme park located in seoul... etc', 'theme park located in seoul... etc']
# 관광지 Image 1
image1 = './img/수정/다대포해수욕장.jpeg'
#Wordcloud Image 2
image2 = './img/인화/대릉원 워드클라우드.png'
#그래프 Image 3
image3 = './img/예시/graph.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab4, name, googlelink, intro, image1, image2, image3)

# --------------------------(아띠쥬)-------------------------
#관광지명
name = list[4]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EA%B4%91%EC%95%88%EB%A6%AC%ED%95%B4%EC%88%98%EC%9A%95%EC%9E%A5/data=!3m2!1e3!4b1!4m6!3m5!1s0x3568ed2f27c70ec7:0xff6df0e14d9216fb!8m2!3d35.1531696!4d129.118666!16s%2Fm%2F03hp9yc?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Bada Maeul Pojang Macha Chon, or Ocean City Street Food Alley, is located behind Haeundae Beach and has been in operation for over 20 years. The Ocean City Street Food Alley has over 40 street carts. It was especially famous for its lobster dishes, which included a large steamed lobster and lobster ramyeon, among other freshly caught seafood.'''
#추천 장소 4곳
rec_place = ['미니멀주 세종점', '베어트리파크', '금강수목원', '세종공룡월드']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/예시/ltseoul.png', './img/예시/everland.jpeg', './img/예시/gjworld.jpeg', './img/예시/carrbay.jpeg']
#추천 장소 설명 4개
rec_caption = ['theme park located in seoul... etc 기타 간단한 영어 설명 - 번역기 돌려도 됨', 'theme park located in seoul... etc',
               'theme park located in seoul... etc', 'theme park located in seoul... etc']
# 관광지 Image 1
image1 = './img/수정/해운대포장마차촌.jpeg'
#Wordcloud Image 2
image2 = './img/인화/대릉원 워드클라우드.png'
#그래프 Image 3
image3 = './img/예시/graph.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab5, name, googlelink, intro, image1, image2, image3)