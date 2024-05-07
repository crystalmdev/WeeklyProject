import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
st.header('Gyeonggi')

list = ['Everland',
        'Hwadam Forest',
        'Seoul Land',
        'Nizimori Studio',
        'Korean Folk Village']
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

# --------------------------(에버랜드)-------------------------

#관광지명
name = list[0]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%97%90%EB%B2%84%EB%9E%9C%EB%93%9C/data=!3m1!4b1!4m6!3m5!1s0x357b5403ce34d773:0x1fa18ab619238098!8m2!3d37.2939104!4d127.2025664!16s%2Fm%2F012dzv65?authuser=0&entry=ttu'
#관광지 소개 글
intro = '''
It is a theme park that provides pleasant rest and joy with various seasonal festivals, attractions, animals and plants. More than 40 kinds of latest attractions in five theme zones provide thrilling thrills, and Wooden Coaster T Express is especially loved by roller coaster enthusiasts. Large entertainment, such as various stage performances and multimedia fireworks shows throughout the park, adds new joy every day, and at the Everland Zoo "Zootopia," which is certified as the first Asian zoo AZA (American Zoo Aquarium Association), you can experience high-quality animal ecology exhibitions such as Safari World and Lost Valley. In addition, you can also see beautiful theme gardens such as tulips and roses, exhibitions and experiences of satisfaction with the five senses at Everland, which has led Korea's flower festival and garden culture for more than 40 years.
'''
#추천 장소 4곳
rec_place = ['Yongin Rural Theme Park',
             'Yongin Natural Recreation Forest',
             'Caribbean Bay',
             'Korean Folk Village']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/종혁/경기/용인농촌테마파크.jpg',
                 './img/종혁/경기/용인자연휴양림.jpg',
                 './img/종혁/경기/캐리비안베이.jpg',
                 './img/종혁/경기/한국민속촌.bmp']
#추천 장소 설명 4개
rec_caption = ['Yongin Rural Theme Park is a large-scale comprehensive experience facility suitable for rural and rural characteristics considering the connection with surrounding tourism resources.',
               "Yongin Natural Recreation Forest, created by Yongin-si, Gyeonggi-do, at the foot of Jeonggwangsan Mountain in Mohyeon-eup, is a stay-type rest area with accommodations, trails, and children's playgrounds with beautiful natural scenery.",
               "It is a water park with indoor and outdoor facilities including wave pools, running water pools, and children's play areas.",
               'It is a folk museum that introduces traditional Korean houses and customs, with restaurants and theme parks.']
# 관광지 Image
image1 = './img/종혁/경기/에버랜드.jpg'
#Wordcloud
image2 = './img/종혁/경기/에버랜드 워드클라우드.png'
#파이차트 경로
data = ('./data/경기/에버랜드.csv')
#Positive 개수
pos = 474
#Negative 개수
neg = 264
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/종혁/경기/에버랜드 그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab1, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(화담숲)-------------------------
#관광지명
name = list[1]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%ED%99%94%EB%8B%B4%EC%88%B2/data=!4m15!1m8!3m7!1s0x357caab1b451d903:0xf04be54b008265c9!2z7ZmU64u07Iiy!8m2!3d37.3412584!4d127.2892037!10e1!16s%2Fg%2F119w13skb!3m5!1s0x357caab1b451d903:0xf04be54b008265c9!8m2!3d37.3412584!4d127.2892037!16s%2Fg%2F119w13skb?authuser=0&entry=ttu'
#관광지 소개 글
intro = '''
It is an arboretum where you can feel spring flowers and autumn leaves in a garden surrounded by forests while walking along a quiet trail.
'''
#추천 장소 4곳
rec_place = ['Pocheon Art Valley',
             'Byeokcho Arboretum',
             'Namhansanseong Fortress',
             'Suwon Hwaseong']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/종혁/경기/포천아트밸리.jpg',
                 './img/종혁/경기/벽초지수목원.jpg',
                 './img/종혁/경기/남한산성.jpg',
                 './img/종혁/경기/수원화성.jpg']
#추천 장소 설명 4개
rec_caption = ['It is an old granite quarry, a complex cultural space with outdoor statues, lakes, and concert stages.',
               'It is a lush park with European and Asian themed gardens, with pavilions, ponds, and willow trees.',
               'There is Namhansanseong Provincial Park with Namhansanseong Fortress, one of the four fortresses that protected Hanyang in the past.',
               "An 18th-century fortification with the city's ancient walls and old structures remaining, it leads from here to the Old Town."]
# 관광지 Image
image1 = './img/종혁/경기/화담숲.png'
#Wordcloud
image2 = './img/종혁/경기/화담숲 워드클라우드.png'
#파이차트 경로
data = './data/경기/화담숲.csv'
#Positive 개수
pos = 291
#Negative 개수
neg = 196
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/종혁/경기/화담숲 그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab2, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(서울랜드)-------------------------
#관광지명
name = list[2]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%84%9C%EC%9A%B8%EB%9E%9C%EB%93%9C/data=!3m1!4b1!4m6!3m5!1s0x357ca0a1c64c4cdb:0x5225b2032101891a!8m2!3d37.4341563!4d127.0201267!16s%2Fm%2F0h3tjxq?authuser=0&entry=ttu'
#관광지 소개 글
intro = '''
Seoul Land, which has the title of Korea's first amusement park, has established itself as a representative theme park in Korea upon its opening. It is located about 30 minutes from Seoul Station and Myeongdong Station, so transportation is convenient, and nearby Seoul Grand Park's Dong and Botanic Gardens, Forest Baths, and National Museum of Modern and Contemporary Art are widely loved as Korea's representative tourist destination.
'''
#추천 장소 4곳
rec_place = ['Seoul Grand Park',
             "Seoul Children's Grand Park",
             'First Garden',
             'Daebudo Island']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/종혁/경기/서울대공원.jpg',
                 './img/종혁/경기/어린이대공원.jpg',
                 './img/종혁/경기/퍼스트가든.bmp',
                 './img/종혁/경기/대부도.jpg']
#추천 장소 설명 4개
rec_caption = ['The zoo has about 3,000 animals and has access to rose gardens, art galleries, and theme parks.',
               "Children's Grand Park opened on Children's Day on May 5, 1973. It is 56,552㎡ and consists of green spaces with green forests and blue grass, so it serves as a citizen's park as a resting and cultural space for children as well as youth and ordinary citizens.",
               'It is a large-scale complex cultural facility located in Paju-si, Gyeonggi-do.',
               'It is a small island in the Yellow Sea with trails, fishing grounds, and beautiful beaches.']
# 관광지 Image
image1 = './img/종혁/경기/서울랜드.bmp'
#Wordcloud
image2 = './img/종혁/경기/서울랜드 워드클라우드.png'
#파이차트 경로
data = './data/경기/서울랜드.csv'
#Positive 개수
pos = 187
#Negative 개수
neg = 94
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/종혁/경기/서울랜드 그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab3, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(니지모리스튜디오)-------------------------

#관광지명
name = list[3]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EB%8B%88%EC%A7%80%EB%AA%A8%EB%A6%AC%EC%8A%A4%ED%8A%9C%EB%94%94%EC%98%A4/data=!4m14!1m7!3m6!1s0x357cdaf9f14058c3:0xad0735e9ed954a20!2z64uI7KeA66qo66as7Iqk7Yqc65SU7Jik!8m2!3d37.879315!4d127.092758!16s%2Fg%2F11sjpgknyp!3m5!1s0x357cdaf9f14058c3:0xad0735e9ed954a20!8m2!3d37.879315!4d127.092758!16s%2Fg%2F11sjpgknyp?authuser=0&entry=ttu'
#관광지 소개 글
intro = '''
Nijimori Studio, located in Dongducheon, Gyeonggi Province, is more like Japan than Japan, and is a film set that perfectly reproduces the villages of the Edo period in Japan.
'''
#추천 장소 4곳
rec_place = ['Daebudo Island',
             'Ludensia',
             'Byeokcho Arboretum',
             'First Garden']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/종혁/경기/대부도.jpg',
                 './img/종혁/경기/루덴시아.jpg',
                 './img/종혁/경기/벽초지수목원.jpg',
                 './img/종혁/경기/퍼스트가든.bmp']
#추천 장소 설명 4개
rec_caption = ['It is a small island in the Yellow Sea with trails, fishing grounds, and beautiful beaches.',
               'Ludensia, called the Alps of Yeoju, is a European-style theme park that provides new cultural experiences based on inspiration and fun.',
               'It is a lush park with European and Asian themed gardens, with pavilions, ponds, and willow trees.',
               'It is a large-scale complex cultural facility located in Paju-si, Gyeonggi-do.']

# 관광지 Image
image1 = './img/종혁/경기/니지모리스튜디오.jpg'
#Wordcloud
image2 = './img/종혁/경기/니지모리스튜디오 워드클라우드.png'
#파이차트 경로
data = './data/경기/니지모리스튜디오.csv'
#Positive 개수
pos = 1427
#Negative 개수
neg = 652
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/종혁/경기/니지모리스튜디오 그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab4, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(한국민속촌)-------------------------

#관광지명
name = list[4]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%ED%95%9C%EA%B5%AD%EB%AF%BC%EC%86%8D%EC%B4%8C/data=!3m1!4b1!4m6!3m5!1s0x357b5aa55e3c2351:0x3e682538e0a196eb!8m2!3d37.258939!4d127.1181126!16zL20vMGc0M25j?authuser=0&entry=ttu'
#관광지 소개 글
intro = '''
It is a folk museum that introduces traditional Korean houses and customs, with restaurants and theme parks.
'''
#추천 장소 4곳
rec_place = ['Yongin Rural Theme Park',
             'Yongin Natural Recreation Forest',
             'Everland',
             'Café Street in Bojeong-dong']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/종혁/경기/용인농촌테마파크.jpg',
                 './img/종혁/경기/용인자연휴양림.jpg',
                 './img/종혁/경기/에버랜드.jpg',
                 './img/종혁/경기/보정동 카페거리.jpg']
#추천 장소 설명 4개
rec_caption = ['Yongin Rural Theme Park is a large-scale comprehensive experience facility suitable for rural and rural characteristics considering the connection with surrounding tourism resources.',
               "Yongin Natural Recreation Forest, created by Yongin-si, Gyeonggi-do, at the foot of Jeonggwangsan Mountain in Mohyeon-eup, is a stay-type rest area with accommodations, trails, and children's playgrounds with beautiful natural scenery.",
               'It is a theme park that provides a pleasant rest and joy with various seasonal festivals, attractions, animals, and plants.',
               'Pretty cafes are gaining popularity along the square-shaped residential alley. The Café Street in Bojeong-dong is impressive in its unique and exotic appearance as if it were in a small village in a foreign country in an alley harmonized with nature.']
# 관광지 Image
image1 = './img/종혁/경기/한국민속촌.bmp'
#Wordcloud
image2 = './img/종혁/경기/한국민속촌 워드클라우드.png'
#파이차트 경로
data = './data/경기/한국민속촌.csv'
#Positive 개수
pos = 267
#Negative 개수
neg = 197
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/종혁/경기/한국민속촌 그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab5, name, googlelink, intro, image1, image2, data, pos, neg, image3)