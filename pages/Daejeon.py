import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
st.header('Daejeon')
list = ['Sangso-dong Forest Park🌳', 'O-World🎢', 'Jangtaesan Recreational Forest🌲',
        'Daejeon National Soopchewon🌿', 'Hanbat Arboretum🌸']
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

# 상소동--------------------------------------------------------------------------------------

#관광지명
name = list[0]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%83%81%EC%86%8C%EB%8F%99%EC%82%B0%EB%A6%BC%EC%9A%95%EC%9E%A5/data=!3m1!4b1!4m6!3m5!1s0x35654559ceea79af:0xaa0e403886f59245!8m2!3d36.2352607!4d127.4712365!16s%2Fg%2F1wc2_2sh?entry=ttu'
#관광지 소개 글
intro = '''Sangso-dong Forest Park is located at the point where the foothills of Maninsan Mountain and Sikjangsan 
        Mountain meet. The road to the park is beautifully lined with sycamore trees. The park offers various 
        facilities for enjoying nature and in particular, the stone pagodas placed throughout the park are a 
        must-see. Visitors can stack their own rocks and make wishes relating to family, health, relationships, 
        and more. The park is great for walks, hikes, or even just to relax as wild flowers bloom all throughout 
        spring to fall.'''
#추천 장소 4곳
rec_place = ['Jangdong Forest Park', 'Buddong Reservoir', 'Gyeryongsan Fortress', 'Railway Village']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/다율/장동산림욕장.jpg',
                 './img/다율/법동소류지.png',
                 './img/다율/계족산성.jpg',
                 './img/다율/철도관사촌.jpg']
#추천 장소 설명 4개
rec_caption = ["A place to relax and breathe in the fresh air of Gejoksan.",
               "Healing amidst windmills and blooming flowers by the water and nature",
               "Traces of fierce competition between Silla and Baekje",
               "A village holding historical value from the modern and contemporary era"]
# 관광지 Image
image1 = './img/다율/상소동산림욕장.jpg'
#Wordcloud
image2 = './img/다율/상소동산림욕장 워드클라우드.png'
#파이차트 경로
data = 'data/대전/상소동산림욕장.csv'
#Positive 개수
pos_cnt = 28
#Negative 개수
neg_cnt = 5
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/다율/상소동산림욕장 그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab1, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# 오월드-----------------------------------------------------------------------------------------------
#관광지명
name = list[1]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/Daejeon+O-World/data=!3m1!4b1!4m6!3m5!1s0x35654e61dd45625d:0xd9e0f93060ed6a4e!8m2!3d36.2886167!4d127.3969124!16s%2Fg%2F1212gtl8?entry=ttu'
#관광지 소개 글
intro = '''Daejeon O-World was established when the Daejeon Zoo and Joy Land, an amusement park, were integrated 
        under the supervision of the Daejeon City Corporation. The project cost a whopping 40 billion won and 
        resulted in the construction of Flower Land (100,000㎡) in addition to the renamed Zoo Land and the 
        preexisting Joy Land. It opened on May 1, 2009 to the public. The three main sections of Daejeon O-World 
        are Zoo Land, Joy Land, and Flower Land. Zoo Land is currently home to a total of 600 animals of 130 different 
        species including American black bears, Bengal tigers, lions, elephants, giraffes, zebras, and ostriches. 
        Amusement rides, waterslides, and four-season sledding are housed at Joy Land. Flower Land boasts a number 
        of smaller sections such as Rose Garden, Four Season Garden, Herb Garden, and Maze Garden and is home to a 
        total of 150,000 tress of 100 different species and 200,000 flowers of 85 different species. An outdoor stage 
        and concert hall are also located in the area. There are plenty of things to see and enjoy in every corner of 
        Daejeon O-World. Just beyond Festival Street, visitors will find a large (3,000㎡) pond with a fountain.'''
#추천 장소 4곳
rec_place = ['Tinolja Animal Park', 'Euneungjeongi Cultural Street', 'Daejeon Skyroad', 'Bomunsanseong']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/다율/티놀자.jpg',
                 './img/다율/으능정이.jpg',
                 './img/다율/스카이로드.jpeg',
                 './img/다율/보문산성.jpg']
#추천 장소 설명 4개
rec_caption = ["An animal park where you can interact with animals",
               "A cultural and artistic street known as the Myeongdong of Daejeon",
               "Installing a 214m x 13m arcade with multimedia video screens for spectacular shows.",
               "It is speculated to have been built during the intense battles between the late Baekje and Silla periods."]
# 관광지 Image
image1 = './img/다율/오월드.jpg'
#Wordcloud
image2 = './img/다율/대전오월드 워드클라우드.png'
#파이차트 경로
data = 'data/대전/대전오월드.csv'
#Positive 개수
pos_cnt = 118
#Negative 개수
neg_cnt = 65
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/다율/대전오월드 그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab2, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# 장태산자연휴양림-----------------------------------------------------------------------------------------------
#관광지명
name = list[2]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/Jangtaesan+Recreational+Forest/data=!3m1!4b1!4m6!3m5!1s0x356553a079f05293:0xf6814125580cd530!8m2!3d36.2187201!4d127.3401569!16s%2Fg%2F121gv9zc?entry=ttu'
#관광지 소개
intro = '''Jangtaesan Recreational Forest consists of a dense forest of ginkgo trees and bald cypress. Lush valleys 
        nearby make for a great getaway during summer vacation. Yongtaeul Reservoir, located at the entrance, gives 
        beautiful views as well. Inside the natural recreation forest, various facilities including walking paths, 
        beautiful views as well. Inside the natural recreation forest, various facilities including walking paths, 
        physical activity facilities, a botanical garden and bare-foot walking paths are available for visitors.
'''
#추천 장소 4곳
rec_place = ['Gyejoksan Red Clay Trail', 'Daejeon EXPO Plaza', 'Bomunsan Observatory', 'Daedong Mural Village']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/다율/황톳길.jpg', './img/다율/엑스포.jpg', './img/다율/보문산전망대.jpeg', './img/다율/대동벽화마을.jpg']
#추천 장소 설명 4개
rec_caption = ["Let's go trekking barefoot",
               "A space to enjoy cultural activities, leisure, and sports together",
               "Romantic night views in the heart of downtown Daejeon",
               "Known as Daejeon's iconic Dal Dong neighborhood"]
# 관광지 Image
image1 = './img/다율/장태산자연휴양림.jpg'
#Wordcloud
image2 = './img/다율/장태산자연휴양림 워드클라우드.png'
#파이차트 경로
data = 'data/대전/장태산자연휴양림.csv'
#Positive 개수
pos_cnt = 107
#Negative 개수
neg_cnt = 41
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/다율/장태산자연휴양림 그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab3, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# 국립대전숲체원 -------------------------------------------------------------------------------

#관광지명
name = list[3]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EA%B5%AD%EB%A6%BD%EB%8C%80%EC%A0%84%EC%88%B2%EC%B2%B4%EC%9B%90/data=!3m1!4b1!4m6!3m5!1s0x357ab2d659e3f4cb:0xfc25de3d6622f49a!8m2!3d36.3240331!4d127.2909875!16s%2Fg%2F11j4ztgh4_?entry=ttu'
#관광지 소개 글
intro = '''The National Daejeon Forest Wellness Center, a leading forest welfare facility in the central region, 
        offers various forest experience and education programs for people to enhance their physical and mental health 
        through the forest freely. It is the only place in the country where you can enter the forest via an elevator 
        deck road, providing various forest paths, seminar rooms, and spaces for accommodation and meals for anyone to 
        enjoy the forest experience freely.
'''
#추천 장소 4곳
rec_place = ['Bomunsan Forest Healing Center', 'Healing Forest', 'Pangdong Reservoir', 'Gyeryongsan Sutonggol Valley']
#추천 장소 이미지 경로 4개
#추천 장소 설명 4개
rec_caption = ["Experience nature's positive energy and heal both body and mind through forest therapy.",
               "A healing sanctuary for body and mind, nestled in nature.",
               "Transformed into an ecological relaxation space",
               "A scenic trail unfolds with beautiful valleys and picturesque mountains, resembling silk threads."]
# 관광지 Image
image1 = './img/다율/숲체원.jpeg'
#Wordcloud
image2 = './img/다율/국립대전숲체원 워드클라우드.png'
#파이차트 경로
data = 'data/대전/국립대전숲체원.csv'
#Positive 개수
pos_cnt = 17
#Negative 개수
neg_cnt = 7
#Bigram NetworkX Graph 이미지 첨부
image3 = 'img/다율/국립대전숲체원 그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab4, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# 한밭수목원-------------------------------------------------------------------------------

#관광지명./img
name = list[4]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/Hanbat+Arboretum/data=!3m1!4b1!4m6!3m5!1s0x3565497f5d03e619:0xb3fc1a9c65052b0!8m2!3d36.3683723!4d127.3880555!16s%2Fg%2F122xkz0d?entry=ttu'
#관광지 소개 글
intro = '''Hanbat Arboretum, linked with the Government Complex-Daejeon and Science Park, is the largest man-made 
        urban arboretum in Korea. It serves multiple purposes: a reservoir of genetically diverse foliage, 
        an eco-learning center for students, and a recreational area where people can relax and pass the time 
        in the peaceful embrace of nature. The arboretum, standing on a lot measuring 387,000 square meters, is 
        divided into three sections. The West Garden and Nammun Square opened on April 28th, 2005. The East Garden 
        opened on May 9th, 2009, and consists of 19 uniquely themed parks, including the Magnolia Garden, Medicinal 
        Herbs Garden, Rock Garden, and Fruit Garden.'''
#추천 장소 4곳
rec_place = ['Maninsan Recreational Forest', 'Sikjangsan Cultural Park', 'Gabcheon', 'Daecheongho Lake']
#추천 장소 이미지 경로 4개정동진해변
rec_place_img = ['./img/다율/만인산2.jpg', './img/다율/식장산.jpg', './img/다율/갑천.jpg', './img/다율/대청호.jpg']
#추천 장소 설명 4개
rec_caption = ["A place to relax while enjoying the natural scenery.",
               "Daejeon's prominent tourist attraction known for its New Year sunrise event",
               "A place where you can enjoy exercise amidst beautiful scenery",
               "The waterway connecting Daejeon and Cheongju"]
# 관광지 Image
image1 = './img/다율/한밭수목원.jpg'
#Wordcloud
image2 = './img/다율/한밭수목원 워드클라우드.png'
#파이차트 경로
data = 'data/대전/한밭수목원.csv'
#Positive 개수
pos_cnt = 85
#Negative 개수
neg_cnt = 40
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/다율/한밭수목원 그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab5, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)