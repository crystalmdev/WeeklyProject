import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
st.header('Jeonbuk')
list = ['Jeonju Zoo',
        'Gyeonggijeon',
        'Jeonju Hanok Village',
        'Gyeongam-dong Railway Village',
        'Jeonju Arboretum of Korea Expressway Corporation']
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

# --------------------------(전주동물원)-------------------------

#관광지명
name = list[0]
#관광지 구글 링크
googlelink = 'https://www.google.co.kr/maps/place/%EC%A0%84%EC%A3%BC%EB%8F%99%EB%AC%BC%EC%9B%90/data=!3m1!4b1!4m6!3m5!1s0x3570232086e07ab1:0xa5407158c9003e98!8m2!3d35.8551475!4d127.1443503!16s%2Fg%2F1tff5htv?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
Jeonju Zoo opened in June 1978, with more than 100 species of animals and a variety of seasonal plants growing. 
Jeonju Zoo consists of the forest of birds, the forest of beasts, the forest of jannabi, the forest of herbivores, the forest of species conservation, and the forest of grasslands. 
In the forest of birds, the behavior and food activities of animals can be observed without any obstruction of vision at observation posts such as mallards, herons, and pelicans. 
The forest of predators has bears and lion leopards, and the forest of jannabi has squirrel monkeys, egg-tailed lemurs, and the forest of herbivores includes llamas, flower deer, and zebras. 
Wolves and tigers can be seen in the forest of species conservation, and elephants, hippos, ostriches, kangaroos, and large rhinos in the forest of grasslands.'''
#추천 장소 4곳
rec_place = ['Gyeonggijeon',
             'Jeonju Hanok Village',
             'Omokdae',
             'Jaman Mural Village']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/종혁/전북/경기전.jpg',
                 './img/종혁/전북/전주한옥마을.jpg',
                 './img/종혁/전북/오목대.jpg',
                 './img/종혁/전북/자만벽화마을.jpg']
#추천 장소 설명 4개
rec_caption = ['Built in 1410, this famous temple has a museum featuring historical exhibits and portraits of kings.',
               'It is a cultural village with traditional hanok, calligraphy museum, and traditional liquor museum.',
               'There is a monument honoring Taejo Lee Seong-gye as an observation deck at the top of a hill overlooking Hanok Village.',
               'It is a village with various cartoon-style murals painted on houses and narrow alleys on the hill.']
# 관광지 Image
image1 = './img/종혁/전북/전주동물원.jpg'
#Wordcloud
image2 = './img/종혁/전북/전주동물원 워드클라우드.png'
#파이차트 경로
data = './data/전북/전주동물원.csv'
#Positive 개수
pos = 105
#Negative 개수
neg = 51
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/종혁/전북/전주동물원 그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab1, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(경기전)-------------------------
#관광지명
name = list[1]
#관광지 구글 링크
googlelink = 'https://www.google.co.kr/maps/place/%EC%A0%84%EC%A3%BC%EA%B2%BD%EA%B8%B0%EC%A0%84/data=!3m1!4b1!4m6!3m5!1s0x357023601cf26ae5:0x1f95dfca67044b31!8m2!3d35.8153492!4d127.1497938!16s%2Fg%2F12pgctfmf?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Gyeonggijeon Hall is a building built in the 10th year of King Taejong (1410) to enshrine the portrait of King Taejo, which opened the Joseon Dynasty, or to enshrine Eojin and hold ancestral rites. Eojin concession areas in Jeonju, Gyeongju, and Pyongyang were first called Eoyongjeon Hall, but in the 12th year of King Taejong (1412), they were called Taejojeon Hall, and in the 24th year of King Sejong's reign (1442), Jeonju was called Gyeonggijeon Hall, Gyeongju Jipgyeongjeon Hall, and Pyongyang was called Yeongseonjeon Hall. Gyeonggijeon Hall was destroyed during the reign of Jeong Yu-jae in the 30th year of King Seonjo (1597), but it was rebuilt in the 6th year of King Gwanghaegun (1614). Gyeonggijeon consists of Hamabyeong, a red-colored Hongsalmun, a foreign newspaper, an internal newspaper, and a Jeongjeon Hall dedicated to Eojin.'''
#추천 장소 4곳
rec_place = ['Jeonju Hanok Village',
             'Omokdae',
             'PungNamMun',
             'Jaman Mural Village']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/종혁/전북/전주한옥마을.jpg',
                 './img/종혁/전북/오목대.jpg',
                 './img/종혁/전북/풍남문.jpg',
                 './img/종혁/전북/자만벽화마을.jpg']
#추천 장소 설명 4개
rec_caption = ['It is a cultural village with traditional hanok, calligraphy museum, and traditional liquor museum.',
               'There is a monument honoring Taejo Lee Seong-gye as an observation deck at the top of a hill overlooking Hanok Village.',
               'The south gate of the former Jeonju Eupseong in Jeonju-si, Jeonbuk Special Self-Governing Province. It was designated as a treasure on January 21, 1963.',
               'It is a village with various cartoon-style murals painted on houses and narrow alleys on the hill.']
# 관광지 Image
image1 = './img/종혁/전북/경기전.jpg'
#Wordcloud
image2 = './img/종혁/전북/경기전 워드클라우드.png'
#파이차트 경로
data = './data/전북/경기전.csv'
#Positive 개수
pos = 102
#Negative 개수
neg = 49
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/종혁/전북/경기전 그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab2, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(전주한옥마을)-------------------------
#관광지명
name = list[2]
#관광지 구글 링크
googlelink = 'https://www.google.co.kr/maps/place/%EC%A0%84%EC%A3%BC+%ED%95%9C%EC%98%A5%EB%A7%88%EC%9D%84/data=!3m1!4b1!4m6!3m5!1s0x3570236212eebd4b:0x8ef4be1bc6d0848e!8m2!3d35.8175376!4d127.1520417!16s%2Fg%2F1tc_zclz?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''It is estimated that people began to live in Jeonju about 15,000 years ago. Originally, villages in the form of natural villages were formed at the foot of the mountain, but in 665, when Wansanju was installed during the reign of King Munmu of Silla, the residence moved to the flatland. The people of Jeonju's full-fledged life on the flatland began with the construction of Jeonju Castle.'''
#추천 장소 4곳
rec_place = ['Gyeonggijeon',
             'Omokdae',
             'Jaman Mural Village',
             'PungNamMun']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/종혁/전북/경기전.jpg',
                 './img/종혁/전북/오목대.jpg',
                 './img/종혁/전북/자만벽화마을.jpg',
                 './img/종혁/전북/풍남문.jpg']
#추천 장소 설명 4개
rec_caption = ['Built in 1410, this famous temple has a museum featuring historical exhibits and portraits of kings.',
               'There is a monument honoring Taejo Lee Seong-gye as an observation deck at the top of a hill overlooking Hanok Village.',
               'It is a village with various cartoon-style murals painted on houses and narrow alleys on the hill.',
               'The south gate of the former Jeonju Eupseong in Jeonju-si, Jeonbuk Special Self-Governing Province. It was designated as a treasure on January 21, 1963.']
# 관광지 Image
image1 = './img/종혁/전북/전주한옥마을.jpg'
#Wordcloud
image2 = './img/종혁/전북/전주한옥마을 워드클라우드.png'
#파이차트 경로
data = './data/전북/전주한옥마을.csv'
#Positive 개수
pos = 326
#Negative 개수
neg = 206
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/종혁/전북/전주한옥마을 그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab3, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(경암동철길마을)-------------------------

#관광지명
name = list[3]
#관광지 구글 링크
googlelink = 'https://www.google.co.kr/maps/place/%EA%B2%BD%EC%95%94%EB%8F%99+%EC%B2%A0%EA%B8%B8%EB%A7%88%EC%9D%84/data=!3m1!4b1!4m6!3m5!1s0x35705c605e3bb43f:0xb8a69745e793f8e9!8m2!3d35.9813124!4d126.7354981!16s%2Fg%2F11gfdtfyhq?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Gyeongam-dong Cheolgil Village was completed in 1944 in Gyeongam-dong, Gunsan-si, Jeollabuk-do, and was named after the village around the 2.5 km railroad that connects the Paper Korea factory and Gunsan Station. The origin of the name was that the village formed around the railroad was called Gyeongam-dong Cheolgil Village according to the name of the administrative district where the village was located. In 1944, people began to live around the railroad, which was opened during the Japanese occupation, and in the 1970s, the village was formed naturally. Although trains do not run now, the railroad tracks remain as they are, stimulating modern memories. The Gyeongam-dong Railway was first opened in 1944 during the Japanese occupation to carry newspaper materials. It was called the 'North Line Paper Railway' until the mid-1950s, and after the early 1970s it was called the 'Generation Paper Line' or the 'Sepung Railway', but after the newly acquired company went bankrupt, it is now called the 'Paper Korea Line'. Gyeongam-dong Cheolgil Village is famous for a retro sensibility by recreating the scenery of the 1970s and 1980s. Old houses and shops remain everywhere, so you can feel as if you have traveled back in time. In addition, it sells drawing, dalgona, and ddakji on both sides of the railroad track, and is popular with travelers as there are food and entertainment such as taking pictures in old school uniforms.'''
#추천 장소 4곳
rec_place = ['Seonyudo Beach',
             'Saemangeum Seawall',
             'Zhangjia Island',
             'Gogunsan Islands']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/종혁/전북/선유도해수욕장.jpg',
                 './img/종혁/전북/새만금방조제.webp',
                 './img/종혁/전북/장자도.jpg',
                 './img/종혁/전북/고군산군도.jpg']
#추천 장소 설명 4개
rec_caption = ['Seonyudo Beach is a natural coastal sand dune beach, and it is called Myeongsasimri Beach because of its wide range of transparent and beautiful white sand beaches like glass grains.',
               'It is the longest seawall in the world. It is 33.9 kilometers long in total, which is 1.4 kilometers longer than the 32.5 kilometers of the second-ranked Zawider seawall in the Netherlands.',
               'It is said that Jangjado Island has the shape of a horse and is surrounded by a large mountain that has formed the vein of Seonyudo across the sea, so there are many characters.',
               "It's an archipelago where you can enjoy sand beaches, wooded trails, and boat trips through rock walls."]

# 관광지 Image
image1 = './img/종혁/전북/경암동철길마을.jpg'
#Wordcloud
image2 = './img/종혁/전북/경암동철길마을 워드클라우드.png'
#파이차트 경로
data = './data/전북/경암동철길마을.csv'
#Positive 개수
pos = 132
#Negative 개수
neg = 105
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/종혁/전북/경암동철길마을 그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab4, name, googlelink, intro, image1, image2, data, pos, neg, image3)

# --------------------------(한국도로공사 전주수목원)-------------------------

#관광지명
name = list[4]
#관광지 구글 링크
googlelink = 'https://www.google.co.kr/maps/place/%ED%95%9C%EA%B5%AD%EB%8F%84%EB%A1%9C%EA%B3%B5%EC%82%AC+%EC%A0%84%EC%A3%BC%EC%88%98%EB%AA%A9%EC%9B%90/data=!3m1!4b1!4m6!3m5!1s0x35703c3db0ee5865:0x9bc13f0de6200416!8m2!3d35.8709862!4d127.0549618!16s%2Fg%2F1tdzcww5?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''It is 340,000 square meters in size and has 3,410 species of tree genetic resources. The arboretum operated by the Korea Expressway Corporation supplies trees to restore the natural environment damaged during the construction of the highway, collects various plant species, and uses them as a natural learning center. It conducts research on the preservation, proliferation, distribution of plants, and the development of native plants. The plants owned by the Korea Expressway Corporation arboretum are mainly planted in units of [the family]. In particular, it is convenient to observe as it is divided into general arboretum, rock garden, herbal garden, wetland garden, wild grass garden, rose garden, Mugunghwa garden, Jukrimwon, textbook garden, southern garden, glass greenhouse, and mooring garden.'''
#추천 장소 4곳
rec_place = ['Daeah Arboretum',
             'Jeonju Hanok Village',
             'Gyeonggijeon',
             'Jeonju Hyanggyo']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/종혁/전북/대아수목원.jpg',
                 './img/종혁/전북/전주한옥마을.jpg',
                 './img/종혁/전북/경기전.jpg',
                 './img/종혁/전북/전주향교.jpg']
#추천 장소 설명 4개
rec_caption = ['It is a cozy resting place with a mineral spring, a shelter, an observatory, a forest data room, and a forest classroom.',
               'It is a cultural village with traditional hanok, calligraphy museum, and traditional liquor museum.',
               'Built in 1410, this famous temple has a museum featuring historical exhibits and portraits of kings.',
               'It is a Joseon-era educational facility with several buildings, surrounded by giant ginkgo trees.']
# 관광지 Image
image1 = './img/종혁/전북/한국도로공사 전주수목원.jpg'
#Wordcloud
image2 = './img/종혁/전북/한국도로공사 전주수목원 워드클라우드.png'
#파이차트 경로
data = './data/전북/한국도로공사 전주수목원.csv'
#Positive 개수
pos = 93
#Negative 개수
neg = 36
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/종혁/전북/한국도로공사 전주수목원 그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab5, name, googlelink, intro, image1, image2, data, pos, neg, image3)