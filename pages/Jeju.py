import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.header('Jeju Island🍊')
list = ['Snoopy Garden', 'Hamdeok Beach', 'Camellia Hill', 'Seongsan Sunrise Peak', 'Camellia Forest']
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

# --------------------------(스누피가든)-------------------------

#관광지명
name = list[0]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%8A%A4%EB%88%84%ED%94%BC%EA%B0%80%EB%93%A0/data=!3m2!1e3!4b1!4m6!3m5!1s0x350d1bc32bdef82d:0x35c7b3cf574c06f5!8m2!3d33.4441972!4d126.7783058!16s%2Fg%2F11k0sd47kl?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
        Snoopy Garden House is a place where you can meet honest and unique Peanuts friends and receive messages of sympathy and comfort through their mutual relationships.
        Garden House's Theme Hall is a space where you can connect your daily life with the theme of 'Peanuts, Nature & Life' and the daily stories contained in Peanuts episodes.
        Walk, look, eat, and rest in the five themed halls, Cafe Snoopy, and Peanuts Store, and send messages of relaxation and comfort to your current self through Peanuts characters.
        Garden House Outdoor Garden
        The outdoor garden is a place where you can experience Peanuts episodes in nature, learn the meaning of life, and find comfort through relaxation in nature.
        Peanuts friends find the meaning of life and grow by experiencing the natural environment and seasonal changes such as snow, rain, wind, and fallen leaves.
        Experience the pure value of Jeju’s nature and various episodes of Peanuts at each theme garden.
        '''
#추천 장소 4곳
rec_place = ['Seongsan Sunrise Peak', 'Sanbangsan Mountain', 'Yongduam Rock', 'Seopjikoji']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/인화/성산일출봉.jpg', './img/인화/산방산.jpg', './img/인화/용두암.jpg', './img/인화/섭지코지.jpg']
#추천 장소 설명 4개
rec_caption = ['Seongsan Ilchulbong, unlike other volcanic cones on Jeju Island, is a water-based volcano formed when magma erupts from under the water.',
                'As you drive through the southwestern part of Jeju, you can see Sanbangsan Mountain, a landmark in Sagye-ri, Andeok-myeon, which boasts the grandeur of a huge sculpture.',
                'It was named Yongduam after the shape of a dragon rising from the sea in a roar.',
                'Seopjikoji, which juts out on the eastern coast of Jeju, has spectacular coastal scenery with Seongsan Ilchulbong in the background.']
# 관광지 Image
image1 = './img/인화/스누피가든.jpg'
#Wordcloud
image2 = './img/인화/스누피가든 워드클라우드.png'
#파이차트 경로
data = 'data/제주/스누피가든.csv'
#Positive 개수
pos_cnt = 735
#Negative 개수
neg_cnt = 386
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/인화/스누피가든그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab1, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)
# --------------------------(함덕해수욕장)-------------------------
#관광지명
name = list[1]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%ED%95%A8%EB%8D%95%ED%95%B4%EC%88%98%EC%9A%95%EC%9E%A5/data=!3m2!1e3!4b1!4m6!3m5!1s0x350cfcafaaf72b55:0xf0d2596ca578b870!8m2!3d33.5434231!4d126.6697752!16s%2Fg%2F1hdzn_dcy?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
        If you walk along Jeju Olle Course 19, you can come across Hamdeok Beach, which has emerald jewels. Hamdeok Beach, located in Hamdeok-ri, Jocheon-eup, Jeju-si, is also called ‘Hamdeok Seoubong Beach’ thanks to the tall volcano (Seoubong Peak) that stands right next to the beach.
        Although it is only 20km away from Jeju Airport, the moment you arrive here, you feel like you have arrived in another country. The tall palm trees that welcome you from the entrance, the emerald sea contrasting with the white sand, and the clear water and white waves that transparently reflect even the sand and seaweed.
        Among the numerous beaches on Jeju Island, the three beaches with the prettiest sea colors are definitely Hyeopjae, Gimnyeong, and Hamdeok Beach. The water is clear and shallow, making it a good summer resort for families. The west side of the beach is connected by a cloud bridge, allowing you to experience the experience of walking on the sea.
        The lawn, which is great for picnics, and the walking trail where you can enjoy the sea safely at night are attractive, so there is a constant flow of visitors all year round. Especially in summer, it is open at night, so you can enjoy Jeju’s blue nights at the sea.
        Seoubong Peak, located right next to it, presents picturesque scenery every season with yellow rape flowers in spring and green in summer. If you climb Seoubong Peak, you can enjoy the luxury of a panoramic view of Hamdeok Beach. If the weather is good, it is the best observation point from which you can overlook Hallasan Mountain and the eastern oreums.
        '''
#추천 장소 4곳
rec_place = ['Hyeopjae Beach', 'Gimnyeong Beach', 'Geumneung Beach', 'Gwakji Beach']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/인화/협재해수욕장.jpg', './img/인화/김녕해수욕장.jpg', './img/인화/금능해수욕장.jpg', './img/인화/곽지해수욕장.jpg']
#추천 장소 설명 4개
rec_caption = ['If you were asked to choose a beach worth visiting on the west side of Jeju Island, Hyeopjae Beach would be ranked first and second.',
                'It was made of sand piled on top of a huge rock called lava, and Seongsegi is meant to be a small castle to prevent invasion by foreign powers.',
                'Clear water that shows through the bottom, shallow water with the sea water lapping at you, and even a hot shower to enjoy after playing in the water. If you are looking for a beach with the best conditions for visiting with children, Geumneung Beach is the perfect place.',
                'Gwakji Beach is a beach with good conditions, including a 350m long, 70m wide white sand beach, an average water depth of 1.5m, and a slope of 5 to 8 degrees.']
# 관광지 Image 1
image1 = './img/인화/함덕해수욕장.jpg'
#Wordcloud Image 2
image2 = './img/인화/함덕해수욕장 워드클라우드.png'
#파이차트 경로
data = 'data/제주/함덕해수욕장.csv'
#Positive 개수
pos_cnt = 271
#Negative 개수
neg_cnt = 86
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/인화/함덕해수욕장그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab2, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# --------------------------(카멜리아힐)-------------------------
#관광지명
name = list[2]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%B9%B4%EB%A9%9C%EB%A6%AC%EC%95%84+%ED%9E%90/data=!3m2!1e3!4b1!4m6!3m5!1s0x350c5b755d81da01:0xea6d4e1147bdb92f!8m2!3d33.2898049!4d126.3682983!16s%2Fg%2F1tff5c77?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
         Camellia Hill is the largest camellia arboretum in the East, where you can see over 500 varieties of camellia flowers from over 80 countries, including native camellias, baby camellias, and European camellias.
        There are many cute photo spots in the arboretum, so it is especially popular among tourists with couples and families. During the season when camellia flowers bloom, there is a constant stream of people coming to take wonderful photos with the camellia flowers in full bloom as a background.
        Where are there only camellia flowers? When summer begins, hydrangea flowers resembling the blue sky greet visitors, and in fall, silver grass and pink muhly fill the fall garden. Thanks to the new changes of clothes each season, it boasts a 100% success rate for taking the perfect shot no matter what time of day you visit.
        Not only the Bird Song Wind Sound Road, which is known as the background of the Innisfree CF, but also the traditional Olle Road with Jeju's stone walls and the emotional forest path with twinkling yellow light bulbs are also must-take photo points. There are so many photo spots in every nook and cranny that you will lose track of time as you take pictures here and there.
        A walk around Camellia Hill takes approximately 40 minutes to 1 hour and 20 minutes. We recommend that you allow plenty of time to visit.
        '''
#추천 장소 4곳
rec_place = ['Jeju Camellia Arboretum', 'Camellia Forest', 'Jeju Herb Garden', 'Sanbangsan Mountain']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/인화/제주동백수목원.jpg', './img/인화/동백포레스트.jpg', './img/인화/제주허브동산.jpg', './img/인화/산방산.jpg']
#추천 장소 설명 4개
rec_caption = ['Jeju Camellia Arboretum gives you a feeling of the tropics with camellias that are green throughout the year, unknown birds chirping each season, and citrus orchards full of abundance.',
                'There are beautifully blooming camellia flowers, a stone wall surrounding the colony, and chairs arranged around the trees, making it a great place to take pictures.',
                'There is a place where you can enjoy your Jeju trip with fragrant herbal scents during the day and twinkling lights at night.',
                'As you drive through the southwestern part of Jeju, you can see Sanbangsan Mountain, a landmark in Sagye-ri, Andeok-myeon, which boasts the grandeur of a huge sculpture.',
               ]
# 관광지 Image 1
image1 = './img/인화/카멜리아힐.jpg'
#Wordcloud Image 2
image2 = './img/인화/카멜리아힐 워드클라우드.png'
#파이차트 경로
data = 'data/제주/카멜리아힐.csv'
#Positive 개수
pos_cnt = 412
#Negative 개수
neg_cnt = 237
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/인화/카멜리아힐그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab3, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)


# --------------------------(성산일출봉)-------------------------

#관광지명
name = list[3]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%84%B1%EC%82%B0+%EC%9D%BC%EC%B6%9C%EB%B4%89/data=!3m2!1e3!4b1!4m6!3m5!1s0x350d14b9f6e3789f:0x555132053a23b64b!8m2!3d33.458056!4d126.9425!16s%2Fm%2F0hhq99g?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
        Seongsan Ilchulbong, unlike other volcanic cones on Jeju Island, is a water-based volcano formed when magma erupts from under the water. As the hot magma ejected during volcanic activity meets cold seawater, the volcanic ash retains a lot of moisture and becomes sticky, and this piles up in layers to form Seongsan Ilchulbong.
        The sedimentary layers near the sea were eroded by waves and currents, creating the steep slopes they have today. When it was created, it was an island separate from the mainland of Jeju. As sand and gravel piled up around it, a road was created that connected it to the mainland at low tide. In 1940, a road was built here, and it is now perfectly connected to the mainland.
        When you climb to the top, you can see a crater with a width of about 80,000 pyeong, which is concave like a bowl and has grass such as silver grass growing inside. There are 99 high peaks (rocks) surrounding the crater. It was named ‘Seongsan (城山)’ because it looks like a huge castle, and ‘Ilchulbong (日出峰)’ because the view of the sun rising is spectacular.
        According to legend, if Seongsan Ilchulbong had 100 buds, wild beasts like tigers and lions would have appeared in Jeju as well, but since one is not enough, the number is 99, so neither tigers nor lions would appear.
        '''
#추천 장소 4곳
rec_place = ['Seopjikoji','Sanbangsan Mountain','Yongduam Rock','Cheonjiyeon Waterfall']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/인화/섭지코지.jpg', './img/인화/산방산.jpg', './img/인화/용두암.jpg', './img/인화/천지연폭포.jpg']
#추천 장소 설명 4개
rec_caption = ['Seopjikoji, which juts out on the eastern coast of Jeju, has spectacular coastal scenery with Seongsan Ilchulbong in the background.',
                'As you drive through the southwestern part of Jeju, you can see Sanbangsan Mountain, a landmark in Sagye-ri, Andeok-myeon, which boasts the grandeur of a huge sculpture.',
                'It was named Yongduam after the shape of a dragon rising from the sea in a roar.',
                'Cheonjiyeon means a pond where heaven and earth meet. The length of the waterfall is 22m and the depth of the pond below is 20m, so it is truly called the pond where heaven and earth meet.']
# 관광지 Image 1
image1 = './img/인화/성산일출봉.jpg'
#Wordcloud Image 2
image2 = './img/인화/성산일출봉 워드클라우드.png'
#파이차트 경로
data = 'data/제주/성산일출봉.csv'
#Positive 개수
pos_cnt = 218
#Negative 개수
neg_cnt = 131
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/인화/성산일출봉그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab4, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)
# --------------------------(동백포레스트)-------------------------
#관광지명
name = list[4]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EB%8F%99%EB%B0%B1+%ED%8F%AC%EB%A0%88%EC%8A%A4%ED%8A%B8/data=!3m2!1e3!4b1!4m6!3m5!1s0x350dabfea4595ea5:0xcd0c8274abe3e311!8m2!3d33.3001071!4d126.6364877!16s%2Fg%2F11h1tp3hc1?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
        ‘Camellia Forest’ in Silrye-ri, Namwon-eup is a camellia colony with round baby camellia trees planted.
        There are beautifully blooming camellia flowers, a stone wall surrounding the colony, and chairs arranged around the trees, making it a great place to take pictures.
        If you go up the trail built around the camellia tree, you can see the entire view of the camellia colony. Please note that the camellia flowers here are in full bloom and reach their peak between late December and January.
        Jeju Island is famous for seeing different flowers in each season: rapeseed flowers in spring, hydrangeas in summer, pink muhly in fall, and camellias in winter. The admission fee is not expensive, so it is a great place to stop by.
        '''
#추천 장소 4곳
rec_place = ['Jeju Camellia Arboretum','Namwon Keuneong Coast ','Saryeoni-Supgil','Camellia Hill']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/인화/제주동백수목원.jpg', './img/인화/남원큰엉해변.jpg', './img/인화/사려니숲길.jpg', './img/인화/카멜리아힐.jpg']
#추천 장소 설명 4개
rec_caption = ['Jeju Camellia Arboretum gives you a feeling of the tropics with camellias that are green throughout the year, unknown birds chirping each season, and citrus orchards full of abundance.',
                'Eong means ‘hill’ in the Jeju Island dialect. Namwon Keuneong is so named because it is a hill with a large rock with its mouth wide open as if swallowing the sea. The top of the cliff is flat and covered with soft grass.',
                'Saryeoni Forest Trail is one of Jeju\'s 31 hidden scenic spots. It is a forest path filled with cedar trees that starts from Bijarim-ro and passes through Mulchat Oreum and Saryeoni Oreum.',
                'Camellia Hill is the largest camellia arboretum in the East, where you can see over 500 varieties of camellia flowers.']
# 관광지 Image 1
image1 = './img/인화/동백포레스트.jpg'
#Wordcloud Image 2
image2 = './img/인화/동백포레스트 워드클라우드.png'
#파이차트 경로
data = 'data/제주/동백포레스트.csv'
#Positive 개수
pos_cnt = 138
#Negative 개수
neg_cnt = 66
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/인화/동백포레스트그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab5, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)