import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.header('Gyeongbuk')
list = ['Woljeonggyo Bridge', 'Hwangridan Street','Daereungwon', 'Cheomseongdae', 'Yeongildae Beach']
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

# --------------------------(월정교)-------------------------

#관광지명
name = list[0]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EA%B2%BD%EC%A3%BC+%EC%9B%94%EC%A0%95%EA%B5%90/data=!3m2!1e3!4b1!4m6!3m5!1s0x35664e601588af23:0xcd02c996ebde671b!8m2!3d35.8291928!4d129.2180462!16s%2Fg%2F11bv6q29jj?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''The name Jeongjeong is recorded in Samguk Sagi (History of the Three Kingdoms) in the 19th year of King Gyeongdeok’s reign of Unified Silla: 
        “The palace will be located in Wolcheon, with two parts, Woljeong Bridge and Chunyang Bridge.”
        After 10 years of collaborative investigation, historical research, and restoration of what was lost and disappeared during the Joseon Dynasty, 
        all restoration was completed in April 2018. In 2013, the bridge was selected for restoration, and the gate tower (motor gate) of the bridge was built separately.
        On the second floor of the gate tower, there is an exhibition hall where you can view videos of the bridge's restoration process and excavated artifacts.
        We can see the entirety of Woljeong Bridge during the day, and Woljeong Bridge at night tempts us with another charm.
        The person on the other side of Woljeong Bridge is the person looking at Woljeong Bridge. You can capture Woljeong Bridge shining softly over the river.'''
#추천 장소 4곳
rec_place = ['Donggung Palace and Wolji Pond', 'Cheonmachong', 'Bomun Tourist Complex', 'Bomunjeong']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/인화/dongpalace.jpg', './img/인화/cheonma.jpg', './img/인화/bomun.jpg', './img/인화/bomunjeong.jpg']
#추천 장소 설명 4개
rec_caption = ['Announcement time: 09:00 - 22:00 (ticket date 21:30), short break\
                        Fee: Adults 3,000 won / 2,000 won / Children 1,000 won',
                       'Operating hours 09:00-22:00 \
                       Admission fee: Adults 3,000 / Soldiers, Youth 2,000 / Children 1,000',
                       'Bomun Tourist Complex has leisure and tourist facilities scattered across a large area,\
                        so it is recommended to travel by car or bicycle. \
                        The public transportation infrastructure is good, so traveling by bus is not a problem.',
                       'Bomunjeong boasts such beautiful scenery that it was once introduced as ‘Korea’s Secret Place’ on CNN.\
                       Cherry trees and maple trees are planted around the octagonal pavilion and two ponds, \
                       making it a place to enjoy the scenery in any season.']
# 관광지 Image
image1 = './img/인화/woljeong_bridge.jpg'
#Wordcloud
image2 = './img/인화/월정교 워드클라우드.png'
#파이차트 경로
data = 'data/경북/월정교.csv'

# 예시 데이터
pos_cnt = 136
neg_cnt = 43

# #Positive 개수
# pos = 136
# #Negative 개수
# neg = 43

#Bigram NetworkX Graph 이미지 첨부
image3 = './img/인화/월정교그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab1, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)
#
# --------------------------(황리단길)-------------------------
#관광지명
name = list[1]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EB%8C%80%EB%A6%89%EC%9B%90/data=!3m2!1e3!4b1!4m6!3m5!1s0x35664e43390d70d7:0xcc0024d3d633ca05!8m2!3d35.8383029!4d129.2128614!16s%2Fg%2F1q66rsykf?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
        Hwangridan-gil is the youngest road in Gyeongju. It refers to the area around Hwangnam-dong and Sajeong-dong on both sides of the road starting from Naenam Intersection to Hwangnam Elementary School Intersection.
        A few years ago, young people began to gather here, and cafes with a nice atmosphere, cute props, souvenir shops, and unique restaurants opened.
        In the beginning, shops were built mainly along the roadside, but as the outer edge of Hwangridan-gil expanded, unique shops began popping up in every alley.
        It is so hot that it has become an essential course that cannot be missed when traveling to Gyeongju.
        Go to the cafe you were looking for, knock on the door of a restaurant that catches your eye while walking, or go to the last stage of your Gyeongju trip to get a cute souvenir to commemorate Gyeongju. Let’s eat, drink, and have fun on Hwangridan-gil.
        '''
#추천 장소 4곳
rec_place = ['Cheomseongdae', 'Bomunho Lake', 'Woljeonggyo Bridge', 'Daereungwon']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/인화/cheom.jpg', './img/인화/bomunlake.jpg', './img/인화/woljeong_bridge.jpg', './img/인화/daer.jpg']
#추천 장소 설명 4개
rec_caption = ['It is an astronomical observatory from the Silla period that observed the movement of celestial bodies.',
                'Bomun Lake, a huge artificial lake measuring 500,000 pyeong',
                'Opening hours: 09:00-22:00\
                Admission fee: Free\
                Parking information: Use Woljeonggyo public parking lot (153-5 Gyo-dong, free)',
                'Opening hours: 09:00-22:00 (ticket sales close at 21:30)\
                Admission fee: Free (Cheonmachong Tomb paid)\
                Parking: Daereungwon public parking lot (9 Gyerim-ro, paid), Nodong public parking lot (767 Taejong-ro, paid), Jjoksae temporary parking lot (Enter Wonhwa-ro 181beon-gil, free)']
# 관광지 Image 1
image1 = './img/인화/hwanglidan.jpg'
#Wordcloud Image 2
image2 = './img/인화/황리단길 워드클라우드.png'
#파이차트 경로
data = 'data/경북/황리단길.csv'
#Positive 개수
pos = 193
#Negative 개수
neg = 117
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/인화/황리단길그래프.png'
# 영어 후기
# Its a great place for walking lots of coffee shops and fun snacks Downside it is usually very crowded

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab2, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(대릉원)-------------------------
# #관광지명
name = list[2]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EA%B4%91%EC%95%88%EB%A6%AC%ED%95%B4%EC%88%98%EC%9A%95%EC%9E%A5/data=!3m2!1e3!4b1!4m6!3m5!1s0x3568ed2f27c70ec7:0xff6df0e14d9216fb!8m2!3d35.1531696!4d129.118666!16s%2Fm%2F03hp9yc?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
        Tomb ruins are scattered throughout the area, centered around Daereungwon, where 23 tombs from the Silla period are gathered on a large land of 126,500 m2.
    Even just looking around the inside of Daereungwon will take quite a bit of time.
    Ancient tombs worth paying attention to include the tomb of King Michu, the 13th king,
    Hwangnamdaechong Tomb, which catches the eye with its huge double-shaped tomb, and Cheonmachong Tomb, where you can look inside the tomb.
    The picturesque photo zone of a magnolia tree standing between ancient tombs is a viewing point of Daereungwon that should not be missed.
        '''
#추천 장소 4곳
rec_place = ['Cheonmachong', 'Cheomseongdae', 'Woljeonggyo Bridge', 'Bomunjeong']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/인화/cheonma.jpg', './img/인화/cheom.jpg', './img/인화/woljeong_bridge.jpg', './img/인화/bomunjeong.jpg']
#추천 장소 설명 4개
rec_caption = ['Operating hours 09:00-22:00\
                        Admission fee: Adults 3,000 / Soldiers, Youth 2,000 / Children 1,000',
                       'It is an astronomical observatory from the Silla period that observed the movement of celestial bodies.',
                       'Opening hours: 09:00-22:00\
                       Admission fee: Free\
                        Parking information: Use Woljeonggyo public parking lot (153-5 Gyo-dong, free)',
                       'Bomunjeong boasts such beautiful scenery that it was once introduced as ‘Korea’s Secret Place’ on CNN.\
                       Cherry trees and maple trees are planted around the octagonal pavilion and two ponds, \
                       making it a place to enjoy the scenery in any season.']
# 관광지 Image 1
image1 = './img/인화/daer.jpg'
#Wordcloud Image 2
image2 = './img/인화/대릉원 워드클라우드.png'
#파이차트 경로
data = 'data/경북/대릉원.csv'
#Positive 개수
pos = 164
#Negative 개수
neg = 33
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/인화/대릉원그래프.png'
# 영어 후기
# Nice area Very beautiful place / good
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab3, name, googlelink, intro, image1, image2, data, pos, neg, image3)
# --------------------------(첨성대)-------------------------

#관광지명
name = list[3]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%B2%A8%EC%84%B1%EB%8C%80/data=!3m1!1e3!4m10!1m2!2m1!1z7LKo7ISx64yA!3m6!1s0x35664e67aead8a6b:0x28a9d45e5267e482!8m2!3d35.8346828!4d129.2190631!15sCgnssqjshLHrjIBaCyIJ7LKo7ISx64yAkgENaGlzdG9yaWNfc2l0ZeABAA!16zL20vMDI3MWQz?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
        It is an astronomical observatory from the Silla Dynasty that observed the movement of celestial bodies. It had a cylindrical part shaped like a liquor bottle on top of the stylobate, which served as a pedestal, and a crown shaped like the letter 井 on top. It is approximately 9m high.
    The cylindrical part is made of 27 layers of fan-shaped stones, and compared to the smooth and well-trimmed exterior, the interior walls are uneven due to the back roots of the stones sticking out. Centered around the southeastern window, the lower part is filled with masonry stones, and the upper part is open to the top and is hollow. The eastern half of the summit is blocked by flagstones, and the ends of long stones interlocked in the shape of the letter 井 protrude to the outside. This type of appearance is also found in levels 19 to 20 and levels 25 to 26, and appears to have been suitable for carrying a ladder inside. According to an old record, “people are supposed to go up in the middle,” and it appears that they placed a ladder outside, went inside through the window, and then used the ladder to climb to the top and observe the sky.
    Astronomy is deeply related to agriculture in that it can determine the timing of farming based on the movement of the sky, and is also related to politics, given that astrology, which predicted good or bad times for a country based on observation results, was considered important in ancient countries. You can see how deep this is. Therefore, it became a matter of great national interest from early on, and it is believed that this served as a good background for the construction of Cheomseongdae.
    It is believed to have been built during the reign of Queen Seondeok of Silla (reign 632-647). It is of great value as the oldest astronomical observatory in the East and can be said to be a valuable national heritage that shows the high level of science at the time.
        '''
#추천 장소 4곳
rec_place = ['Woljeonggyo Bridge','Daereungwon','Donggung Palace and Wolji Pond','Cheonmachong']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/인화/woljeong_bridge.jpg', './img/인화/daer.jpg', './img/인화/dongpalace.jpg', './img/인화/cheonma.jpg']
#추천 장소 설명 4개
rec_caption = ['Opening hours: 09:00-22:00\
                       Admission fee: Free\
                        Parking information: Use Woljeonggyo public parking lot (153-5 Gyo-dong, free)',
                       'Opening hours: 09:00-22:00 (ticket sales close at 21:30)\
                        Admission fee: Free (Cheonmachong Tomb paid)\
                        Parking: Daereungwon public parking lot (9 Gyerim-ro, paid), Nodong public parking lot (767 Taejong-ro, paid), Jjoksae temporary parking lot (Enter Wonhwa-ro 181beon-gil, free)',
                       'Announcement time: 09: 00 - 22:00(ticket date 21: 30), short break \
                        Fee: Adults 3,000won / 2,000won / Children1,000won',
                       'Operating hours 09:00-22:00\
                        Admission fee: Adults 3,000 / Soldiers, Youth 2,000 / Children 1,000']
# 관광지 Image 1
image1 = './img/인화/cheom.jpg'
#Wordcloud Image 2
image2 = './img/인화/첨성대 워드클라우드.png'
#파이차트 경로
data = 'data/경북/첨성대.csv'
#Positive 개수
pos = 173
#Negative 개수
neg = 75
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/인화/첨성대그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab4, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(영일대해수욕장)-------------------------

#관광지명
name = list[4]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%98%81%EC%9D%BC%EB%8C%80%ED%95%B4%EC%88%98%EC%9A%95%EC%9E%A5/data=!3m2!1e3!4b1!4m6!3m5!1s0x356703a3f05e4869:0x98f8a6822ea8a54c!8m2!3d36.0561507!4d129.3781717!16s%2Fg%2F12mb3mrxq?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
         Pohang Yeongildae Beach, where roses and the sea come together
    Pohang Yeongildae Beach is a representative beach in Pohang.
    It was originally called Bukbu Beach, but the name was changed to ‘Yeongildae Beach’ in June 2013 when ‘Yeongildae Marine Pavilion’ was built.
    The night view of Yeongil University & POSCO is considered a representative night view attraction in Pohang, being designated as the 5th view among the 12 scenic views of Pohang.
        '''
#추천 장소 4곳
rec_place = ['Space Walk','Pohang Maritime skywalk','Chilpo Beach','Pohang--Songdo Beach']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/인화/spacewalk.jpg', './img/인화/pohangsky.jpg', './img/인화/chilpo.jpg', './img/인화/pohangsongdo.jpg']
#추천 장소 설명 4개
rec_caption = ['The Space Walk, located in Pohang Hwanhwa Park, was built with a track length of 333m and a number of stairs of 717.',
                'The height is 7m and the total length is 463m.\
                The largest scale in the country\
                This is a walking trail where you can walk on the beautiful sea of Pohang.',
                'Chilpo Beach, located 13km north of Pohang, was opened early as a beach with a wide white sand beach and clear, shallow water.',
                'Songdo Beach was a representative beach in Gyeongsangbuk-do, but was closed due to worsening erosion of the white sand beach, and has been redeveloped as a tourist destination since 2012.']
# 관광지 Image 1
image1 = './img/인화/youngildae.jpg'
#Wordcloud Image 2
image2 = './img/인화/영일대해수욕장 워드클라우드.png'
#파이차트 경로
data = 'data/경북/영일대해수욕장.csv'
#Positive 개수
pos = 56
#Negative 개수
neg = 14
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/인화/영일대해수욕장그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab5, name, googlelink, intro, image1, image2, data, pos, neg, image3)




