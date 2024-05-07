import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
st.header('Ulsan️')
list = ['Ganwoljae🗿', 'Wow Zoo🐻', 'Yeongnam Alps⛰️',
        'Taehwagang Donggulpia🦇', 'Amethyst Cavern Park💎']
tab1, tab2, tab3, tab4, tab5 = st.tabs(list)

def tabs(tabnum, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3):
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
        with st.container(height=270):
            st.markdown(intro)

        st.divider()

        col1, col2 = st.columns([1,1])

        with col1:
            st.markdown('**Image**')
            st.image(Image.open(image1),
                     use_column_width=True)

        with col2:
            st.markdown('**You may also like 😃**')
            row1 = st.columns(2)
            row2 = st.columns(2)
            for i, col in enumerate(row1 + row2):
                tile = col.expander(rec_place[i])
                tile.image(Image.open(rec_place_img[i]),
                     caption=rec_caption[i],
                     use_column_width=True)

        st.divider()

        col1, col2 = st.columns([1,1])

        with col1:
            st.markdown('💡**Highlights of the Destination**')
            st.text('(Top Keywords based on Korean blog)')
            st.image(Image.open(image2),
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

        total_count = pos_cnt + neg_cnt
        st.markdown(f'🔍The reviews from korean visitors are generally like this (**{total_count} reviews**)')
        positive_ratio = (pos_cnt / total_count) * 100
        negative_ratio = (neg_cnt / total_count) * 100

        positive_icon = '😊'  # 긍정을 나타내는 이모티콘
        negative_icon = '😞'  # 부정을 나타내는 이모티콘

        positive_display = f'{positive_icon} {positive_ratio:.0f}%'
        negative_display = f'{negative_icon} {negative_ratio:.0f}%'

        st.subheader(f'**:green[{positive_display}]** **:red[{negative_display}]**')

        with st.expander('Review text positive/negative word distribution (Bigram NetworkX Graph)'):
            st.image(Image.open(image3), use_column_width=True)

# 간월재--------------------------------------------------------------------------------------

#관광지명
name = list[0]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/Ganwoljae+Flame+Grass+Road/data=!4m6!3m5!1s0x3566216c02af50c5:0x1ea30f5c60d66d81!8m2!3d35.5477127!4d129.0452648!16s%2Fg%2F1tjgy76h?entry=ttu'
#관광지 소개 글
intro = '''Ganwoljae is a place where the ridges of Mt. Sinbulsan and Mt. Ganwolsan, known as the "Alps of Yeongnam," 
        meet. It's famous for its autumn silver grass fields. Feeling the cool breeze, one can gaze upon the exotic 
        landscape of Ganwoljae and forget the exhaustion of daily life. The easiest way to reach Ganwoljae is via the 
        "Deer Farm Course," a relatively flat path of about 6km, making it accessible even for beginners unfamiliar 
        with hiking.'''
#추천 장소 4곳
rec_place = ['Silver Grass Plain', 'Yeongchuksan Mountain', 'Sinbulsan Falls National Recreational Forest', 'Jujeon Pebble Beach']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/다율/억새평원.jpg', './img/다율/영축산.jpg', './img/다율/폭포.jpg', './img/다율/주전몽돌해변.jpg']
#추천 장소 설명 4개
rec_caption = ["Ulju County Park, is the nation's premier silver grass plain, renowned for its beauty.",
               "Stunning scenery, renowned hiking spot in Gajisan Provincial Park.",
               "Silver grass fields and refreshing waterfalls make it a relaxing forest retreat.",
               "Black pebble beach with soothing waves"]
# 관광지 Image
image1 = './img/다율/간월재.jpg'
#Wordcloud
image2 = './img/다율/간월재 워드클라우드.png'
#파이차트 경로
data = 'data/울산/간월재.csv'
#Positive 개수
pos_cnt = 31
#Negative 개수
neg_cnt = 23
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/다율/간월재그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab1, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# 와우쥬-----------------------------------------------------------------------------------------------
#관광지명
name = list[1]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/Waujyu/data=!4m10!1m2!2m1!1z7JmA7Jqw7KWs!3m6!1s0x35662deb295e3d23:0xbea6710b98324a76!8m2!3d35.5372968!4d129.25799!15sCgnsmYDsmrDspaySAQN6b2_gAQA!16s%2Fg%2F11g0kjlk6q?entry=ttu'
#관광지 소개 글
intro = '''Wow Zoo is a unique cafe in Ulsan Metropolitan City, where you can interact with animals in the heart of 
        the city. It's a special space where you can touch, breathe, and bond with animals freely living in the cafe. 
        You can encounter various animals like desert foxes, red foxes, squirrel monkeys, owls, and reptiles, and even 
        touch snakes. It's a place where you can see and touch animals that are not easily found elsewhere, like 
        alpacas from South America, and experience the preciousness of life firsthand.'''
#추천 장소 4곳
rec_place = ['Canyon Park', 'Ulsan Grand Park Zoo', 'Ulsan Theme Botanical Arboretum', 'Gangdong Pebble Beach']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/다율/캐니언파크.png', './img/다율/울산대공원.jpg',
                 './img/다율/울산테마식물원.jpg', './img/다율/강동몽돌해변.jpg']
#추천 장소 설명 4개
rec_caption = ["An indoor zoo where visitors can experience feeding animals.",
               "A place to learn about the beauty of animals and nature while fostering a love for them.",
               "An eco-friendly arboretum utilizing natural ecological forests.",
               "A beautiful seaside with cute pebbles and clear blue waters."]
# 관광지 Image
image1 = './img/다율/와우쥬.jpg'
#Wordcloud
image2 = './img/다율/와우쥬 본점 워드클라우드.png'
#파이차트 경로
data = 'data/울산/와우쥬본점.csv'
#Positive 개수
pos_cnt = 32
#Negative 개수
neg_cnt = 22
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/다율/와우쥬본점그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab2, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# 영남알프스-----------------------------------------------------------------------------------------------
#관광지명
name = list[2]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/Jangtaesan+Recreational+Forest/data=!3m1!4b1!4m6!3m5!1s0x356553a079f05293:0xf6814125580cd530!8m2!3d36.2187201!4d127.3401569!16s%2Fg%2F121gv9zc?entry=ttu'
#관광지 소개
intro = '''Yeongnam Alps is formed by mountains with an elevation of over 1,000 meters centered on Gajisan Mountain, 
        which spans Ulsan, Miryang, Yangsan, Cheongdo and Gyeongju, boasting beautiful terrains and landscape. Its 
        name originated from how it is comparable to the beauty and grandeur of the Alps in Europe. 
        
        The total area of Yeongnam Alps is around 255 ㎢, and it is a mountain tourist attraction connected by nine 
        mountains including Sinbulsan, one of the 100 greatest mountains of Korea. Though its beauty is famous 
        regardless of the season, it is completely covered with silver grass every fall to boast a fantastic view, 
        attracting countless hikers from all over the country.
        
        Gorgeous nature is not the only aspect luring people to Yeongnam Alps; there are also many things to enjoy, 
        from mountain biking (MTB), that fearlessly runs through the mountain trails, valleys, gravel roads and 
        bushes to paragliding by which you get a complete panoramic view of the Yeongnam Alps. The region currently 
        looks to establish the Sky Silver Grass Trail, which aims to utilize existing trails to the greatest extent 
        possible, and to restore silver grass colonies, and it also hosts low-carbon sports events such as the 
        Yeongnam Alps Marathon and MTB Challenge Competition.
'''
#추천 장소 4곳
rec_place = ['Cheonhwangsan', 'GaJi Mountain Provincial Park', 'Jakcheongjeong Valley', 'Jinha Beach']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/다율/천황산.jpg', './img/다율/가지산.jpg', './img/다율/작천정계곡.jpg', './img/다율/진하.jpg']
#추천 장소 설명 4개
rec_caption = ["The central peak of the Yeongnam Alps, Cheonhwangsan (main peak: Sajabong)",
               "A beautiful place with vast silver grass fields exuding the atmosphere of autumn",
               "Jakcheongjeong Valley: A picturesque landscape created by clear water and white rocks",
               "A place where body and mind heal amidst gentle waves"]
# 관광지 Image
image1 = './img/다율/영남알프스.jpg'
#Wordcloud
image2 = ('./img/다율/영남알프스 워드클라우드.png')
#파이차트 경로
data = 'data/울산/영남알프스.csv'
#Positive 개수
pos_cnt = 32
#Negative 개수
neg_cnt = 22
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/다율/영남알프스그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab3, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# 태화강동굴피아 -------------------------------------------------------------------------------

#관광지명
name = list[3]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%ED%83%9C%ED%99%94%EA%B0%95%EB%8F%99%EA%B5%B4%ED%94%BC%EC%95%84/data=!3m1!4b1!4m6!3m5!1s0x356632a77370930f:0x4206ea384662f866!8m2!3d35.5449258!4d129.3021944!16s%2Fg%2F11f31x966y?entry=ttu'
#관광지 소개 글
intro = '''Taehwagang Donggulpia has transformed several artificial caves created by the Japanese military during the 
        Japanese colonial period into a tourist attraction, originally intended for storing military supplies. 
        Visitors can catch a glimpse of Ulsan's history and way of life during that era. Outside the caves, there is 
        an artificial falls, and inside, various experiential zones such as the Cave Adventure Zone, Digital Sketch 
        Experience Zone, and Lighting Art Zone offer diverse interactive experiences.
'''
#추천 장소 4곳
rec_place = ['Taehwa River National Garden', 'Taehwa River Silver Grass Field', 'Jangsaengpo Whale Cultural Village',
             'Daewangam Park Suspension Bridge']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/다율/태화강국가정원.jpg', './img/다율/억새군락지.jpg', './img/다율/장생포.jpg', './img/다율/출렁다리.jpg']
#추천 장소 설명 4개
rec_caption = ["A themed garden with six themes located along the Taehwa River in Ulsan",
               "A silver grass field illuminated in golden hues by the setting sun",
               "The only whale-themed cultural tourism facility in Korea",
               "Thrillingly Enjoy the Spectacular View of Daewangam"]
# 관광지 Image
image1 = './img/다율/동굴피아.jpg'
#Wordcloud
image2 = './img/다율/태화강동굴피아 워드클라우드.png'
#파이차트 경로
data = 'data/울산/태화강동굴피아.csv'
#Positive 개수
pos_cnt = 26
#Negative 개수
neg_cnt = 15
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/다율/태화강동굴피아그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab4, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# 자수정동굴나라-------------------------------------------------------------------------------

#관광지명
name = list[4]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps?sca_esv=88efb82a0fd29766&output=search&q=%EC%9E%90%EC%88%98%EC%A0%95%EB%8F%99%EA%B5%B4%EB%82%98%EB%9D%BC&source=lnms&entry=mc&ved=1t:200715&ictx=111'
#관광지 소개 글
intro = '''Amethyst Cavern Park is the largest man-made cave tourist attraction in Korea, where one of the five 
        jewels of the World, amethyst, was mined. Connected like a labyrinth, the cave is 2.5 kilometers long and 
        fills an area of approximately 15,000 square meters. The average temperature is between 12 and 16 degrees 
        Celsius year round. Visitors can take either the walking tour that goes through a different themed halls or 
        take a boat ride through the cave river. On the second floor of the cave, visitors can see Jurassic World 
        filled with different dinosaurs and character lamps. '''
#추천 장소 4곳
rec_place = ['Ilsan Beach', 'Ulsan Bridge Observatory', 'Myeongseon Island', 'Wishing Mailbox at Ganjeolgot']
#추천 장소 이미지 경로 4개정동진해변
rec_place_img = ['./img/다율/일산해수욕장.jpg', './img/다율/울산대교.jpg', './img/다율/명선도.png', './img/다율/소망우체통.jpg']
#추천 장소 설명 4개
rec_caption = ["A Sea with Diverse Charms",
               "Landmark with a View of Ulsan",
               "A picturesque night view with fantastic media art",
               "A must-see landmark where you'll definitely want to take a photo!"]
# 관광지 Image
image1 = './img/다율/자수정동굴나라.jpg'
#Wordcloud
image2 = './img/다율/자수정동굴나라 워드클라우드.png'
#파이차트 경로
data = 'data/울산/자수정동굴나라.csv'
#Positive 개수
pos_cnt = 75
#Negative 개수
neg_cnt = 40
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/다율/자수정동굴나라그래프.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab5, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)