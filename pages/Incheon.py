import streamlit as st
from PIL import Image
import numpy as np # TEST
st.header('Incheon')
list = ['Wolmido Island', 'Incheon Chinatown', 'Incheon Grand Park', 'Wolmi Theme Park', 'Songwol-dong Fairy Tale Village ']
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

# -------------------------(dict)-----------------------------
dict = {
    '월미테마파크' : ['Wolmi Theme Park ', './img/수정/월미테마파크.jpeg', 'Wolmi Theme Park is located on Wolmido Island in Incheon. Spanning 13,200 square meters, it features various amusement rides including a ferris wheel, swing boat, and go-karts.'],
    '영종도' : ['Yeongjongdo Island', './img/수정/영종도.webp', 'Yeongjongdo Island, combined with Yongyudo and Sammokdo Islands through land reclamation work, connects to the mainland via Yeongjongdaegyo Bridge and is located 3 kilometers northwest of Yeonan Pier, Incheon.'],
    '인천차이나타운' : ['Incheon Chinatown','./img/수정/인천차이나타운.jpeg', "Incheon's Chinatown came into being with the opening of Incheon Port in 1883 and Incheon's designation as an extraterritoriality of the Ching dynasty in the following year."],
    '마시안해변' : ['Masian Beach', './img/수정/마시안해변.bmp',"Located in the vicinity of Incheon International Airport, Masian Beach is unique in that it offers visitors an opportunity to experience both wetland and a sandy beach at the same time. When the tide is low, visitors will be fascinated by the distinctive co-existence of endless black wetland and the ivory sandy beach."],
    '송월동동화마을' : ['Songwol-dong Fairy Tale Village ', './img/수정/송월동동화마을.jpeg', "Songwol-dong was named for its view of the moon between the pine forest. The opening of Incheon Port in 1883 led to the start of many foreigners coming into the area for settlement, and it turned into a rich village."],
    '소래산': ['Soraesan Mountain ','./img/수정/소래산.jpeg',"Soraesan Mountain, with an altitude of 299 meters, is situated between Siheung and Incheon. Its name 'Sorae' originates from the area's old name, reflecting its rich heritage. The scenic mountain features a forest park, badminton courts, basketball courts, futsal fields, and various other amenities."],
    '소래습지생태공원': ['Sorae Marsh Ecological Park','./img/수정/소래습지생태공원.jpeg',"Sorae Marsh Ecological Park is located on a vast plot of land in Incheon. The walking paths by the salt storage and the windmill are especially popular photo points. Many people visit in fall for the shimmering silver grass, said to appear in many colors depending on the lighting."],
    '강화도':['Ganghwado Island','./img/수정/월미도.jpeg'],
    '원인재':[,],
    '월미도':['Wolmido Island', './img/수정/월미도.jpeg' ,"Wolmido Island has very few historical records, despite being the location of a temporary palace, built in 1653 during the reign of King Hyojong. On weekends and holidays, people flock to Wolmido Island to enjoy coffee and fresh seafood at the cafes and restaurants overlooking the sea."],
    '을왕리해수욕장':[,]
        }

# --------------------------(월미도)-------------------------
#관광지명
name = list[0]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%9B%94%EB%AF%B8%EB%8F%84/data=!3m2!1e3!4b1!4m6!3m5!1s0x357b82632534876d:0x834d1ce34f129aca!8m2!3d37.4754003!4d126.5978148!16s%2Fm%2F0j7n6nc?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Wolmido Island has very few historical records, despite being the location of a temporary palace, built in 1653 during the reign of King Hyojong. The palace was built on the eastern side of the island, but it is impossible to find traces of it now. From the late 1920s until the '30s, the island was transformed into a resort, a very popular destination at the time. Wolmi Culture Street opened in July 1989 and helped improve the area's fame. On weekends and holidays, people flock to Wolmido Island to enjoy coffee and fresh seafood at the cafes and restaurants overlooking the sea. Despite being 1 kilometer off the coast, Wolmido is no longer an island, being connected to the mainland through modern construction techniques. It is now an easily accessible retreat for locals and tourists alike.'''
#추천 장소 4곳
rec_place = [dict['월미테마파크'][0], dict['영종도'][0], dict['인천차이나타운'][0], dict['마시안해변'][0]]
#추천 장소 이미지 경로 4개
rec_place_img = [dict['월미테마파크'][1], dict['영종도'][1], dict['인천차이나타운'][1], dict['마시안해변'][1]]
#추천 장소 설명 4개
rec_caption = [dict['월미테마파크'][2], dict['영종도'][2], dict['인천차이나타운'][2], dict['마시안해변'][2]]
# 관광지 Image
image1 = './img/수정/월미도.jpeg'
#Wordcloud
image2 = './img/인화/대릉원 워드클라우드.png'
#그래프
image3 = './img/예시/graph.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab1, name, googlelink, intro, image1, image2, image3)

# --------------------------(인천차이나타운)-------------------------
#관광지명
name = list[1]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%9D%B8%EC%B2%9C+%EC%B0%A8%EC%9D%B4%EB%82%98%ED%83%80%EC%9A%B4/data=!3m2!1e3!4b1!4m6!3m5!1s0x357b789af07d8fd7:0x97f43442e51633c9!8m2!3d37.475589!4d126.6178849!16s%2Fm%2F02rhs_v?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Incheon's Chinatown came into being with the opening of Incheon Port in 1883 and Incheon's designation as an extraterritoriality of the Ching dynasty in the following year. In the past, the area held many stores trading goods imported from China, but currently most Chinese businesses in the area are restaurants. Today, the residents of Chinatown are mostly 2nd or 3rd generation Chinese, descendents of the early Chinese settlers. The area harbors many of the flavors of China, while the traditional culture of the first generation is preserved.'''
#추천 장소 4곳
rec_place = [dict['송월동동화마을'][0], dict['월미도'][0], dict['월미테마파크'][0], dict['영종도'][0]]
#추천 장소 이미지 경로 4개
rec_place_img = [dict['송월동동화마을'][1], dict['월미도'][1], dict['월미테마파크'][1], dict['영종도'][1]]
#추천 장소 설명 4개
rec_caption = [dict['송월동동화마을'][2], dict['월미도'][2], dict['월미테마파크'][2], dict['영종도'][2]]
# 관광지 Image 1
image1 = './img/수정/롯데월드부산.jpg'
#Wordcloud Image 2
image2 = './img/인화/대릉원 워드클라우드.png'
#그래프 Image 3
image3 = './img/예시/graph.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab2, name, googlelink, intro, image1, image2, image3)

# --------------------------(인천대공원)-------------------------
#관광지명
name = list[2]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%9D%B8%EC%B2%9C%EB%8C%80%EA%B3%B5%EC%9B%90/data=!3m1!1e3!4m10!1m2!2m1!1z7J247LKc64yA6rO17JuQ!3m6!1s0x357b7c98d4dd7b0f:0x88d0d7acb8001d6e!8m2!3d37.459244!4d126.7522197!15sCg_snbjsspzrjIDqs7Xsm5BaEiIQ7J247LKcIOuMgOqzteybkJIBBHBhcmvgAQA!16s%2Fm%2F0nbhyl_?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Incheon Grand Park is an urban nature park located in Jangsu-dong, Namdong-gu, Incheon. The park is surrounded by Gwanmosan Mountain and Sangasan Mountain. Spanning across 727 acres of land, Incheon Grand Park is the only large-scale natural green park in Incheon. The park provides a pleasant atmosphere for citizens to escape from the city life and enjoy the natural surroundings. Over 4 million people visit the park every year to take in the clean air and relax in nature.'''
#추천 장소 4곳
rec_place = [dict['소래산'][0], dict['소래습지생태공원'][0], dict['강화도'][0], dict['원인재'][0]]
#추천 장소 이미지 경로 4개
rec_place_img = [dict['소래산'][1], dict['소래습지생태공원'][1], dict['강화도'][1], dict['원인재'][1]]
#추천 장소 설명 4개
rec_caption = [dict['소래산'][2], dict['소래습지생태공원'][2], dict['강화도'][2], dict['원인재'][2]]
# 관광지 Image 1
image1 = './img/수정/해운대해수욕장.jpeg'
#Wordcloud Image 2
image2 = './img/인화/대릉원 워드클라우드.png'
#그래프 Image 3
image3 = './img/예시/graph.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab3, name, googlelink, intro, image1, image2, image3)

# --------------------------(월미테마파크)-------------------------
#관광지명
name = list[3]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%9B%94%EB%AF%B8%ED%85%8C%EB%A7%88%ED%8C%8C%ED%81%AC/data=!3m2!1e3!4b1!4m6!3m5!1s0x357b82884e45dfff:0x5184d1be20d0fa05!8m2!3d37.4713635!4d126.5962858!16s%2Fg%2F1tk1ky1p?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Wolmi Theme Park is located on Wolmido Island in Incheon. Spanning 13,200 square meters, it features various amusement rides including a ferris wheel, swing boat, and go-karts. One of its highlights is the tagada ride, where riders sit on circular seats that move in all directions to the beat of music while a DJ adds to the excitement. Visitors can also enjoy panoramic views of Songdo Town, the Incheondaegyo Bridge, and Yeongjongdaegyo Bridge from the ferris wheel.'''
#추천 장소 4곳
rec_place = [dict['월미도'][0], dict['송월동동화마을'][0], dict['인천차이나타운'][0], dict['을왕리해수욕장'][0]]
#추천 장소 이미지 경로 4개
rec_place_img = [dict['월미도'][1], dict['송월동동화마을'][1], dict['인천차이나타운'][1], dict['을왕리해수욕장'][1]]
#추천 장소 설명 4개
rec_caption = [dict['월미도'][2], dict['송월동동화마을'][2], dict['인천차이나타운'][2], dict['을왕리해수욕장'][2]]
# 관광지 Image 1
image1 = './img/수정/다대포해수욕장.jpeg'
#Wordcloud Image 2
image2 = './img/인화/대릉원 워드클라우드.png'
#그래프 Image 3
image3 = './img/예시/graph.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab4, name, googlelink, intro, image1, image2, image3)

# --------------------------(송월동동화마을)-------------------------
#관광지명
name = list[4]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EA%B4%91%EC%95%88%EB%A6%AC%ED%95%B4%EC%88%98%EC%9A%95%EC%9E%A5/data=!3m2!1e3!4b1!4m6!3m5!1s0x3568ed2f27c70ec7:0xff6df0e14d9216fb!8m2!3d35.1531696!4d129.118666!16s%2Fm%2F03hp9yc?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Songwol-dong was named for its view of the moon between the pine forest. The opening of Incheon Port in 1883 led to the start of many foreigners coming into the area for settlement, and it turned into a rich village. However, young people gradually moved out, leaving the village in a state of stagnation. As such, a renovation project was brought about to improve the development of the village by decorating with murals and sculptures of classic fairy tales.'''
#추천 장소 4곳
rec_place = [dict['인천차이나타운'][0], dict['월미도'][0], dict['월미테마파크'][0], dict['영종도'][0]]
#추천 장소 이미지 경로 4개
rec_place_img = [dict['인천차이나타운'][1], dict['월미도'][1], dict['월미테마파크'][1], dict['영종도'][1]]
#추천 장소 설명 4개
rec_caption = [dict['인천차이나타운'][2], dict['월미도'][2], dict['월미테마파크'][2], dict['영종도'][2]]
# 관광지 Image 1
image1 = './img/수정/해운대포장마차촌.jpeg'
#Wordcloud Image 2
image2 = './img/인화/대릉원 워드클라우드.png'
#그래프 Image 3
image3 = './img/예시/graph.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab5, name, googlelink, intro, image1, image2, image3)