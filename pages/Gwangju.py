import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
st.header('Gwangju')
list = ['Uncheon Reservoir🌊', 'Solomon Law Park🏛️', 'Mudeungsan Lift Monorail🚡',
        'Gwangju Metropolitan Arboretum🌳', 'Hello Animal🐾']
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

# 운천저수지------------------------------------------------------------------------------------------

#관광지명
name = list[0]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%9A%B4%EC%B2%9C%EC%A0%80%EC%88%98%EC%A7%80/data=!3m1!4b1!4m6!3m5!1s0x357189436d15cebf:0xca6d06318ae09c6f!8m2!3d35.1479357!4d126.8554067!16s%2Fg%2F11thg9pkdd?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''In 1951, it was located in the city center due to the construction of large-scale land 
        development around the reservoir to supply agricultural water to the Marukdong agricultural 
        land and prevent disasters, and upstream water shortages and inflow of sewage turned it into 
        a source of odor and breeding ground for pests, causing various complaints. From 1995, annual 
        projects were carried out to block the inflow of sewage and waste water and supply clean water, 
        resulting in the restoration of the self-purification ability, transforming it into a natural 
        ecological park where various birds fly.'''
#추천 장소 4곳
rec_place = ['Gwangju Stream', 'Sangmu Food Alley', 'Ssangam Park', 'Food Specialty Street in Geumho-dong']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/다율/광주천.jpg',
                 './img/다율/상무지구.png',
                 './img/다율/쌍암.jpg',
                 './img/다율/금호먹거리촌.jpeg']
#추천 장소 설명 4개
rec_caption = ['Recently, Gwangju has become famous for its cherry blossom path, where cherry blossoms bloom first.',
               "Gwangju's culinary hub",
               'Nature and Culture in Gwangju',
               'A food-specialized street densely packed with restaurants located in Geumho-dong']
# 관광지 Image
image1 = './img/다율/운천저수지.jpg'
#Wordcloud
image2 = './img/다율/운천저수지 워드클라우드.png'
#파이차트 경로
data = 'data/광주/운천저수지.csv'
#Positive 개수
pos_cnt = 14
#Negative 개수
neg_cnt = 6
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/다율/운천저수지그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab1, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# 솔로몬-----------------------------------------------------------------------------------------------
#관광지명
name = list[1]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EB%B2%95%EB%AC%B4%EB%B6%80+%EA%B4%91%EC%A3%BC%EC%86%94%EB%A1%9C%EB%AA%AC%EB%A1%9C%ED%8C%8C%ED%81%AC/data=!4m10!1m2!2m1!1z7IaU66Gc66qs66Gc7YyM7YGs!3m6!1s0x35718d6d338d4969:0x304581b592162eaa!8m2!3d35.1892253!4d126.9310181!15sChLshpTroZzrqqzroZztjIztgaySAQp0aGVtZV9wYXJr4AEA!16s%2Fg%2F11v0y4rplm?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Solomon Law Park is a theme park operated by the Ministry of Justice, offering an experiential legal 
        education. Visitors can learn about and experience the law in an easy and entertaining way. The Law Experience 
        Center provides opportunities to experience legislation, investigation, courtrooms, and prisons. The park 
        includes a Law Playground, as well as amenities like a leisure area and a convenience store.'''
#추천 장소 4곳
rec_place = ['Bitgoeul Rural Theme Park', 'Gwangju Family Land',
             'May 18 Democracy Square', 'Gwangju Sajik Park']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/다율/빛고을.jpg',
                 './img/다율/패밀리랜드.jpeg',
                 './img/다율/518-2.jpg',
                 './img/다율/사직공원.jpg']
#추천 장소 설명 4개
rec_caption = ["A space designed to activate local tourism resources and provide relaxation.",
               'A dreamy amusement park filled with love.',
               'The symbol of the democratization movement in South Korea.',
               "A place where people prayed for the country's peace and prosperity."]
# 관광지 Image
image1 = './img/다율/솔로몬.jpg'
#Wordcloud
image2 = './img/다율/광주솔로몬로파크 워드클라우드.png'
#파이차트 경로
data = 'data/광주/광주솔로몬로파크.csv'
#Positive 개수
pos_cnt = 14
#Negative 개수
neg_cnt = 6
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/다율/광주솔로몬로파크그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab2, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# 무등산 리프트&모노레일------------------------------------------------------------------------------------------
#관광지명
name = list[2]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EB%AC%B4%EB%93%B1%EC%82%B0+%EB%A6%AC%ED%94%84%ED%8A%B8%26%EB%AA%A8%EB%85%B8%EB%A0%88%EC%9D%BC/data=!3m1!4b1!4m6!3m5!1s0x35718d4a73ce1865:0xd9b18a98805afd5e!8m2!3d35.1488919!4d126.9473604!16s%2Fg%2F11m_j_nw6h?hl=ko&entry=ttu'
#관광지 소개
intro = '''To use the lift and monorail located at Jisan Park in Gwangju, visitors can purchase a ticket at the ticket 
        office in the convenience store on the first floor and go up to the boarding area on the second floor. Get on 
        the lift with a track length of 745 meters and an operating speed of 12 m/sec and climb for about 20 minutes 
        while enjoying the scenery of Mudeungsan Mountain to arrive at Bitgoeul Station. From here, visitors can 
        transfer to the monorail. Passengers can feel the thrill of riding toward the top on a monorail which can 
        accommodate about 20 people at a time. A spectacular view of Mudeungsan Mountain will unfold in all directions. 
        The view of Gwangju from Palgakjeong Observatory at the end of the monorail is a beautiful sight that visitors 
        to Gwangju must see at least once as it is a famous attraction to enjoy the view of Gwangju.
'''
#추천 장소 4곳
rec_place = ['Jisan Recreation Area', 'Mudeungsan Observation Deck',
             'Mudeungsan National Park', 'Mudeungsan Mountain']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/다율/지산유원지.jpg',
                 './img/다율/전망대.jpg',
                 './img/다율/무등산국립공원.jpg',
                 './img/다율/무등산.jpg']
#추천 장소 설명 4개
rec_caption = ['Experience a unique thrill on Mt. Mudeung!',
               'Top attractions to fully experience and enjoy in Gwangju',
               'The backbone of the Honam region, spanning Gwangju and Jeollanam-do provinces.',
               'Mount Mudeung, where people of all ages can enjoy hiking comfortably without steep slopes.']
# 관광지 Image
image1 = './img/다율/무등산.jpg'
#Wordcloud
image2 = './img/다율/무등산 리프트&모노레일 워드클라우드.png'
#파이차트 경로
data = 'data/광주/무등산 리프트&모노레일.csv'
#Positive 개수
pos_cnt = 25
#Negative 개수
neg_cnt = 24
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/다율/무등산그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab3, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# 광주시립수목원 -------------------------------------------------------------------------------

#관광지명
name = list[3]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EA%B4%91%EC%A3%BC%EC%8B%9C%EB%A6%BD%EC%88%98%EB%AA%A9%EC%9B%90/data=!3m1!4b1!4m6!3m5!1s0x35718ba0c5b69e25:0xea1af5b7bd2addc!8m2!3d35.0900219!4d126.8825582!16s%2Fg%2F11l5p6n4h6?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Gwangju Metropolitan Forest is a park located in Dodong-dong, Nam-gu, Gwangju Metropolitan City. It opened 
        in October 2023 and is a beautiful place where you can encounter nature amidst the city, with diverse plants 
        and trees..
'''
#추천 장소 4곳
rec_place = ['Donggul Cave ', 'Penguin Village Craft Street ', 'Wonyeo Valley', 'Pochung Temple']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/다율/뒹굴동굴.jpg',
                 './img/다율/펭귄마을.jpg',
                 './img/다율/원효계곡.jpg',
                 './img/다율/포충사.jpg']
#추천 장소 설명 4개
rec_caption = ['Japanese colonial-era anti-communist bunkers now historic landmarks.',
               'Retro-themed craft culture experiential tourism site.',
               "Gwangju's top summer retreat: Mt. Mudeung's lush forests and clear streams.",
               'Memorial for Gu Gyeong-myeong, a guerrilla leader who fought in the Battle of Geumsan.']
# 관광지 Image
image1 = './img/다율/시립수목원.jpeg'
#Wordcloud
image2 = './img/다율/광주광역시립수목원 워드클라우드.png'
#파이차트 경로
data = 'data/광주/광주광역시립수목원.csv'
#Positive 개수
pos_cnt = 23
#Negative 개수
neg_cnt = 9
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/다율/광주광역시립수목원그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab4, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# 헬로애니멀-------------------------------------------------------------------------------

#관광지명
name = list[4]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%ED%97%AC%EB%A1%9C%EC%95%A0%EB%8B%88%EB%A9%80%EA%B4%91%EC%A3%BC%EC%A0%90/data=!3m1!4b1!4m6!3m5!1s0x35718c869514c31d:0xbf1b01032cbb8380!8m2!3d35.1484751!4d126.9150982!16s%2Fg%2F11lltqd3m1?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''It is an indoor exotic zoo, housing over 50 small animals including cute reptiles and birds, where visitors 
        can interact closely by listening to explanations from expert caretakers, touching and observing them up close, 
        and even feeding them. While families with children are common visitors, there is also a growing trend of young 
        adults coming for unique dates.'''
#추천 장소 4곳
rec_place = ['Uchi Zoo Park', 'Gwangju Art Street', 'Aqua City', 'Jungmeorijae Pass']
#추천 장소 이미지 경로 4개정동진해변
rec_place_img = ['./img/다율/우치공원.jpg',
                 './img/다율/예술의거리.jpg',
                 './img/다율/아쿠아시티.jpg',
                 './img/다율/중머리재.jpeg']
#추천 장소 설명 4개
rec_caption = ['A place of dreams, hope, and beautiful memories.',
               "Gwangju's cultural street, embracing the arts.",
               'Water play and maritime safety learning hub.',
               "The vast grassy field, dubbed 'Middle Hairline Peak (Seungdubong),' resembles a monk's head."]
# 관광지 Image
image1 = './img/다율/헬로애니멀2.jpg'
#Wordcloud
image2 = './img/다율/헬로애니멀 광주점 워드클라우드.png'
#파이차트 경로
data = 'data/광주/헬로애니멀 광주점.csv'
#Positive 개수
pos_cnt = 7
#Negative 개수
neg_cnt = 6
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/다율/헬로애니멀그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab5, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)