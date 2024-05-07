import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
st.header('Gangwon️')
list = ['Anmok Beach🏖️', 'Nami Island🌳', 'Ojukheon House🏡', 'Sokcho Eye🎡', 'Haslla Art World🎨']
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

# 안목해변------------------------------------------------------------------------------------------

#관광지명
name = list[0]
#관광지 구글 링크
googlelink = 'https://www.google.co.kr/maps/place/%EC%95%88%EB%AA%A9%ED%95%B4%EB%B3%80/data=!3m1!4b1!4m6!3m5!1s0x3561e702c82e633d:0x850a8296837b2d4c!8m2!3d37.7731576!4d128.9472722!16s%2Fg%2F11c6_twdv5?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Nestled in Gangneung, Gangwon Province, Anmok Beach is a serene getaway 
        spanning 500 meters with over 20,000 square meters of pristine **white sands**, 
        perfect for families seeking **relaxation**. Alongside the beach sits Anmok Port, 
        where spring brings seaweed harvests and summer yields flatfish, rockfish (flounder), 
        squid, octopus, Manila clams (cockles), while autumn and winter offer Alaska pollack, 
        snow crabs, and flounder, all brought in by 23 fishing boats returning at 9 a.m. 
        As August draws to a close, the spectacle of mackerel chasing anchovies toward the shore 
        unfolds, sometimes prompting locals to gather these anchovy schools with buckets and nets. 
        Recently, the area has also gained renown as a **charming coffee street**, inviting visitors 
        to savor a variety of coffee delights.'''
#추천 장소 4곳
rec_place = ['Gangneung Coffee Street', 'Gyeongpo Beach', 'Sageunjin Beach', 'Gangmun Beach']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/다율/커피거리.png',
                 './img/다율/경포해수욕장.jpg',
                 './img/다율/사근진해수욕장.png',
                 './img/다율/강문해변.jpg']
#추천 장소 설명 4개
rec_caption = ['Enjoy coffee with a beautiful beach view.',
               'A place of beauty where lush pine forests meet the beach in harmony.',
               'A cozy beach shaded by lush pine forests.',
               'A pet-friendly beach where you can run along the white sandy shore.']
# 관광지 Image
image1 = './img/다율/안목해변.png'
#Wordcloud
image2 = './img/다율/안목해변 워드클라우드.png'
#파이차트 경로
data = './data/강원/안목해변.csv'
#Positive 개수
pos_cnt = 12
#Negative 개수
neg_cnt= 3
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/다율/안목해변그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab1, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# 남이섬-----------------------------------------------------------------------------------------------
#관광지명
name = list[1]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EB%82%A8%EC%9D%B4%EC%84%AC/data=!3m2!1e3!4b1!4m6!3m5!1s0x356326e41560af75:0xd64aaaa329e7c522!8m2!3d37.7899352!4d127.5258072!16s%2Fm%2F04f41_n?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Nami Island, with the concept of “Fairy Tale Village and Song Village,” provides various 
        cultural events, concerts, exhibitions, and more to give children dreams and hopes, couples' 
        love and memories, and artists a space for creativity. Tourists can enjoy facilities including 
        Song Museum, Picture Book Playground, MICE Center, and various activities such as Charity Train, 
        Story Tour Bus, Bicycle, etc. Restaurants provide delicious food with carefully selected local 
        ingredients and Hotel Jeonggwanru has themed accommodations.'''
#추천 장소 4곳
rec_place = ['Myeongdong Dakgalbi Street', 'Soyanggang Skywalk', 'Jade Garden', 'Alpaca World']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/다율/명동닭갈비골목.jpg',
                 './img/다율/소양강스카이워크.jpg',
                 './img/다율/제이드가든.jpg',
                 './img/다율/알파카월드.jpg']
#추천 장소 설명 4개
rec_caption = ["The representative Dakgalbi alley in Chuncheon.",
               'A skywalk with thrilling heights and stunning multicolored lighting.',
               'A small piece of Europe in the midst of the forest, boasting a botanical garden.',
               'Cute animals beside more cute animals.']
# 관광지 Image
image1 = './img/다율/남이섬2.jpg'
#Wordcloud
image2 = './img/다율/남이섬 워드클라우드.png'
#파이차트 경로
data = 'data/강원/남이섬.csv'
#Positive 개수
pos_cnt = 13
#Negative 개수
neg_cnt = 17
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/다율/남이섬그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab2, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# 오죽헌-----------------------------------------------------------------------------------------------
#관광지명
name = list[2]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%98%A4%EC%A3%BD%ED%97%8C/data=!3m1!1e3!4m6!3m5!1s0x3561e5b962230f29:0x8e262b2b0fff29!8m2!3d37.7791837!4d128.8794575!16s%2Fg%2F1220__3q?hl=ko&entry=ttu'
#관광지 소개
intro = '''Ojukheon House was where Yi I (penname Yulgok; scholar and politician of the Joseon Period) 
        was born. It was built during the early Joseon dynasty and was designated as a Treasure in 1963 
        for its historical value.Inside the house is Mongryongsil, where Yi I was born. The household 
        complex also features the household shrine, Munseongsa, the sarangchae (men's quarters), Eojaegak 
        Pavilion, Yulgok Memorial Hall, and Gangneung Municipal Museum. Since 1961, the city of Gangneung 
        has held a memorial ceremony at Yulgok Memorial Hall from October 25 to 26.
'''
#추천 장소 4곳
rec_place = ['Seongyojang House', 'Songjeong Beach', 'Jumunjin Breakwater', 'Jeongdongsimgok Badabuchae Trail']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/다율/선교장.jpeg',
                 './img/다율/송정해변.jpg',
                 './img/다율/주문진방파제.jpg',
                 './img/다율/정동심곡.jpg']
#추천 장소 설명 4개
rec_caption = ['Dignified houses with a 300-year-old tradition.',
               'A beautiful beach with silver-white sands stretching wide along the expansive sea.',
               "The Jumunjin Breakwater, famous as a filming location for the drama 'Goblin'",
               "Cheongdongjin Trail, Preserving Nature's Splendor"]
# 관광지 Image
image1 = './img/다율/오죽헌.jpg'
#Wordcloud
image2 = './img/다율/오죽헌 워드클라우드.png'
#파이차트 경로
data = 'data/강원/오죽헌.csv'
#Positive 개수
pos_cnt = 6
#Negative 개수
neg_cnt = 3
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/다율/오죽헌그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab3, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# 속초아이 -------------------------------------------------------------------------------

#관광지명
name = list[3]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%86%8D%EC%B4%88%EC%95%84%EC%9D%B4+%EB%8C%80%EA%B4%80%EB%9E%8C%EC%B0%A8/data=!3m1!4b1!4m6!3m5!1s0x5fd8bb97b967bf4b:0xb29d52c8d7ebb0f9!8m2!3d38.1907881!4d128.6027924!16s%2Fg%2F11rv6gct68?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Sokcho Eye is the only observation wheel located on a beach in South Korea, offering a 
        panoramic view of Sokcho's blue sea and the breathtaking scenery of Seoraksan Mountain. 
        Standing at a height of 22 floors, the Sokcho Eye consists of 36 cabins, each accommodating 
        up to 6 passengers, allowing a maximum of 216 people to enjoy the ride simultaneously.
'''
#추천 장소 4곳
rec_place = ['Yeonggeumjeong ', 'Yeongnangho Lake', 'Oeongchi Badahyanggiro Trail', 'Cheoksan Spatel ']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/다율/영금정.jpeg',
                 './img/다율/영랑호.jpg',
                 './img/다율/외옹치.jpg',
                 './img/다율/척산온천.jpg']
#추천 장소 설명 4개
rec_caption = ['Beach views from pavilion at end of cliff bridge',
               'Scenic lake with stunning views',
               'Enjoying the beachside path with light and dynamic activities',
               'A place to unwind from travel fatigue and also take care of your health']
# 관광지 Image
image1 = './img/다율/속초아이.jpg'
#Wordcloud
image2 = './img/다율/속초아이 워드클라우드.png'
#파이차트 경로
data = 'data/강원/속초아이.csv'
#Positive 개수
pos_cnt = 59
#Negative 개수
neg_cnt = 28
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/다율/속초아이그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab4, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# 하슬라아트월드-------------------------------------------------------------------------------

#관광지명
name = list[4]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%ED%95%98%EC%8A%AC%EB%9D%BC%EC%95%84%ED%8A%B8%EC%9B%94%EB%93%9C/data=!3m1!4b1!4m6!3m5!1s0x3561c32bbfa6a49b:0x566b6373d0ad039d!8m2!3d37.7061609!4d129.0116549!16s%2Fg%2F1td518gp?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Haslla Art World is an art space that harmonizes nature, people and art. The Sculpture Garden,
        approximately 27 acres in size, offers various themed gardens and structures. Contemporary 
        Gallery has approximately 200 contemporary artworks, while Pinocchio & Marionette Gallery has 
        various artworks from all over Europe. Haslla Art World has exhibitions and performances 
        throughout the year, providing visitors with a special experience every time they visit.'''
#추천 장소 4곳
rec_place = ['Jeongdongjin Beach', 'Mangsang Beach', 'Samcheok Beach', 'Sokcho Beach']
#추천 장소 이미지 경로 4개정동진해변
rec_place_img = ['./img/다율/정동진.jpg',
                 './img/다율/망상해변.jpg',
                 './img/다율/삼척해변.jpg',
                 './img/다율/속초해수욕장.png']
#추천 장소 설명 4개
rec_caption = ['The beach with the closest makeshift station to the sea in the world.',
               'A pristine white sandy beach and azure blue waters.',
               'A great place with expansive sandy beaches and lush pine forests.',
               'Sokcho Beach, beloved by vacationers.']
# 관광지 Image
image1 = './img/다율/하슬라.jpg'
#Wordcloud
image2 = './img/다율/하슬라아트월드 워드클라우드.png'
#파이차트 경로
data = 'data/강원/하슬라아트월드.csv'
#Positive 개수
pos_cnt = 43
#Negative 개수
neg_cnt = 19
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/다율/하슬라아트월드그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab5, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)