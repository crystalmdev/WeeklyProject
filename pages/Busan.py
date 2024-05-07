import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
st.header('Busan')
list = ['Gwangalli beach', 'Lotte World Busan', 'Haeundae Beach', 'Dadaepo Beach', 'Haeundae Street food alley']
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

# --------------------------(광안리해수욕장)-------------------------

#관광지명
name = list[0]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EA%B4%91%EC%95%88%EB%A6%AC%ED%95%B4%EC%88%98%EC%9A%95%EC%9E%A5/data=!3m2!1e3!4b1!4m6!3m5!1s0x3568ed2f27c70ec7:0xff6df0e14d9216fb!8m2!3d35.1531696!4d129.118666!16s%2Fm%2F03hp9yc?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Located to the west of Haeundae Beach, Gwangalli Beach is 1.4 kilometers long and 25~110 meters wide, and is famous for its fine sand. The area underwent a water purification process, which led the ecosystem to flourish in the nearby river waters. In addition to the beachfront, the Gwangalli area is filled with delicious restaurants and romantic cafes, as well as stores selling famous fashion brands. The area has plenty to offer, but many people come in the evening to take in the bright lights of Gwangandaegyo Bridge, stretching across the horizon.'''
#추천 장소 4곳
rec_place = ['Songjeong Beach', 'Haeundae Beach', 'Songdo Beach', 'Dalmaji Road']
#추천 장소 이미지 경로 4개
rec_place_img = ['img/수정/송정해수욕장.jpeg',
                 'img/수정/해운대해수욕장.jpeg',
                 'img/수정/송도해수욕장.webp',
                 'img/수정/해운대달맞이길.png']
#추천 장소 설명 4개
rec_caption = ['Songjeong Beach is ideal for families with young children because of its shallow waters. The beach is very popular as a photography venue for pre-wedding photoshoots.',
               'Haeundae Beach is the most famous beach in Busan. The white sand beach creates a beautiful coastline before a shallow bay, making it perfect for swimming.',
               'Songdo Beach was one of the first beaches to open in Korea in 1913. The area has a variety of accommodation and dining options, and is well equipped with convenience facilities such as an overpass, promenade, boat yard etc.',
               'Dalmaji Road refers to the pass that connects Haeundae Beach with Songjeong Beach over Wausan Mountain. It is an 8 km-long coastal road lined with cherry and pine trees, offering a beautiful coast view and a perfect place for seaside drives.']
# 관광지 Image
image1 = 'img/수정/광안리해수욕장.jpeg'
#Wordcloud
image2 = 'img/수정/부산/광안리해수욕장 워드클라우드.png'
#파이차트 경로
data = 'data/부산/광안리해수욕장.csv'
#Positive 개수
pos = 151
#Negative 개수
neg = 65
#Bigram NetworkX Graph 이미지 첨부
image3 = 'img/수정/부산/광안리해수욕장그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab1, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(롯데월드 어드밴처 부산)-------------------------
#관광지명
name = list[1]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EB%A1%AF%EB%8D%B0%EC%9B%94%EB%93%9C+%EC%96%B4%EB%93%9C%EB%B2%A4%EC%B2%98+%EB%B6%80%EC%82%B0/data=!3m2!1e3!4b1!4m6!3m5!1s0x35688df2c51276f1:0xebe28acdea1ee316!8m2!3d35.1968317!4d129.2132274!16s%2Fg%2F11qh3d226h?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Lotte World Adventure opened in Busan, where visitors can experience fun and exciting performances and parades. Busan Lotte World is built in Busan and has convenient access using public transportation, leading to many visitors since the first day of its opening. Lotte World Adventure Busan consists of six themed zones. At the heart of the fairy village, Tinker Falls Zone, is the Talking Tree, which uses animatronic technology to tell the story of six themes in the park. Rory Castle in the Royal Garden Zone, located at the highest point in Lotte World, is designed to look like it is floating on water, and visitors can enjoy the view of Busan and the sea in front of Gijang at a glance. Other rides, especially the Giant Digger and Giant Splash, have already received word-of-mouth excitement. As such, there are not only attractions for adults, but also amusement rides for families with young children. It is placed indoors so that children can safely enjoy it regardless of the weather. The parade, the highlight of the amusement park, runs twice a day for about 30 minutes.'''
#추천 장소 4곳
rec_place = ['Songjeong Beach', 'Gamcheon Culture Village', 'Haeundae Beach', 'Busan Tower']
#추천 장소 이미지 경로 4개
rec_place_img = ['img/수정/송정해수욕장.jpeg',
                 'img/수정/감천문화마을.jpeg',
                 'img/수정/해운대해수욕장.jpeg',
                 'img/수정/부산타워.webp']
#추천 장소 설명 4개
rec_caption = [rec_caption[0], #송정해수욕장
               'Gamcheon Culture Villiage was formed by refugees of the Korean war who built their houses in staircase-fashion on the foothills of a coastal mountain. The many alleys in this community are vibrantly decorated with murals and sculptures created by the residents.',
                rec_caption[1], #해운대해수욕장
               "Busan Tower, standing at 120 meters tall, is an iconic observation tower situated in Busan's Yongdusan Park. This tower offers visitors panoramic views of Busan Port and Yeongdo Island."]
# 관광지 Image
image1 = 'img/수정/롯데월드부산.jpg'
#Wordcloud
image2 = 'img/수정/부산/롯데월드 어드벤처 부산 워드클라우드.png'
#파이차트 경로
data = 'data/부산/롯데월드 어드벤처 부산.csv'
#Positive 개수
pos = 311
#Negative 개수
neg = 238
#Bigram NetworkX Graph 이미지 첨부
image3 = 'img/수정/부산/롯데월드 부산그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab2, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(해운대해수욕장)-------------------------
#관광지명
name = list[2]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%ED%95%B4%EC%9A%B4%EB%8C%80%ED%95%B4%EC%88%98%EC%9A%95%EC%9E%A5/data=!3m2!1e3!4b1!4m6!3m5!1s0x35688d5c0efe075f:0x9963b1d5c163ac98!8m2!3d35.1586975!4d129.1603842!16s%2Fm%2F03bx6xl?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Haeundae Beach is the most famous beach in Busan. The white sand beach is roughly 1.5 kilometers long, over a 30- to 50-meter wide area, creating a beautiful coastline before a shallow bay, making it perfect for swimming. People flock to Haeundae Beach every summer. All kinds of accommodations from luxury hotels to private guesthouses have developed in the area around the beach, making this the perfect summer vacation spot. Haeundae Beach is also famous for various cultural events and festivals held throughout the year. Other facilities in the area include Dongbaekseom Island, Busan Aquarium, a yachting dock, BEXCO, driving courses and more.'''
#추천 장소 4곳
rec_place = ['Dongbaekseom Island', 'Dalmaji Road', 'Haeundae Blueline Park', 'Songjeong Beach']
#추천 장소 이미지 경로 4개
rec_place_img = ['img/수정/동백섬.jpeg',
                 'img/수정/해운대달맞이길.png',
                 'img/수정/블루라인파크.jpeg',
                 'img/수정/송정해수욕장.jpeg']
#추천 장소 설명 4개
rec_caption = ["Dongbaekseom Island (Island of Camellias) is an island located off one end of Busan's famous Haeundae Beach. Dongbaekseom Island is easy to navigate thanks to the walking path that is built around it.",
               'Dalmaji Road refers to the pass that connects Haeundae Beach with Songjeong Beach over Wausan Mountain. It is an 8 km-long coastal road lined with cherry and pine trees, offering a beautiful coast view and a perfect place for seaside drives.',
               'Haeundae Blueline Park is an eco-friendly redevelopment of the former railroad facilities of the Donghae Nambu Line, a 4.8-kilometer-long stretch from Haeundae’s Mipo to Cheongsapo to Songjeong.',
                'Songjeong Beach is ideal for families with young children because of its shallow waters. The beach is very popular as a photography venue for pre-wedding photoshoots.']
# 관광지 Image
image1 = 'img/수정/해운대해수욕장.jpeg'
#Wordcloud
image2 = 'img/수정/부산/해운대해수욕장 워드클라우드.png'
#파이차트 경로
data = 'data/부산/해운대해수욕장.csv'
#Positive 개수
pos = 167
#Negative 개수
neg = 60
#Bigram NetworkX Graph 이미지 첨부
image3 = 'img/수정/부산/해운대해수욕장그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab3, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(다대포해수욕장)-------------------------

#관광지명
name = list[3]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EB%8B%A4%EB%8C%80%ED%8F%AC%ED%95%B4%EC%88%98%EC%9A%95%EC%9E%A5/data=!3m2!1e3!4b1!4m6!3m5!1s0x3568dd14c8f34565:0x9ef60b3754f60850!8m2!3d35.0469015!4d128.9662387!16s%2Fg%2F122_gqsw?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Dadaepo Beach is made from sands deposited by the Nakdonggang River. It features shallow water and a wide sand beach suitable for children. Water activities can be enjoyed at the beach such as paddleboarding, kiteboarding and more. More visitors have been attracted after the addition of a coastal park and walking paths. At the entrance of the beach, there is a grand plaza with a large-scale musical floor fountain. Visitors can enjoy the musical fountain from late-April to October.'''
#추천 장소 4곳
rec_place = ['Morundae', 'Amisan Observatory', 'Haeundae Beach', 'Gamcheon Culture Villiage']
#추천 장소 이미지 경로 4개
rec_place_img = ['img/수정/몰운대.jpeg',
                 'img/수정/아미산전망대.bmp',
                 'img/수정/해운대해수욕장.jpeg',
                 'img/수정/감천문화마을.jpeg']
#추천 장소 설명 4개
rec_caption = ['Morundae-gil Trail, starting from Noeuljeong Pavilion and covering the coast of Morundae Peninsula, is a perfect location to watch the sunset. Memorable attractions along the trail include the point where the Nakdonggang River flows into the southern sea, walking through a coastal pine forest.',
               'Amisan Observatory, where you can look down at the point where the Nakdonggang River and the sea become one,  is a place where visitors can enjoy the golden sunset and appreciate the pleasant scenery of the river and the sea while feeling the cool breeze.',
               'Haeundae Beach is the most famous beach in Busan. The white sand beach creates a beautiful coastline before a shallow bay, making it perfect for swimming.',
               'Gamcheon Culture Villiage was formed by refugees of the Korean war who built their houses in staircase-fashion on the foothills of a coastal mountain. The many alleys in this community are vibrantly decorated with murals and sculptures created by the residents.']

# 관광지 Image
image1 = 'img/수정/다대포해수욕장.jpeg'
#Wordcloud
image2 = 'img/수정/부산/다대포해수욕장 워드클라우드.png'
#파이차트 경로
data = 'data/부산/다대포해수욕장.csv'
#Positive 개수
pos = 87
#Negative 개수
neg = 23
#Bigram NetworkX Graph 이미지 첨부
image3 = 'img/수정/부산/다대포해수욕장그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab4, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(해운대 포장마차촌)-------------------------

#관광지명
name = list[4]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%ED%95%B4%EC%9A%B4%EB%8C%80%ED%8F%AC%EC%9E%A5%EB%A7%88%EC%B0%A8%EC%B4%8C/data=!3m2!1e3!4b1!4m6!3m5!1s0x35688d58f2092243:0xb49654b3d06d8fff!8m2!3d35.1583788!4d129.1569762!16s%2Fg%2F11c1vms3db?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Bada Maeul Pojang Macha Chon, or Ocean City Street Food Alley, is located behind Haeundae Beach and has been in operation for over 20 years. The Ocean City Street Food Alley has over 40 street carts. It was especially famous for its lobster dishes, which included a large steamed lobster and lobster ramyeon, among other freshly caught seafood.'''
#추천 장소 4곳
rec_place = ['Haeundae Beach', 'Dalmaji Road', 'Seafood Pojang Macha Chon', 'Dongbaekseom Island']
#추천 장소 이미지 경로 4개
rec_place_img = ['img/수정/해운대해수욕장.jpeg',
                 'img/수정/해운대달맞이길.png',
                 'img/수정/해물포장마차촌.jpeg',
                 'img/수정/동백섬.jpeg']
#추천 장소 설명 4개
rec_caption = ['Haeundae Beach is the most famous beach in Busan. The white sand beach creates a beautiful coastline before a shallow bay, making it perfect for swimming.',
               'Dalmaji Road refers to the pass that connects Haeundae Beach with Songjeong Beach over Wausan Mountain. It is an 8 km-long coastal road lined with cherry and pine trees, offering a beautiful coast view and a perfect place for seaside drives.',
               'Seafood Pojang Macha Chon is where you can taste a variety of seafood caught in the waters off Gijang.',
               "Dongbaekseom Island (Island of Camellias) is an island located off one end of Busan's famous Haeundae Beach. Dongbaekseom Island is easy to navigate thanks to the walking path that is built around it."]
# 관광지 Image
image1 = 'img/수정/해운대포장마차촌.jpeg'
#Wordcloud
image2 = 'img/수정/부산/해운대 포장마차촌 워드클라우드.png'
#파이차트 경로
data = 'data/부산/해운대포장마차촌.csv'
#Positive 개수
pos = 62
#Negative 개수
neg = 50
#Bigram NetworkX Graph 이미지 첨부
image3 = 'img/수정/부산/해운대포장마차촌그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab5, name, googlelink, intro, image1, image2, data, pos, neg, image3)