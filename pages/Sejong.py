import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.header('Sejong')
list = ['Sejong National Arboretum', 'Dodori Park', 'Gobok Reservoir', 'Jochiwon Theme Street', 'Sejong Attige']
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


# -------------------------(dict)-----------------------------
dict1 = {
    '금강수목원':['Geumgang Recreational Forest', './img/수정/금강수목원.jpeg', "Geumgang Recreational Forest is different from other recreational forests. Rather than a dense forest with a trail, this forest has a variety of attractions such as the Forest Museum, an arboretum, greenhouse, pond, and wildlife park scattered on well-maintained roads, giving the impression of a city park."],
    '베어트리파크':['Beartree Park', './img/수정/베어트리파크.jpeg', "Beartree Park is a beautiful natural space in Sejong founded by entrepreneur Lee Jae-yeon. The park first started out as a private garden cared for by Lee personally."],
    '밀마루전망대':['Milmaru Tower', './img/수정/밀마루전망대.jpeg', "Located at the center of the Sejong Administrative Town, Milmaru Observatory is designed to provide a view of the city in every direction. You can see the ever-changing Sejong City at one glance as well as neighboring regions such as Gongju and Jochiwon."],
    '조치원테마거리':[list[3], './img/수정/조치원테마거리.jpeg', "Jochiwon Theme Street is a theme street created using the traditional market in Jochiwon-eup, Chungcheongnam-do. This is a place where you can feel the old atmosphere by reproducing the appearance of Jochiwon-eupseong Fortress during the Joseon Dynasty."],
    '조치원역광장':['Jochiwon Station Square', './img/수정/조치원역광장.jpeg', "Jochiwon Station, which resembles the Chinese character for a bird (bird), opened for business on January 1, 1905 as Botong Station on the Gyeongbu Line."],
    '국립세종수목원':[list[0], './img/수정/국립세종수목원.jpeg', "The Sejong National Arboretum, which is about to open as the first urban arboretum in Korea, was built on an area adjacent to the Sejong Government Complex. It is possible to see 2,834 species of 1.72 million plants (including 45,958 trees) under various themes such as the nation's largest four-season greenhouse, traditional Korean garden, Cheongryujiwon for study, and bonsai garden."],
    '고복자연공원':['Gobok Natural Park', './img/수정/고복자연공원.jpeg', "Gobok Natural Park spans an area of 1,840,000 square meters and nearby attractions include a forest, Yonggul Cave, Sinheungsa Temple, and an outdoor sculpture park on Obongsan Mountain."],
    '도담동먹자골목':['Dodam-dong Food Alley', './img/수정/도담동먹자골목.jpeg', "Dodam-dong Food Alley is one of the centers of the Dodam-dong commercial district. There is a wide range of delicious restaurants, from the 'Karim Avenue Hill Shopping Mall' backed by the Dodam-dong Fresh Market parking lot to the 'Shopping Mall in Doram Village Complex 7 and 8' to the 'Dodam-dong Food Alley' with Bangchukcheon in the background."],
    '비학산':['Bihaksan Mountain', './img/수정/비학산.jpeg', "Bihaksan Mountain, located in Geumnam-myeon, Sejong City, was named so because the mountain resembles a flying crane. The height of Bihaksan Mountain is 162.5m above sea level, and Ilchulbong Peak is also not very high at 228m, so it is a mountain that people of all ages and genders can easily go for a walk."],
    '조천변벛꽃길':['Jocheonside cherry blossom road', './img/수정/조천변벛꽃길.jpeg', "The cherry blossom road along Jocheon is a famous spot in Sejong City that many citizens visit every year. You can enjoy the beauty of spring by walking through the cherry blossom tunnel that stretches for several kilometers along the embankment."],
    '고복저수지':[list[2], './img/수정/고복저수지.jpeg', "Gobok Reservoir is located in the Gobok-ri and Yongam-ri areas of Yeonseo-myeon, Sejong Special Self-Governing City. There are restaurants and cafes specializing in duck meat dishes and catfish spicy stew scattered around the reservoir, and many tourists come to enjoy them on weekends."],
    '세종미니멀주':['Sejong Minimal Zoo', './img/수정/세종미니멀주.jpeg', "Sejong Minimal Zoo is an urban zoo where you can see, hear and interact with animals."],
    '세종공룡월드':['Sejong Dinosaur World', './img/수정/세종공룡월드.jpeg', 'Sejong Dinosaur World offers dinosaurs from the Jurassic period. Enjoy a realistic walking dinosaur show and a magic show at Asan Dinosaur World with 500 seats at a reasonable price.']
}

# --------------------------(국립세종수목원)-------------------------
#관광지명
name = list[0]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EA%B5%AD%EB%A6%BD%EC%84%B8%EC%A2%85%EC%88%98%EB%AA%A9%EC%9B%90/data=!3m2!1e3!4b1!4m6!3m5!1s0x357acb4a4c989b5b:0x892194666573b3e9!8m2!3d36.4978379!4d127.2854901!16s%2Fg%2F155q41_z?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''The Sejong National Arboretum, which is about to open as the first urban arboretum in Korea, was built on an area of 65 ha adjacent to the Sejong Government Complex, where several government ministries are located. It is possible to see 2,834 species of 1.72 million plants (including 45,958 trees) under various themes such as the nation's largest four-season greenhouse, traditional Korean garden, Cheongryujiwon for study, and bonsai garden. It is another national arboretum established following the Baekdudaegan National Arboretum following the National Arboretum Expansion Plan for conserving and developing genetic tree resources by climate and vegetation zone.'''
#추천 장소 4곳
rec_place = [dict1['금강수목원'][0], dict1['베어트리파크'][0], dict1['밀마루전망대'][0], dict1['조치원테마거리'][0]]
#추천 장소 이미지 경로 4개
rec_place_img = [dict1['금강수목원'][1], dict1['베어트리파크'][1], dict1['밀마루전망대'][1], dict1['조치원테마거리'][1]]
#추천 장소 설명 4개
rec_caption = [dict1['금강수목원'][2], dict1['베어트리파크'][2], dict1['밀마루전망대'][2], dict1['조치원테마거리'][2]]
# 관광지 Image
image1 = dict1['국립세종수목원'][1]
#Wordcloud
image2 = 'img/수정/세종/국립세종수목원 워드클라우드.png'
#파이차트 경로
data = 'data/세종/국립세종수목원.csv'
#Positive 개수
pos = 172
#Negative 개수
neg = 65
#Bigram NetworkX Graph 이미지 첨부
image3 = 'img/수정/세종/국립세종수목원그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab1, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(도도리파크)-------------------------
#관광지명
name = list[1]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EB%8F%84%EB%8F%84%EB%A6%AC%ED%8C%8C%ED%81%AC/data=!3m2!1e3!4b1!4m6!3m5!1s0x357ad314052ee56f:0x357da527de9363d0!8m2!3d36.5975243!4d127.2869857!16s%2Fg%2F11s8_xc035?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Dodori Park, a rural theme park, is a space for citizens to recognize the value and importance of rural resources and to continuously conserve and promote them. Within Dodori Park, there is a fresh market (farmer's market) to provide safe food to citizens and a place where people can experience various things using local agricultural products. In addition, there are play spaces such as the indoor Dodori Tower and the outdoor Dodori Adventure and Maze Park, so anyone can come and enjoy.'''
#추천 장소 4곳
rec_place = [dict1['조치원테마거리'][0], dict1['금강수목원'][0], dict1['조치원역광장'][0], dict1['국립세종수목원'][0]]
#추천 장소 이미지 경로 4개
rec_place_img = [dict1['조치원테마거리'][1], dict1['금강수목원'][1], dict1['조치원역광장'][1], dict1['국립세종수목원'][1]]
#추천 장소 설명 4개
rec_caption = [dict1['조치원테마거리'][2], dict1['금강수목원'][2], dict1['조치원역광장'][2], dict1['국립세종수목원'][2]]
# 관광지 Image 1
image1 = 'img/수정/도도리파크.jpeg'
#Wordcloud Image 2
image2 = 'img/수정/세종/도도리파크 워드클라우드.png'
#파이차트 경로
data = 'data/세종/도도리파크.csv'
#Positive 개수
pos = 6
#Negative 개수
neg = 1
#Bigram NetworkX Graph 이미지 첨부
image3 = 'img/수정/세종/도도리파크그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab2, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(고복저수지)-------------------------
#관광지명
name = list[2]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EA%B3%A0%EB%B3%B5%EC%A0%80%EC%88%98%EC%A7%80/data=!3m2!1e3!4b1!4m6!3m5!1s0x357acdf2be5de3e9:0xf1494528e7291562!8m2!3d36.602851!4d127.231805!16s%2Fg%2F119pfnw_h?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''If you leave Yeonhwasa Temple and go to Gobok-ri, Yeonseo-myeon, you will come across Gobok Reservoir with a large area of 1.949㎢ (1.142㎢ in Gobok-ri, 0.807㎢ in Yongam-ri). There is 'Minrakjeong' in the middle of Gobok Reservoir. If you climb up the pavilion and look out over the reservoir, the view is also spectacular. Around Gobok Reservoir, there are restaurants specializing in herbal duck and spicy catfish soup to whet the appetite of gourmets. The surrounding village has an orchard complex growing grapes, peaches, and pears, as well as commercial facilities, lodging facilities, and various public facilities.'''
#추천 장소 4곳
rec_place = [dict1['고복자연공원'][0], dict1['금강수목원'][0], dict1['도담동먹자골목'][0], dict1['비학산'][0]]
#추천 장소 이미지 경로 4개
rec_place_img = [dict1['고복자연공원'][1], dict1['금강수목원'][1], dict1['도담동먹자골목'][1], dict1['비학산'][1]]
#추천 장소 설명 4개
rec_caption = [dict1['고복자연공원'][2], dict1['금강수목원'][2], dict1['도담동먹자골목'][2], dict1['비학산'][2]]
# 관광지 Image 1
image1 = dict1['고복저수지'][1]
#Wordcloud Image 2
image2 = 'img/수정/세종/고복저수지 워드클라우드.png'
#파이차트 경로
data = 'data/세종/고복저수지.csv'
#Positive 개수
pos = 16
#Negative 개수
neg = 2
#Bigram NetworkX Graph 이미지 첨부
image3 = 'img/수정/세종/고복저수지그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab3, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(조치원테마거리)-------------------------
#관광지명
name = list[3]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%A1%B0%EC%B9%98%EC%9B%90+%ED%85%8C%EB%A7%88%EA%B1%B0%EB%A6%AC/data=!3m2!1e3!4b1!4m6!3m5!1s0x35652d384eb92f2f:0x2b9666daae1edbd1!8m2!3d36.6007996!4d127.3009819!16s%2Fg%2F11s8gj75kj?hl=ko&entry=ttu'
#관광지 소개 글
intro = dict1['조치원테마거리'][2]
#추천 장소 4곳
rec_place = [dict1['조치원역광장'][0], dict1['조천변벛꽃길'][0], dict1['베어트리파크'][0], dict1['고복저수지'][0]]
#추천 장소 이미지 경로 4개
rec_place_img = [dict1['조치원역광장'][1], dict1['조천변벛꽃길'][1], dict1['베어트리파크'][1], dict1['고복저수지'][1]]
#추천 장소 설명 4개
rec_caption = [dict1['조치원역광장'][2], dict1['조천변벛꽃길'][2], dict1['베어트리파크'][2], dict1['고복저수지'][2]]
# 관광지 Image 1
image1 = dict1['조치원테마거리'][1]
#Wordcloud Image 2
image2 = 'img/수정/세종/조치원테마거리 워드클라우드.png'
#파이차트 경로
data = 'data/세종/조치원테마거리.csv'
#Positive 개수
pos = 1
#Negative 개수
neg = 1
#Bigram NetworkX Graph 이미지 첨부
image3 = 'img/수정/세종/조치원테마거리그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab4, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(아띠쥬)-------------------------
#관광지명
name = list[4]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EB%AF%B8%EB%8B%88%EB%A9%80%EC%A3%BC+%EC%84%B8%EC%A2%85%EC%A0%90/data=!3m1!1e3!4m10!1m2!2m1!1z7IS47KKFIOyVhOudoOyjvA!3m6!1s0x357acb1bd5ce725b:0x394f4ca02156bcb!8m2!3d36.4739818!4d127.2748139!15sChDshLjsooUg7JWE652g7KO8kgEDem9v4AEA!16s%2Fg%2F11kj25lxxj?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Sejong Attige, located on the 7th floor of the Happy Raum Blue building in Daepyeong-dong, Sejong City, is a small indoor zoo where you can see animals up close and experience feeding them. At the entrance, there is a sculpture of a cute panda bear family, so children have fun taking pictures.'''
#추천 장소 4곳
rec_place = [dict1['세종미니멀주'][0], dict1['베어트리파크'][0], dict1['금강수목원'][0], dict1['세종공룡월드'][0]]
#추천 장소 이미지 경로 4개
rec_place_img = [dict1['세종미니멀주'][1], dict1['베어트리파크'][1], dict1['금강수목원'][1], dict1['세종공룡월드'][1]]
#추천 장소 설명 4개
rec_caption = [dict1['세종미니멀주'][2], dict1['베어트리파크'][2], dict1['금강수목원'][2], dict1['세종공룡월드'][2]]
# 관광지 Image 1
image1 = 'img/수정/아띠쥬.jpeg'
#Wordcloud Image 2
image2 = 'img/수정/세종/아띠쥬 워드클라우드.png'
#파이차트 경로
data = 'data/세종/아띠쥬.csv'
#Positive 개수
pos = 10
#Negative 개수
neg = 3
#Bigram NetworkX Graph 이미지 첨부
image3 = 'img/수정/세종/아띠쥬그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab5, name, googlelink, intro, image1, image2, data, pos, neg, image3)
