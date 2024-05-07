import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
st.header('Chungbuk')

list = ['Cheongnamdae',
        'Forest Resom Have Nine Spa',
        'Uirimji',
        'Chungju Lavarland',
        'Aquatic Plant Study Center']
tab1, tab2, tab3, tab4, tab5 = st.tabs(list)

def tabs(tabnum, name, googlelink, intro, image1, image2, data, pos, neg, image3):
    with (tabnum):
        st.subheader(name)
        # st.markdown('**Train: 3hrs 24 min / Bus: 5hrs 2 min** (departure from seoul)')
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
            st.image(image1,
                     use_column_width=True)

        with col2:
            st.markdown('**You may also like 😃**')
            row1 = st.columns(2)
            row2 = st.columns(2)
            for i, col in enumerate(row1 + row2):
                tile = col.expander(rec_place[i])
                tile.image(rec_place_img[i],
                     caption=rec_caption[i],
                     use_column_width=True)

        st.divider()

        col1, col2 = st.columns([1,1])

        with col1:
            st.markdown('💡**Highlights of the Destination**')
            st.text('(Top Keywords based on Korean blog)')
            st.image(image2,
                     use_column_width=True)
        with col2:
            data1 = pd.read_csv(data)
            data1[['Year', 'Month', 'Day']] = data1['날짜'].str.rstrip('.').str.split('.', expand=True)
            # 전체 데이터에서 모든 월을 추출
            all_months = data1['Month'].unique()

            # 'month' 리스트 생성
            month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                          'October', 'November', 'December']

            # 월 이름 리스트를 전체 월 중 있는 월만 남기도록 필터링
            filtered_month_list = [month_list[int(month) - 1] for month in all_months]
            # popular_month 만들기
            popular_month = pd.DataFrame(data1['Month'].value_counts().sort_index())
            popular_month['month'] = filtered_month_list

            # 후기수 가장 많은 달 1위 뽑기
            mon = popular_month.sort_values(by='count', ascending=False)['month'][0]
            st.markdown(f'**🗓️ Most Visited Month: :red[{mon}]**')

            st.text('(based on Korean reviews)')
            fig = px.pie(popular_month, values='count',
                         names='month', hover_data=['count'],
                         labels={'count': 'Count'},
                         width=400, height=400, hole=0.3)

            fig.update_traces(textinfo='percent+label', textfont_size=14, textposition='inside')
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig)

        st.divider()

        total_count = pos + neg
        st.markdown(f'🔍The reviews from korean visitors are generally like this (**{total_count} reviews**)')
        positive_ratio = (pos / total_count) * 100
        negative_ratio = (neg / total_count) * 100

        positive_icon = '😊'  # 긍정을 나타내는 이모티콘
        negative_icon = '😞'  # 부정을 나타내는 이모티콘

        positive_display = f'{positive_icon} {positive_ratio:.0f}%'
        negative_display = f'{negative_icon} {negative_ratio:.0f}%'

        st.subheader(f'**:green[{positive_display}]** **:red[{negative_display}]**')

        with st.expander('Review text positive/negative word distribution (Bigram NetworkX Graph)'):
            st.image(image3, use_column_width=True)

# --------------------------(청남대)-------------------------

#관광지명
name = list[0]
#관광지 구글 링크
googlelink = 'https://www.google.co.kr/maps/place/%EC%B2%AD%EB%82%A8%EB%8C%80/data=!3m1!4b1!4m6!3m5!1s0x35652533bd955661:0x8c872679c076ca7b!8m2!3d36.4618125!4d127.4891875!16s%2Fm%2F0nbd4d1?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
Cheongnamdae is located on the lake of Daecheong, meaning Cheongnamdae is the "warm South's Blue House," which has been used as an official villa for the President of the Republic of Korea since 1983. The total area is 1,844,000 square meters, and the main facilities include golf courses, shade houses, helicopter courses, fish farms, pentagonal fishing villages, and cho homes, and a total of five presidents used it 88 times before it opened, and it was opened to the public on April 18, 2003. More than 116,000 landscaping trees of 124 kinds and 350,000 wild flowers, which change their appearance according to the four seasons, are another pride of Cheongnamdae. The natural ecosystem is also well preserved, and natural monuments otters, flying squirrels, wild boars, elk, raccoons, and pheas live there, and it is also a place for various migratory birds. There is a "Stairway of Happiness" where you can take in the scenery at a glance in Cheongnamdae, and an observatory where you can bend the blue Daecheong Lake and Cheongnamdae as if you are playing fresh.
'''
#추천 장소 4곳
rec_place = ['Munji Cultural Heritage Complex',
             'Daecheong Dam Observatory',
             'Midongsan Arboretum',
             'Seongan-gil']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/종혁/충북/문의문화재단지.jpg',
                 './img/종혁/충북/대청댐 전망대.jpg',
                 './img/종혁/충북/미동산수목원.jpg',
                 './img/종혁/충북/성안길.jpg']
#추천 장소 설명 4개
rec_caption = ['Munmun Cultural Property was established to revive and learn the lives and spirits of our ancestors by recreating our own traditional culture, which is disappearing due to the development of human civilization and rapid industrialization.',
               'When you climb the observatory, you can see the clear Daecheong Lake, and when you enter the water promotion hall, there is a video facility that provides a clear view of water-related materials, dam construction, and various financial resources, serving as a water resource learning center.',
               'Mi Dongsan Arboretum is a provincial arboretum located in Cheongju-si, Chungcheongbuk-do, built for the purpose of R&D and distribution of advanced forestry technologies and the creation of ecological education environment',
               'Seongan-gil, located in the middle of the city center of Cheongju, is one of the busiest places in the country.']
# 관광지 Image
image1 = './img/종혁/충북/청남대.jpg'
#Wordcloud
image2 = './img/종혁/충북/청남대 워드클라우드.png'
#파이차트 경로
data = ('./data/충북/청남대.csv')
#Positive 개수
pos = 200
#Negative 개수
neg = 100
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/종혁/충북/청남대 그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab1, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(포레스트리솜 해브나인스파)-------------------------
#관광지명
name = list[1]
#관광지 구글 링크
googlelink = 'https://www.google.co.kr/maps/place/%ED%95%B4%EB%B8%8C%EB%82%98%EC%9D%B8+%EC%8A%A4%ED%8C%8C/data=!4m15!1m8!3m7!1s0x3563834f2630b737:0x894a4e51c835b440!2z7ZW067iM64KY7J24IOyKpO2MjA!8m2!3d37.1576958!4d128.0466289!10e1!16s%2Fg%2F11fmh3_mhp!3m5!1s0x3563834f2630b737:0x894a4e51c835b440!8m2!3d37.1576958!4d128.0466289!16s%2Fg%2F11fmh3_mhp?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
Forest Resom Have Nine Spa is located in Baegun-myeon, Jecheon-si, Chungcheongbuk-do. The Healing Spa Zone is equipped with facilities such as a Bade Pool, a water energy spa, and a filamentous spa where you can enjoy various water pressure massages depending on the area of the human body's meridians. The Aqua Play Zone is a play pool that guardians and children can enjoy together and consists of kids slides, running water pools, and beach pools. The outdoor spa zone has various facilities, including Infinity Pool, which you can enjoy outdoors while looking at the forest.
'''
#추천 장소 4곳
rec_place = ['Cheongju Hot Spring Spa',
             'Park Dal-jae Natural Recreation Forest',
             'Uirimji',
             'Jecheon Oksoonbong Suspension Bridge']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/종혁/충북/청주온천스파.jpg',
                 './img/종혁/충북/박달재자연휴양림.jpg',
                 './img/종혁/충북/의림지.jpg',
                 './img/종혁/충북/제천 옥순봉 출렁다리.jpg']
#추천 장소 설명 4개
rec_caption = ['Spa',
               'A dense forest where pine trees and miscellaneous trees coexist for about 150 years is in harmony with the strange rock formations.',
               'Uirimji is one of the representative repair facilities in Korea, and it is known that it has existed since the Three Han Period, although the date of its formation is not clear.',
               'It is a suspension bridge where you can feel Oksunbong Peak, one of the 10 scenic views of Jecheon, with your whole body on the surface of Cheongpung Lake']
# 관광지 Image
image1 = './img/종혁/충북/포레스트리솜 해브나인스파.jpg'
#Wordcloud
image2 = './img/종혁/충북/포레스트리솜 해브나인스파 워드클라우드.png'
#파이차트 경로
data = './data/충북/포레스트리솜 해브나인스파.csv'
#Positive 개수
pos = 200
#Negative 개수
neg = 100
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/종혁/충북/포레스트리솜 해브나인스파 그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab2, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(의림지)-------------------------
#관광지명
name = list[2]
#관광지 구글 링크
googlelink = 'https://www.google.co.kr/maps/place/%EC%9D%98%EB%A6%BC%EC%A7%80/data=!4m15!1m8!3m7!1s0x3563910aa82921cb:0x4d00e24664fe13c0!2z7J2Y66a87KeA!8m2!3d37.1732513!4d128.2104938!10e1!16s%2Fg%2F120l33yp!3m5!1s0x3563910aa82921cb:0x4d00e24664fe13c0!8m2!3d37.1732513!4d128.2104938!16s%2Fg%2F120l33yp?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
Uirimji is one of the representative repair facilities in Korea, and although the date of its construction is not clear, it is known to have existed since the Three Han Period. It is said that during the reign of King Jinheung of Silla, a malicious Ureuk blocked the stream and built a bank, and it is also said that Park Uirim, the prefectural governor who came here 700 years later, built a new one. There are records that Jeong In-ji came here as a inspector during the reign of the Joseon Dynasty and carried out large-scale construction by mobilizing 1,500 troops of the 3rd degree. It has a full area of 130,000 square meters and a maximum depth of 13.5 meters.
'''
#추천 장소 4곳
rec_place = ['Yongchu Falls Glass Observatory',
             'Biryongdam Reservoir',
             'Jecheon Oksoonbong Suspension Bridge',
             'Cheongpungho Tourist Monorail']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/종혁/충북/용추폭포 유리전망대.jpg',
                 './img/종혁/충북/비룡담저수지.jpg',
                 './img/종혁/충북/제천 옥순봉 출렁다리.jpg',
                 './img/종혁/충북/청풍호 관광모노레일.jpg']
#추천 장소 설명 4개
rec_caption = ['It is a place where you can walk while watching the cool water pouring under your feet, so you can relieve your stress by looking at the dizzying feeling of walking on a waterfall and the cool water pouring down.',
               'Jecheon Biryongdam Reservoir is also called the "magic castle" in the form of a secret castle surrounded by a forest.',
               'It is a suspension bridge where you can feel Oksunbong Peak, one of the 10 scenic views of Jecheon, with your whole body on the surface of Cheongpung Lake',
               'This modern monorail course, which takes 50 minutes round trip and has some steep sections, offers views of lakes, mountains, and forests.']
# 관광지 Image
image1 = './img/종혁/충북/의림지.jpg'
#Wordcloud
image2 = './img/종혁/충북/의림지 워드클라우드.png'
#파이차트 경로
data = './data/충북/의림지.csv'
#Positive 개수
pos = 200
#Negative 개수
neg = 100
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/종혁/충북/의림지 그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab3, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(충주라바랜드)-------------------------

#관광지명
name = list[3]
#관광지 구글 링크
googlelink = 'https://www.google.co.kr/maps/place/%EB%9D%BC%EB%B0%94%EB%9E%9C%EB%93%9C/data=!4m15!1m8!3m7!1s0x35648715130c9a4f:0x167567cf635b918!2z652867CU656c65Oc!8m2!3d36.9893295!4d127.9077341!10e1!16s%2Fg%2F11fmv_p0j2!3m5!1s0x35648715130c9a4f:0x167567cf635b918!8m2!3d36.9893295!4d127.9077341!16s%2Fg%2F11fmv_p0j2?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
Chungju Lavarland is the only complex kids cultural content in Korea where you can enjoy indoor kids' cafes and outdoor amusement parks installed in Chungju World Martial Arts Park at the same time. It is a children's theme park with pleasant and comical Akdong Lavar friends, and it is a place where the largest educational experience class in Korea, event performances, and various complex amusement facilities are combined.
'''
#추천 장소 4곳
rec_place = ['Glazed Cave',
             'Tangeumdae',
             'Chungju Dam Observatory',
             'The Seven-story Stone Pagoda in Tappyeong-ri, Chungchu']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/종혁/충북/충주 활옥동굴.jpg',
                 './img/종혁/충북/탄금대.jpg',
                 './img/종혁/충북/충주댐 전망대.jpg',
                 './img/종혁/충북/충주 탑평리 칠층석탑.jpeg']
#추천 장소 설명 4개
rec_caption = ['It is the only talc mine in Korea developed in Japanese colonial era in 1922, with a record of 57 km and an informal 87 km, and a vertical underground height of 711 m, the largest in the East.',
               'Tangeumdae is a hill originally called Daecheongsan Mountain, but it has a very good view with the Namhangang River and dense pine forests that flow smoothly around the rocky cliffs.',
               'Observatory',
               'It is believed to have been built during the Unified Silla Dynasty.']

# 관광지 Image
image1 = './img/종혁/충북/충주라바랜드.jpg'
#Wordcloud
image2 = './img/종혁/충북/충주라바랜드 워드클라우드.png'
#파이차트 경로
data = './data/충북/충주라바랜드.csv'
#Positive 개수
pos = 200
#Negative 개수
neg = 100
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/종혁/충북/충주라바랜드 그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab4, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(수생식물학습원)-------------------------

#관광지명
name = list[4]
#관광지 구글 링크
googlelink = 'https://www.google.co.kr/maps/place/%EC%88%98%EC%83%9D%EC%8B%9D%EB%AC%BC%ED%95%99%EC%8A%B5%EC%9B%90/data=!3m1!4b1!4m6!3m5!1s0x3565392d531fde9b:0xed86e885a2f518cc!8m2!3d36.3909665!4d127.5532312!16s%2Fg%2F1td6vztb?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
Aquatic Plant Learning Center – Celestial Garden is a private garden, located on top of a beautiful lake garden in the middle of Daecheong Lake, the third largest in Korea. 
Surrounded by modified sedimentary rocks, Lake Daecheong, and exotic buildings, the Celestial Garden is evaluated as the most beautiful lake garden in Korea. Celestial Garden was opened in 2009 as a natural science study site designated by the Chungcheongbuk-do Office of Education. 
Currently, it is operated as a private garden designated by the Chungcheongbuk-do Office of Education. 
Celestial Garden has been introduced to various media, boasting landscaping consisting of abundant flowers and plants throughout the year, as well as various aquatic plants and tropical plants living in Korea. 
Celestial Garden is a living site of natural ecology education and a place to experience the natural ecology conservation site with the whole body. Since its opening, it has been actively used as a space to provide not only students but also institutions and companies with natural experience education sites, as well as various programs that provide mental and physical rest and healing. 
In addition to various programs such as healing camps and concerts, it has been used as a filming site for various dramas with only the heavenly garden surrounding the lake and its special architecture. Recently, a forest road has been opened to embrace the lake, allowing you to see the heavenly garden surrounding the lake from the forest.
'''
#추천 장소 4곳
rec_place = ['Busodamak',
             'Jangnyeongsan Natural Recreation Forest',
             "Yuk Young-soo's birthplace",
             'Daecheong Dam Observatory']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/종혁/충북/부소담악.jpg',
                 './img/종혁/충북/장령산자연휴양림.jpg',
                 './img/종혁/충북/육영수 생가.jpg',
                 './img/종혁/충북/대청댐 전망대.jpg']
#추천 장소 설명 4개
rec_caption = ['It is a rocky cliff that rises above the water, and is 700m long.',
               'It is a famous mountain in Okcheon, which is famous for its beautiful natural scenery, and pine, maple, and cypress trees grow naturally.',
               'Hanok [Gyodongjip] in Gu-eup, Okcheon is the birthplace of First Lady Yuk Young-soo and the house where First Lady Yuk was born and raised.',
               'When you climb the observatory, you can see the clear Daecheong Lake, and when you enter the water promotion hall, there is a video facility that provides a clear view of water-related materials, dam construction, and various financial resources, serving as a water resource learning center.']
# 관광지 Image
image1 = './img/종혁/충북/수생식물학습원.jpg'
#Wordcloud
image2 = './img/종혁/충북/수생식물학습원 워드클라우드.png'
#파이차트 경로
data = './data/충북/수생식물학습원.csv'
#Positive 개수
pos = 200
#Negative 개수
neg = 100
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/종혁/충북/수생식물학습원 그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab5, name, googlelink, intro, image1, image2, data, pos, neg, image3)