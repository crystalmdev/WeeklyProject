import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.header('Seoul')
list = ['Seoul Botanic Park', 'Lotte World', 'Gyeongbokgung Palace', 'Seokchonhosu Lake', "Seoul Children's Grand Park"]
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
        '경복궁': ['Gyeongbokgung', './img/수정/경복궁.webp', 'Gyeongbokgung Palace was built as the official palace of the Joseon dynasty by Yi Seong-gye, who becomes King Taejo and the founder of the new regime. Gyeongbokgung Palace is arguably the most beautiful and is the largest of all five palaces.'],
        '서울어린이대공원' : ["Seoul Children's Grand Park", './img/수정/서울어린이대공원.jpeg', 'Opened in May 1973, Seoul Children’s Grand Park is a theme park situated among green forests and fields with a total area of 56,552㎡. It contains a zoo, arboretum, amusement park, and performance venues.'],
        '청계천' : ['Cheonggyecheon Stream', './img/수정/청계천.jpeg', 'Cheonggyecheon Stream is accessible from the square through stairs on the left and Cheonggye Trail on the right.  spectacular sight is created by three-color lights illuminating the fountains and a two-tiered waterfall coming down from a height of four meters.'],
        '남산서울타워' : ['Namsan Seoul Tower', './img/수정/남산서울타워.jpeg', "Namsan Seoul Tower was the first multipurpose tower to be established in Korea, effectively incorporating a sightseeing observatory to a broadcasting tower. The tower's observatory offers an unobstructed view of the whole city, allowing it to become one of the all-time favorite attractions of Seoul citizens as well as domestic and international tourists."],
        '석촌호수' : ['Seokchonhosu Lake', './img/수정/석촌호수.jpeg', "Songpa Naru Park, also commonly referred to as Seokchonhosu Lake, is a citizen park in Seoul with a jogging course and walking trails."],
        '서울스카이' : ['Lotte World Tower SEOUL SKY', './img/수정/서울스카이.jpeg', "SEOUL SKY is located on floors 117-123 of Lotte World Tower, the nation's tallest and the world's fifth tallest building. The observatory offers a panoramic view of the entire capital city, beautiful both day and night."],
        '서촌한옥마을': ['Seochon Village', './img/수정/서촌마을.jpeg', "Seochon Village is the name given to the area to the west of Gyeongbokgung Palace. It is a historic village, home to old shops and hanok buildings that have stood the test of time."],
        '덕수궁': ['Deoksugung Palace', './img/수정/덕수궁.jpeg', "Registered as Historic Site No. 124, Deoksugung Palace was initially not a royal palace, but a residential home of Grand Prince Wolsan (1454-1488), the older brother of King Seongjong (1469-1494) of the Joseon dynasty."],
        '광화문': ['Gwanghwamun', './img/수정/광화문.webp', "Built in 1395 under the reign of King Taejo, the first king of the Joseon dynasty, Gwanghwamun Gate is the southern gate of Gyeongbokgung Palace. It is also the main gate of the palace, therefore larger and fancier in comparison to the other gates."],
        '창덕궁': ['Changdeokgung Palace', './img/수정/창덕궁.jpeg', " [UNESCO World Heritage Site] Changdeokgung Palace was the second royal villa built following the construction of Gyeongbokgung Palace in 1405. It was the principal palace for many kings of the Joseon dynasty, and is the most well-preserved of the five remaining royal Joseon palaces."],
        '송리단길': ['Songnidan-gil Street', './img/수정/송리단길.jpeg', "Located south of the eastern side of Seokchon Lake, this street is home to numerous restaurants and cafes. Today’s “Songnidan-gil Street” came to be as cafes moved into the neighborhood, followed by restaurants and photography studios."],
        '롯데월드 어드벤처': ['Lotte World', './img/수정/롯데월드.png', 'Operated by Lotte Group, Lotte World is the perfect spot for entertainment and sightseeing for Koreans and international tourists alike. The theme park is divided into the indoor Lotte World Adventure, and the outdoor lakeside Magic Island, with additional amenities including a shopping mall, folk museum, ice rink, hotel, and more.'],
        '우리유황온천': ['Our Sulfur Hot Springs', './img/수정/우리유황온천.jpeg', "Our Sulfur Hot Springs supplies natural sulfur hot spring water of 32.6 degrees Celsius from 1,040 meters underground every day. Centered around the main hot spring bath where you can take a sulfur hot spring bath, there is a salt room where you can take a salt compress, a crypt room, a sitz bath, a snack bar, and a sports massage room."],
        }
# --------------------------(서울식물원)-------------------------
#관광지명
name = list[0]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%84%9C%EC%9A%B8%EC%8B%9D%EB%AC%BC%EC%9B%90/data=!3m1!1e3!4m10!1m2!2m1!1z7ISc7Jq47Iud66y87JuQ!3m6!1s0x357c9d01503c1eeb:0x947516d30347709a!8m2!3d37.5694332!4d126.8350132!15sCg_shJzsmrjsi53rrLzsm5CSARBib3RhbmljYWxfZ2FyZGVu4AEA!16s%2Fg%2F11hbqpg8n5?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''The Seoul Botanical Garden was created in Magok, the last remaining development site in Seoul, to introduce native plants and horticulture of 12 different cities from around the world and raise ecological awareness in the city. Seoul Botanic Park integrates a botanical garden and a public park, and the area is the size of 70 soccer fields. It serves as a bridgehead and lifelong education institution with the aim of spreading urban garden culture while staying true to its original role as a plant research conservation institution through expanding endangered wild plant habitats, researching the proliferation of species, and developing varieties. The botanical garden is divided into four spaces: Open Forest, Themed Garden, Lake Garden, and Wetland Garden. The main highlight is the Themed Garden that comprises the Botanic Center, Mogok Cultural Hall, and an outdoor themed garden. '''
#추천 장소 4곳
rec_place = [dict1['경복궁'][0], dict1['서울어린이대공원'][0], dict1['청계천'][0], dict1['남산서울타워'][0]]
#추천 장소 이미지 경로 4개
rec_place_img = [dict1['경복궁'][1], dict1['서울어린이대공원'][1], dict1['청계천'][1], dict1['남산서울타워'][1]]
#추천 장소 설명 4개
rec_caption = [dict1['경복궁'][2], dict1['서울어린이대공원'][2], dict1['청계천'][2], dict1['남산서울타워'][2]]
# 관광지 Image
image1 = 'img/수정/서울식물원.jpeg'
#Wordcloud
image2 = 'img/수정/서울/서울식물원 워드클라우드.png'
#파이차트 경로
data = 'data/서울/서울식물원.csv'
#Positive 개수
pos = 385
#Negative 개수
neg = 208
#Bigram NetworkX Graph 이미지 첨부
image3 = 'img/수정/서울/서울식물원그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab1, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(롯데월드 어드밴처)-------------------------
#관광지명
name = list[1]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EB%A1%AF%EB%8D%B0%EC%9B%94%EB%93%9C/data=!3m1!1e3!4m10!1m2!2m1!1z66Gv642w7JuU65OcIOyWtOuTnOuypOyymA!3m6!1s0x357ca5a7250efe81:0x433df2c1fec03b98!8m2!3d37.5111158!4d127.098167!15sChnroa_rjbDsm5Trk5wg7Ja065Oc67Kk7LKYIgOIAQGSAQp0aGVtZV9wYXJr4AEA!16zL20vMDNqbGo5?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Operated by Lotte Group, Lotte World is the perfect spot for entertainment and sightseeing for Koreans and international tourists alike. The theme park is divided into the indoor Lotte World Adventure, and the outdoor lakeside Magic Island, with additional amenities including a shopping mall, folk museum, ice rink, hotel, and more. Lotte World Adventure is the world's largest indoor amusement park, complete with top-of-the-line rides, fantastic parades and performances, and food from around the world. The Folk Museum displays miniature models of Korea throughout 5,000 years in history. Lotte World Garden Stage presents various themed musicals to match each season and Lotte World Star Avenue is the perfect place to experience Korean stars and the entertainment world.'''
#추천 장소 4곳
rec_place = [dict1['석촌호수'][0], dict1['서울스카이'][0], dict1['서울어린이대공원'][0], dict1['경복궁'][0]]
#추천 장소 이미지 경로 4개
rec_place_img = [dict1['석촌호수'][1], dict1['서울스카이'][1], dict1['서울어린이대공원'][1], dict1['경복궁'][1]]
#추천 장소 설명 4개
rec_caption = [dict1['석촌호수'][2], dict1['서울스카이'][2], dict1['서울어린이대공원'][2], dict1['경복궁'][2]]
# 관광지 Image 1
image1 = 'img/수정/롯데월드.png'
#Wordcloud Image 2
image2 = 'img/수정/서울/롯데월드 어드벤처 워드클라우드.png'
#파이차트 경로
data = 'data/서울/롯데월드 어드벤처.csv'
#Positive 개수
pos = 445
#Negative 개수
neg = 257
#Bigram NetworkX Graph 이미지 첨부
image3 = 'img/수정/서울/롯데월드 어드벤처그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab2, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(경복궁)-------------------------
#관광지명
name = list[2]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EA%B2%BD%EB%B3%B5%EA%B6%81/data=!3m1!1e3!4m10!1m2!2m1!1z6rK967O16raB!3m6!1s0x357ca2c74aeddea1:0x8b3046532cc715f6!8m2!3d37.579617!4d126.977041!15sCgnqsr3rs7XqtoFaCyIJ6rK967O16raBkgERY3VsdHVyYWxfbGFuZG1hcmvgAQA!16zL20vMDJ2M3Q2?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Gyeongbokgung Palace was built as the official palace of the Joseon dynasty by Yi Seong-gye, who becomes King Taejo and the founder of the new regime. Gyeongbokgung Palace is commonly referred to as the Northern Palace because its location in the north of Changdeokgung Palace in the east and Gyeonghuigung Palace in the west. Gyeongbokgung Palace is arguably the most beautiful and is the largest of all five palaces. Many Joseon kings were crowned here, including the 2nd King Jeongjong, 4th King Sejong, 6th King Danjong, 7th King Sejo, 9th King Seongjong, 11th King Jungjong, and the 13th King Myeongjong. The premises were once destroyed by fire during the Imjin War (1592-1598). However, all of the palace buildings were later restored under the leadership of Heungseondaewongun during the reign of King Gojong. The assassination of Empress Myeongseong, however, resulted in Gyeongbokgung Palace losing its function as a royal palace, eventually witnessing the downfall of the Joseon dynasty. Gyeongbokgung Palace retains the original Gyeonghoeru Pavilion, a prime example of Joseon architecture, and the Hyangwonjeong Pavilion and pond. The sculptures in the Geunjeongjeon Hall exemplify Joseon-era sculpture techniques. The west side of the area outside Heungnyemun Gate is occupied by the National Palace Museum of Korea, while the eastern side of Hyangwonjeong Pavilion within the Gyeongbokgung Palace is occupied by the National Folk Museum of Korea.'''
#추천 장소 4곳
rec_place = [dict1['서촌한옥마을'][0], dict1['덕수궁'][0], dict1['광화문'][0], dict1['창덕궁'][0]]
#추천 장소 이미지 경로 4개
rec_place_img = [dict1['서촌한옥마을'][1], dict1['덕수궁'][1], dict1['광화문'][1], dict1['창덕궁'][1]]
#추천 장소 설명 4개
rec_caption = [dict1['서촌한옥마을'][2], dict1['덕수궁'][2], dict1['광화문'][2], dict1['창덕궁'][2]]
# 관광지 Image 1
image1 = 'img/수정/경복궁.webp'
#Wordcloud Image 2
image2 = 'img/수정/서울/경복궁 워드클라우드.png'
#파이차트 경로
data = 'data/서울/경복궁.csv'
#Positive 개수
pos = 181
#Negative 개수
neg = 81
#Bigram NetworkX Graph 이미지 첨부
image3 = 'img/수정/서울/경복궁그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab3, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(석촌호수)-------------------------
#관광지명
name = list[3]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%84%9D%EC%B4%8C%ED%98%B8%EC%88%98(%EC%84%9C%ED%98%B8)/data=!3m2!1e3!4b1!4m6!3m5!1s0x357ca5a160554ffb:0x27d136ac3a9f1dba!8m2!3d37.5080556!4d127.1005556!16s%2Fg%2F1tk_m6rs?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Songpa Naru Park, also commonly referred to as Seokchonhosu Lake, is a citizen park in Seoul with a jogging course and walking trails. It has two lakes with Songpa-daero Boulevard running in between. Originally, a branch of the Hangang River ran through the site, forming one large lake, but the lake was divided into two with the construction of Songpa-daero Boulevard. The total size of the two lakes is 217,850 ㎡, and they hold about 737 tons of water. The depth of the lakes is 4-5 meters.'''
#추천 장소 4곳
rec_place = [dict1['송리단길'][0], dict1['롯데월드 어드벤처'][0], dict1['서울스카이'][0], dict1['광화문'][0]]
#추천 장소 이미지 경로 4개
rec_place_img = [dict1['송리단길'][1], dict1['롯데월드 어드벤처'][1], dict1['서울스카이'][1], dict1['광화문'][1]]
#추천 장소 설명 4개
rec_caption = [dict1['송리단길'][2], dict1['롯데월드 어드벤처'][2], dict1['서울스카이'][2], dict1['광화문'][2]]
# 관광지 Image 1
image1 = 'img/수정/석촌호수.jpeg'
#Wordcloud Image 2
image2 = 'img/수정/서울/석촌호수 서호 워드클라우드.png'
#파이차트 경로
data = 'data/서울/석촌호수 서호.csv'
#Positive 개수
pos = 61
#Negative 개수
neg = 10
#Bigram NetworkX Graph 이미지 첨부
image3 = 'img/수정/서울/석촌호수 서호그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab4, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(서울어린이대공원)-------------------------
#관광지명
name = list[4]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%96%B4%EB%A6%B0%EC%9D%B4%EB%8C%80%EA%B3%B5%EC%9B%90/data=!3m2!1e3!4b1!4m6!3m5!1s0x357ca4d713856077:0x169df594b1f221cc!8m2!3d37.549363!4d127.0818126!16s%2Fm%2F0h3m64t?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Opened in May 1973, Seoul Children’s Grand Park is a theme park situated among green forests and fields with a total area of 56,552㎡. It contains a zoo, arboretum, amusement park, and performance venues. Seoul Children’s Grand Park has been a beloved part of Seoul, a paradise for children and a living venue for education. For grown-ups, it functions as an area of refuge and culture within the city. The Grand Park offers facilities that everyone in the family can enjoy, so everyone can find their own fun in the Grand Park.'''
#추천 장소 4곳
rec_place = [dict1['남산서울타워'][0], dict1['우리유황온천'][0], dict1['청계천'][0], dict1['경복궁'][0]]
#추천 장소 이미지 경로 4개
rec_place_img = [dict1['남산서울타워'][1], dict1['우리유황온천'][1], dict1['청계천'][1], dict1['경복궁'][1]]
#추천 장소 설명 4개
rec_caption = [dict1['남산서울타워'][2], dict1['우리유황온천'][2], dict1['청계천'][2], dict1['경복궁'][2]]
# 관광지 Image 1
image1 = 'img/수정/서울어린이대공원.jpeg'
#Wordcloud Image 2
image2 = 'img/수정/서울/서울어린이대공원 워드클라우드.png'
#파이차트 경로
data = 'data/서울/서울어린이대공원.csv'
#Positive 개수
pos = 37
#Negative 개수
neg = 9
#Bigram NetworkX Graph 이미지 첨부
image3 = 'img/수정/서울/서울어린이대공원그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab5, name, googlelink, intro, image1, image2, data, pos, neg, image3)
