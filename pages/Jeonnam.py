import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.header('Jeonnam')
list = ['Mokpo Marine Cable Car North Port Platform', 'Suncheon Bay National Garden', 'Yi Sun-sin Square','Suncheon Bay Wetland', 'Gwanbangjerim Forest, Damyang']
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

# --------------------------(목포해상케이블카 북항승강장)-------------------------

#관광지명
name = list[0]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EB%AA%A9%ED%8F%AC%ED%95%B4%EC%83%81%EC%BC%80%EC%9D%B4%EB%B8%94%EC%B9%B4+%EB%B6%81%ED%95%AD+%EC%8A%B9%EA%B0%95%EC%9E%A5/data=!3m2!1e3!4b1!4m6!3m5!1s0x3573bb2cbbf39d67:0x489aa56de0a4abb1!8m2!3d34.79841!4d126.3693527!16s%2Fg%2F11t9pgkq23?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
           Gwanbangje is an embankment on Gwanbangcheon Stream that is 6km long from Dongja Village in Namsan-ri, Damyang-eup, through Hwanggeum-ri, Subuk-myeon, to Gangneung-ri, Daejeon-myeon. 
           The reason why Gwanbangje is famous is because it forms a huge forest spanning about 2km. This scenic forest is called Gwanbangjerim, and it is densely packed with trees estimated to be 300 to 400 years old in an area of 49,228 m2. 
           Because of its beauty, it was designated as a natural monument on November 27, 1991, and in 2004, it won the grand prize at the ‘5th Beautiful Forest National Competition’ hosted by the Korea Forest Service. 
           The main tree species are Pujo tree (111 trees), Hackberry tree (18 trees), Cherry tree (9 trees), Yin tree (1 tree), Hornbeam tree (1 tree), Bear's horseradish, and Japanese oak. 
           There are about 420 trees growing there. . Currently, 185 old, large trees are growing in the area designated as a natural monument. 
           In addition, Gwanbangjerim is in the spotlight as a summer resort and is also widely known as a date spot for young couples. 
           Chuseong Stadium is located on the highlands around Gwanbangjerim, and a sculpture park with folk tales was built in 2005, adding to the attractions.
           In order to control the waterway of Damyangcheon, the upper stream of the Yeongsangang River, the government embankment system was established by the governor Seong Iseong (成以性) who built an embankment and planted trees. 
           Afterwards, in 1854 (the 5th year of King Cheoljong's reign), the governor Hwang Jong-rim (黃鍾林) became the official secretary. It is said that it was named Gwanbangje because it was built by mobilizing 30,000 people.
        '''
#추천 장소 4곳
rec_place = ['Mokpo Marine Cable Car Yudalsan Platform', 'Mokpo Skywalk', 'Yudal Mountain', 'Mokpo Gatbawi Rock']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/인화/목포유달산승강장.jpg', './img/인화/목포스카이워크.jpg', './img/인화/유달산.jpg', './img/인화/목포갓바위.jpg']
#추천 장소 설명 4개
rec_caption = ['The longest cable in Korea at 3.23km. At 155m, it is the second tallest cable car tower in the world. Yudalsan platform is the middle point among the three platforms!',
                'Operating hours: Summer 09:00~21:00 , Winter season 09:00~20:00 From the observatory, you can enjoy a beautiful view of the open sea and Gojeong Bridge, and a photo zone is set up, making it perfect for making great memories.',
                'The entire Yudal Mountain is made of granite and has a steep slope, but some gentle terrain is formed along the circuit road.',
                'It was designated as a natural monument on April 27, 2009. Gatbawi Rock consists of two pieces, the larger one is 8m long and the smaller one is about 6m long.']
# 관광지 Image
image1 = './img/인화/목포북항승강장.jpg'
#Wordcloud
image2 = './img/인화/목포해상케이블카 북항승강장 워드클라우드.png'
#파이차트 경로
data = 'data/전남/목포해상케이블카 북항승강장.csv'
#Positive 개수
pos_cnt = 148
#Negative 개수
neg_cnt = 114
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/인화/목포해상케이블카 북항승강장그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab1, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# --------------------------(순천만국가정원)-------------------------
#관광지명
name = list[1]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%88%9C%EC%B2%9C%EB%A7%8C%EA%B5%AD%EA%B0%80%EC%A0%95%EC%9B%90/data=!3m2!1e3!4b1!4m6!3m5!1s0x356e08d4d3d1ec8b:0xa382c2c220219851!8m2!3d34.9284391!4d127.4982691!16s%2Fg%2F11bwcrz0fw?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
        It is Korea's first national garden and one of the world's five largest coastal wetlands.
        Suncheon Bay National Garden, created to protect Suncheon Bay, has 790,000 trees of 505 species and 3.15 million flowers of 113 species planted on 1.12 million m2 (340,000 pyeong) of garden land in the Dosa-dong area of Suncheon.
        In spring, tulips and azaleas burst into flower buds, creating a spectacular sight. In addition, 30,000 m2 around the Sharing Forest was created as a rapeseed flower complex, which blooms all at once in mid-May, creating a wave of yellow.
        The city planted 50,000 hackberry trees and zelkova trees along major traffic routes to create natural shade. A small unmanned track train (PRT) is also in operation between Suncheon Bay Garden and Suncheon Literature Museum (4.64km).
        Visitors who have fully explored the garden can take the PRT to the Literature Museum, get off, and then take the reed train for the 1.2km distance to Mujingyo Bridge at the entrance to Suncheon Bay.
        We also operate eco-friendly transportation methods such as Sky Cube, a sky taxi that connects Suncheon Bay National Garden and wetlands.
        '''
#추천 장소 4곳
rec_place = ['Suncheon Bay Wetland', 'Ocheon Green Square', 'Suncheon Bay Natural Ecology Center', 'Naganeupseong Walled Town']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/인화/순천만습지.jpg', './img/인화/오천그린광장.jpg', './img/인화/순천만자연생태관.jpg', './img/인화/순천낙안읍성.jpg']
#추천 장소 설명 4개
rec_caption = ['Operating Hours : March~April, September~October 08:00~18:00 May~August 08:00~19:00 November~February 08:00~17:00',
                'In Suncheon, the lawn plaza in the middle of the city created for the garden fair is emerging as a popular spot to escape the tropical nights.',
                'At the Suncheon Bay Natural Ecology Center, an ecological learning center where you can see and learn information about the various creatures of Suncheon Bay, you can listen to interesting explanations about Suncheon Bay with a guide.',
                'It is a castle built with earth in the early Joseon Dynasty to prevent damage from frequent Japanese invasions starting from the late Goryeo Dynasty.']
# 관광지 Image 1
image1 = './img/인화/순천만국가정원.jpg'
#Wordcloud Image 2
image2 = './img/인화/순천만국가정원 워드클라우드.png'
#파이차트 경로
data = 'data/전남/순천만국가정원.csv'
#Positive 개수
pos_cnt = 388
#Negative 개수
neg_cnt = 202
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/인화/순천만국가정원그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab2, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# --------------------------(이순신광장)-------------------------
#관광지명
name = list[2]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%9D%B4%EC%88%9C%EC%8B%A0%EA%B4%91%EC%9E%A5/data=!3m2!1e3!4b1!4m6!3m5!1s0x356dd8da215ff693:0xad41a8200c7b3fc!8m2!3d34.7395111!4d127.7360119!16s%2Fg%2F11fy2ky1k_?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
        Yi Sun-sin Square, located in Jungang-dong, Yeosu, is a place where you can see and feel the historical scene, including information on Admiral Yi Sun-sin, who led the Japanese invasions of Korea to victory and an introduction to the volunteer army at the time.
        The square is the starting point of a historical, cultural and tourism belt linked to surrounding historic sites such as Jinnamgwan, where Admiral Yi Sun-sin developed his military plans and issued military orders.
        The Turtle Ship Festival, the oldest patriotic cultural festival in Korea, is held every May.
        The most eye-catching structure here is the Turtle Ship, which is reproduced close to its original form.
        It was designed not only for its exterior appearance but also for viewing from the inside.
        If you go inside the turtle ship, you can feel the dynamic appearance of the naval forces and vivid scenes from the Japanese invasions of Korea during the Japanese invasions of Korea.
        You can also try simple experiences. There were three turtle ships that were active during the Japanese invasions, one each built at the Jeolla Jwasuyeong, Bangdapjin, and Suncheonbu shipyards.
        The location of the turtle ship is exactly where the Jeolla Jwasuyeong shipyard was located.
        On one side of Yi Sun-sin Square, there is a mural depicting the life of Admiral Yi Sun-sin and the process of the Japanese invasions of Korea.
        '''
#추천 장소 4곳
rec_place = ['Yeosu Romantic Carriage Street', 'Goso-dong Mural Village', 'Yeosu Marine Cable Car', 'Yeosu Minam Cruise']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/인화/여수포차거리.jpg', './img/인화/고소동벽화마을.jpg', './img/인화/여수해상케이블카.jpg', './img/인화/여수크루즈.jpg']
#추천 장소 설명 4개
rec_caption = ['A food stall street where you can eat while enjoying the night sea in Yeosu',
                'This is a place where Yeosu citizens enjoy a more beautiful night.',
                'One in four Koreans has already experienced the Yeosu Marine Cable Car.',
                'If you want to enjoy the romantic night view of Yeosu’s night sea and fireworks, come here.',
               ]
# 관광지 Image 1
image1 = './img/인화/이순신광장.jpg'
#Wordcloud Image 2
image2 = './img/인화/이순신광장 워드클라우드.png'
#파이차트 경로
data = 'data/전남/이순신광장.csv'
#Positive 개수
pos_cnt = 58
#Negative 개수
neg_cnt = 35
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/인화/이순신광장그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab3, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# --------------------------(순천만습지)-------------------------

#관광지명
name = list[3]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%88%9C%EC%B2%9C%EB%A7%8C%EC%8A%B5%EC%A7%80/data=!3m1!1e3!4m10!1m2!2m1!1z7Iic7LKc66eM7Iq17KeA!3m6!1s0x356e085330966cef:0xabf75a0e61021820!8m2!3d34.885971!4d127.5090298!15sCg_siJzsspzrp4zsirXsp4BaEyIR7Iic7LKcIOunjCDsirXsp4CSAQ9lY29sb2dpY2FsX3BhcmvgAQA!16s%2Fm%2F076xd1n?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
        Suncheon Bay is a bay located in the midwestern part of the southern coast of Korea, surrounded by Suncheon-si, Goheung-gun, and Yeosu-si in Jeollanam-do.
        The large bay surrounded by the long stretches of Goheung Peninsula and Yeosu Peninsula is sometimes called Suncheon Bay, and the northern sea-level bay surrounded by Inan-dong and Daedae-dong of Suncheon-si and Seonhak-ri and Sangnae-ri of Haeryong-myeon is also called Suncheon Bay.
        Even if we consider only the seawater area of Suncheon Bay in the administrative district, it is a very large area of over 75㎢.
        The total area of the tidal flats exposed during low tide reaches 12㎢, and the total area of the tidal flats is 22.6㎢.
        In addition, from the confluence of Dongcheon and Isacheon in Suncheon to the front of the tidal flat of Suncheon Bay, a huge reed colony with a total area of 5.4㎢ is spread out.
        '''
#추천 장소 4곳
rec_place = ['Suncheon Bay Natural Ecology Center','Suncheon Bay National Garden',' Waon Beach','Naganeupseong Walled Town']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/인화/순천만자연생태관.jpg', './img/인화/순천만국가정원.jpg', './img/인화/와온해변.jpg', './img/인화/순천낙안읍성.jpg']
#추천 장소 설명 4개
rec_caption = ['At the Suncheon Bay Natural Ecology Center, an ecological learning center where you can see and learn information about the various creatures of Suncheon Bay, you can listen to interesting explanations about Suncheon Bay with a guide.',
                'It is Korea\'s first national garden and one of the world\'s five largest coastal wetlands.',
                'It is a place with beautiful sunset views, and the sight of the sun setting over Sol Island in front of Waon Beach creates a spectacular sight.',
                'It is a castle built with earth in the early Joseon Dynasty to prevent damage from frequent Japanese invasions starting from the late Goryeo Dynasty.']
# 관광지 Image 1
image1 = './img/인화/순천만습지.jpg'
#Wordcloud Image 2
image2 = './img/인화/순천만습지 워드클라우드.png'
#파이차트 경로
data = 'data/전남/순천만습지.csv'
#Positive 개수
pos_cnt = 193
#Negative 개수
neg_cnt = 97
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/인화/순천만습지그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab4, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# --------------------------(담양 관방제림)-------------------------

#관광지명
name = list[4]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EB%8B%B4%EC%96%91+%EA%B4%80%EB%B0%A9%EC%A0%9C%EB%A6%BC/data=!3m2!1e3!4b1!4m6!3m5!1s0x3571ea8b3ee9d087:0x62aaf2656e0b1e69!8m2!3d35.3235622!4d126.9891545!16s%2Fg%2F12129ydh?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
        Gwanbangje is an embankment on Gwanbangcheon Stream that is 6km long from Dongja Village in Namsan-ri, Damyang-eup, through Hwanggeum-ri, Subuk-myeon, to Gangneung-ri, Daejeon-myeon.
        The reason why Gwanbangje is famous is because it forms a huge forest spanning about 2km.
        This scenic forest is called Gwanbangjerim, and it is densely packed with trees estimated to be 300 to 400 years old in an area of 49,228 m2.
        Because of its beauty, it was designated as a natural monument on November 27, 1991, and in 2004, it won the grand prize at the ‘5th Beautiful Forest National Competition’ hosted by the Korea Forest Service.
        The main tree species are Pujo tree (111 trees), Hackberry tree (18 trees), Cherry tree (9 trees), Yin tree (1 tree), Hornbeam tree (1 tree), Bear's horseradish, and Japanese oak. There are about 420 trees growing there.
        Currently, 185 old, large trees are growing in the area designated as a natural monument. In addition, Gwanbangjerim is in the spotlight as a summer resort and is also widely known as a date spot for young couples.
        Chuseong Stadium is located on the highlands around Gwanbangjerim, and a sculpture park with folk tales was built in 2005, adding to the attractions.
        In order to control the waterway of Damyangcheon, the upper stream of the Yeongsangang River, the government embankment system was established by the governor Seong Iseong (成以性) who built an embankment and planted trees.
        Afterwards, in 1854 (the 5th year of King Cheoljong's reign), the governor Hwang Jong-rim (黃鍾林) became the official secretary. It is said that it was named Gwanbangje because it was built by mobilizing 30,000 people.
        '''
#추천 장소 4곳
rec_place = ['Damyang Noodle Street','Meta-Provence','Metasequoia Garosu-gil','Soswaewon Garden']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/인화/담양국수거리.jpg', './img/인화/메타프로방스.jpg', './img/인화/메타세쿼이아.jpg', './img/인화/소쇄원.jpg']
#추천 장소 설명 4개
rec_caption = ['There are outdoor tables from the beginning to the end of the noodle street, so you can enjoy a generous amount of noodles at a reasonable price while looking out at the lovely view of the Yeongsan River.',
                'Meta-Provence is a place visited by about 5 million tourists a year and has the feel of a replica of Provence, a French city famous as a resort.',
                'As I walk along the Metasequoia Road, I become immersed in the exotic scenery and find myself drawn into a southern road without even realizing it.',
                'Soswaewon, along with Bogildo\'s Buyongdong Garden, is a representative byeolseo (a house built separately near a farm or field) garden of the Joseon Dynasty that harmonized nature and artificiality.']
# 관광지 Image 1
image1 = './img/인화/담양관방제림.jpg'
#Wordcloud Image 2
image2 = './img/인화/담양관방제림 워드클라우드.png'
#파이차트 경로
data = 'data/전남/담양관방제림.csv'
#Positive 개수
pos_cnt = 61
#Negative 개수
neg_cnt = 23
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/인화/담양관방제림그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab5, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)