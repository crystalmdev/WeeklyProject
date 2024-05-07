import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
st.header('Chunggnam')

list = ['Gongju Hanok Village',
        'Gongsanseong Fortress',
        'House of Yu Gibang',
        'Cheongsan Arboretum',
        'Onyang Hot Spring Land']
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

# --------------------------(공주한옥마을)-------------------------

#관광지명
name = list[0]
#관광지 구글 링크
googlelink = 'https://www.google.co.kr/maps/place/%EA%B3%B5%EC%A3%BC%ED%95%9C%EC%98%A5%EB%A7%88%EC%9D%84/data=!3m1!4b1!4m9!3m8!1s0x357ab9ddf39bce55:0x50e0b021c18d18a8!5m2!4m1!1i2!8m2!3d36.464451!4d127.1088459!16s%2Fg%2F1tg4trlb?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
Gongju Hanok Village is located between the Gongju Songsan-ri Tomb and the Gongju National Museum. 
The traditional kuddle-jang exudes the old atmosphere of hanok, and the card key system for safety and prevention of theft provides comfort. 
Individual lodging buildings are made up of independent houses, and group lodging buildings are equipped with a separate locker room and shower room. 
There are various experience programs where you can learn about Baekje history, including experiencing Baekje costumes, experiencing Baekje tea ceremony, making Gongju albam tea ceremony, and making Baekje artifacts.'''
#추천 장소 4곳
rec_place = ['Royal Tomb of King Muryeong',
             'Gongsanseong Fortress',
             'Gyeryongsan Mountain',
             'Daecheon Beach']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/종혁/충남/무령왕릉.jpg',
                 './img/종혁/충남/공산성.jpg',
                 './img/종혁/충남/계룡산.jpg',
                 './img/종혁/충남/대천해수욕장.jpg']
#추천 장소 설명 4개
rec_caption = ['It is an ancient 6th-century royal tomb known for its impressive design and treasures such as golden crowns.',
               'Located in the middle of a mountain overlooking the river and downtown Gongju, it is a centuries-old Baekje-era fortress.',
               'A trail runs between the famous ridges and the waterfalls and rock zones of the national park.',
               'The mud festival is held every year, and the sanded beach is 3.5km long and there are many shops selling snacks.']
# 관광지 Image
image1 = './img/종혁/충남/공주한옥마을.jpg'
#Wordcloud
image2 = './img/종혁/충남/공주한옥마을 워드클라우드.png'
#파이차트 경로
data = './data/충남/공주한옥마을.csv'
#Positive 개수
pos = 200
#Negative 개수
neg = 100
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/종혁/충남/공주한옥마을 그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab1, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(공산성)-------------------------
#관광지명
name = list[1]
#관광지 구글 링크
googlelink = 'https://www.google.co.kr/maps/place/%EA%B3%B5%EC%82%B0%EC%84%B1/data=!3m1!4b1!4m6!3m5!1s0x357ab77f03639b27:0xf0d79de6719009f8!8m2!3d36.4630408!4d127.1266933!16s%2Fg%2F1210gqw9?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Gongsanseong Fortress is a representative fortress of the Baekje period, and it is a fortress of Baekje that protected Gongju when the capital of Baekje was Gongju. 
It was a Baekje capital city until the capital was moved to Buyeo in the 16th year of the Baekje Kingdom (538), and it was the center of local administration until the Joseon Dynasty, and is an important historical site.'''
#추천 장소 4곳
rec_place = ['Royal Tomb of King Muryeong',
             'Gongju Hanok Village',
             'Gyeryongsan Mountain',
             'Baekje Cultural Complex']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/종혁/충남/무령왕릉.jpg',
                 './img/종혁/충남/공주한옥마을.jpg',
                 './img/종혁/충남/계룡산.jpg',
                 './img/종혁/충남/백제문화단지.jpg']
#추천 장소 설명 4개
rec_caption = ['It is an ancient 6th-century royal tomb known for its impressive design and treasures such as golden crowns.',
               'Gongju Hanok Village is located between the Gongju Songsan-ri Tomb and the Gongju National Museum. ',
               'A trail runs between the famous ridges and the waterfalls and rock zones of the national park.',
               'It is a historical park that shows life during the Baekje period, and its castles, towers, and temples have been rebuilt.']
# 관광지 Image
image1 = './img/종혁/충남/공산성.jpg'
#Wordcloud
image2 = './img/종혁/충남/공산성 워드클라우드.png'
#파이차트 경로
data = './data/충남/공산성.csv'
#Positive 개수
pos = 200
#Negative 개수
neg = 100
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/종혁/충남/공산성 그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab2, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(유기방가옥)-------------------------
#관광지명
name = list[2]
#관광지 구글 링크
googlelink = 'https://www.google.co.kr/maps/place/%EC%84%9C%EC%82%B0+%EC%9C%A0%EA%B8%B0%EB%B0%A9+%EA%B0%80%EC%98%A5/data=!3m1!4b1!4m6!3m5!1s0x357a584ecce297b9:0x1608499e8d79e734!8m2!3d36.824701!4d126.573446!16s%2Fg%2F11g691tvq5?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
It was built in the early 1900s and has an area of 4,770㎡. 
It is a house during the Japanese colonial period and was evaluated as valuable local historical and architectural data, and was designated as a Chungcheongnam-do Folk Cultural Property on October 31, 2005. 
The Yoo Ki-bang House is located facing south against the background of a low hill with forested areas. To the north, a -shaped main house and a hangout house on the west side, and a recently built house form a courtyard. 
Originally, in 1988, the central gate house in front of the main house was demolished, and a pavilion-type main gate house was built as it is now.
'''
#추천 장소 4곳
rec_place = ['Haemi Town Wall',
             'Maaeyeorae Triad',
             'Yonghyeon National Recreation Forest',
             'Beolcheonpo Beach']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/종혁/충남/해미읍성.jpg',
                 './img/종혁/충남/무령왕릉.jpg',
                 './img/종혁/충남/국립용현자연휴양림.jpg',
                 './img/종혁/충남/벌천포해수욕장.jpg']
#추천 장소 설명 4개
rec_caption = ['Built in 1491, it is a stone fortress of the Joseon Dynasty and is a sacred place for Korean Catholics.',
               "Also called Seosan Maae Samjonbul, it is a cultural asset and art work that allows you to feel what Baekje's smile is like, carved on a rock around the 7th century, the late Baekje period.",
               'In the recreational forest, where the valley water is clear and clean, and oak trees are dense, there are accommodation facilities such as forest culture and recreation centers, campgrounds, and forest classes.',
               'The surroundings are quiet and the natural scenery is beautiful, so many people spend their vacations enjoying camping in the pine field every summer.']
# 관광지 Image
image1 = './img/종혁/충남/유기방가옥.jpg'
#Wordcloud
image2 = './img/종혁/충남/유기방가옥 워드클라우드.png'
#파이차트 경로
data = './data/충남/유기방가옥.csv'
#Positive 개수
pos = 200
#Negative 개수
neg = 100
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/종혁/충남/유기방가옥 그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab3, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(청산 수목원)-------------------------

#관광지명
name = list[3]
#관광지 구글 링크
googlelink = 'https://www.google.co.kr/maps/place/%EC%B2%AD%EC%82%B0%EC%88%98%EB%AA%A9%EC%9B%90/data=!4m15!1m8!3m7!1s0x357a6cfc85975205:0x3555dca28b4bc669!2z7LKt7IKw7IiY66qp7JuQ!8m2!3d36.6882641!4d126.2970322!10e1!16s%2Fg%2F1td4bg62!3m5!1s0x357a6cfc85975205:0x3555dca28b4bc669!8m2!3d36.6882641!4d126.2970322!16s%2Fg%2F1td4bg62?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
Located in Taean-gun, Chungcheongnam-do, Cheongsan Arboretum is decorated with an aquatic botanical garden that combines more than 200 wetland plants such as lotus, water lilies and Changpo, a theme garden where you can meet the background and characters in artists' works such as Millet, Goch, and Monet, a walking trail that creates various appearances according to the season, and an arboretum where 600 kinds of trees, including golden metasequoias, are nesting. It has been built since 1990 and has the largest number of lotus varieties in Korea, with a variety of aquatic plants, trees, and wild flowers. Especially in summer, you can appreciate the elegant appearance of the lotus. The entrance closes one hour before sunset, so it is recommended to check it out before visiting.
'''
#추천 장소 4곳
rec_place = ['Mallipo Beach',
             'Cheonripo Arboretum',
             'Mongsanpo Beach',
             'Paduri Beach']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/종혁/충남/만리포해수욕장.jpg',
                 './img/종혁/충남/천리포수목원.jpg',
                 './img/종혁/충남/몽산포해수욕장.jpg',
                 './img/종혁/충남/파도리해수욕장.jpg']
#추천 장소 설명 4개
rec_caption = ['It has a large sandy beach, so you can enjoy swimming and sunbathing, and you can rent parasols and use nearby restaurants.',
               'As an arboretum next to the sea, there are not only native plants but also exotic plants such as magnolia and colorful maple trees.',
               'It is a famous 3km-long sand beach where you can experience the mudflats, with a pine forest and a camping site behind it.',
               'There is a line of rugged black seashore rocks next to the white sand beach, and the beach is covered with small and pretty hailstones.']

# 관광지 Image
image1 = './img/종혁/충남/청산 수목원.jpg'
#Wordcloud
image2 = './img/종혁/충남/청산 수목원 워드클라우드.png'
#파이차트 경로
data = './data/충남/청산 수목원.csv'
#Positive 개수
pos = 200
#Negative 개수
neg = 100
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/종혁/충남/청산 수목원 그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab4, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(온양온천랜드)-------------------------

#관광지명
name = list[4]
#관광지 구글 링크
googlelink = 'https://www.google.co.kr/maps/place/%EC%98%A8%EC%96%91%EC%98%A8%EC%B2%9C%EB%9E%9C%EB%93%9C/data=!3m1!4b1!4m6!3m5!1s0x357ade950237d2ef:0x34627a37b3524060!8m2!3d36.7811968!4d127.0158216!16s%2Fg%2F1hc4r7_4l?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
Onyang Hot Spring Land is a comprehensive hot spring water park located in Asan. Onyang Hot Spring is the oldest hot spring in Korea, and it is recorded that its history is about 1,300 years old through the Baekje and Unified Silla periods. During the Joseon Dynasty, not only King Sejong but also many kings, including King Sejo, Sukjong, Yeongjo, and Jeongjo, stayed there for recreation or treatment. Onyang Hot Spring Land has a hot spring bath (sauna), a jjimjilbang, a children's hot spring (kids' water park), and a fitness center, so anyone of all ages can enjoy Onyang hot spring water. Here, natural alkali hot spring water (PH 8.42) is supplied to the entire business site in the facility without any processing. Onyang Hot Spring is a traditional hot spring attraction that boasts the best water quality in Korea, and it is also a good place to rest and heal with various auxiliary facilities.
'''
#추천 장소 4곳
rec_place = ['Onyang Hot Spring',
             'Asan Spavis',
             'Mediterranean Village',
             'Paradise Spa Dogo']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/종혁/충남/온양온천.jpg',
                 './img/종혁/충남/아산스파비스.jpg',
                 './img/종혁/충남/지중해마을.jpg',
                 './img/종혁/충남/파라다이스스파도고.jpg']
#추천 장소 설명 4개
rec_caption = ['The original bath of Onyang Hot Spring is a bathhouse called Sincheon bath located around the market, and the foot bath is located at the entrance of Onyang Traditional Market and below the bridge of Onyang Hot Spring Station.',
               "Unlike existing simple hot spring facilities, it is a new concept themed hot spring using Korea's first hot spring water, and there are hydrated bed pool, kids pool for children, and outdoor hot spring pool that can be used for all seasons.",
               'The Mediterranean Village is a place reminiscent of a small rural village in the Mediterranean Sea, where exotic European-style buildings gather.',
               'Paradise Spa DOGO, designated as a health hot spring, is a large recreational facility opened by Paradise Group in Asan, Chungcheongnam-do, the home of hot springs.']
# 관광지 Image
image1 = './img/종혁/충남/온양온천랜드.jpg'
#Wordcloud
image2 = './img/종혁/충남/온양온천랜드 워드클라우드.png'
#파이차트 경로
data = './data/충남/온양온천랜드.csv'
#Positive 개수
pos = 200
#Negative 개수
neg = 100
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/종혁/충남/온양온천랜드 그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab5, name, googlelink, intro, image1, image2, data, pos, neg, image3)