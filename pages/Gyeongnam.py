import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.header('Gyeongnam')
list = ['Geochang Iris Garden', 'Hapcheon Image Theme Park', 'SpaTheSpace', 'Dongpirang Village', 'Skyline Luge Tongyeong']
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
# --------------------------(거창창포원)-------------------------

#관광지명
name = list[0]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EA%B1%B0%EC%B0%BD+%EC%B0%BD%ED%8F%AC%EC%9B%90/data=!3m1!1e3!4m10!1m2!2m1!1z6rGw7LC97LC97Y-s7JuQ!3m6!1s0x356f9fdc720242a3:0x4f3242e552e16b1d!8m2!3d35.6544801!4d127.9399841!15sCg_qsbDssL3ssL3tj6zsm5CSAQ9lY29sb2dpY2FsX3BhcmvgAQA!16s%2Fg%2F11h4mkhv8z?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
            Geochang Iris Garden is located in Wolpyeong-ri, Namsang-myeon, and was located in a submerged area when the Hapcheon Dam was built in 1988.
    This is the place where farmers have been growing rice.
    In Geochang-gun, an ecological garden that matches the waterside scenery of the Hwanggang River, a national river, was created to reduce agricultural pollution sources.
    Geochang Iris Garden was created to protect river water quality and revitalize the local economy through tourism resources.
    Iris is a plant that purifies water and has the traditional custom and practicality of washing one's hair on Danot Day.
    Iris has a beautiful appearance, as its name comes from the meaning of 'blooming more beautiful flowers than irises.'
    It is a very beautiful flower.
    In the spring, more than 1 million irises planted form a beautiful colony, and in the summer, the theme is lotus, water lily, and hydrangea.
    There are four seasons with the theme of chrysanthemums and maple leaves in the fall, and silver grass and reeds around the tropical botanical garden, reservoir, and wetlands in the winter.
        '''
#추천 장소 4곳
rec_place = ['Suseungdae Tourist Site', 'Baekdu Mountain Cheonji Hot Springs', 'Gyeongsangnam-do Arboretum', 'jeodo-island']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/인화/수승대관광지.jpg', './img/인화/백두산천지온천.jpg', './img/인화/경남수목원.jpg', './img/인화/저도.jpg']
#추천 장소 설명 4개
rec_caption = ['- Auto camping site 14:00 ~ 13:00 the next day \
                - 2nd auto camping site 14:00 ~ 13:00 the next day \
                - Campground 12:00~Next day 11:00 \
                - Sledding range 10:00~17:00 (Facility maintenance 13:00~14:00)',
                'Weekdays 05:30~20:30\
                Weekends and public holidays 05:30~21:30\
                ※ Entry closes 1 hour before',
                'Fee: Adults: 1,500 won (groups 1,200 won) / Students/Military: 1,000 won (groups 800 won) / Children: 500 won (groups 400 won) ※ Groups of 30 or more\
                Operating hours: Summer season (March to October) 09:00 ~ 18:00 / Winter season (November to February) 09:00 ~ 17:00\
                Parking information: Free',
                'Cruise ship contact information - Geoje Jeodo Cruise Co., Ltd. ☎ 055-636-7033/3002, website http://www.jeodo.co.kr']
# 관광지 Image
image1 = './img/인화/거창창포원.jpg'
#Wordcloud
image2 = './img/인화/거창창포원 워드클라우드.png'
#파이차트 경로
data = 'data/경남/거창창포원.csv'
#Positive 개수
pos_cnt = 40
#Negative 개수
neg_cnt = 11
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/인화/거창창포원그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab1, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# --------------------------(합천영상테마파크)-------------------------
#관광지명
name = list[1]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%ED%95%A9%EC%B2%9C+%EC%98%81%EC%83%81%ED%85%8C%EB%A7%88%ED%8C%8C%ED%81%AC/data=!3m2!1e3!4b1!4m6!3m5!1s0x356f0caef684dd8f:0x75ddd9e6a207e5b4!8m2!3d35.5492109!4d128.07312!16s%2Fg%2F1vzg040z?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
         Hapcheon Film Theme Park, built in 2004, is Korea’s best specialized period piece set from the 1920s to the 1980s.
    This open set is the best filming set in the country where 190 movies, drama advertisements, music videos, and other various video works were filmed.
    Recently, a 150,000㎡ building was built behind the video theme park.
    The nation's best bonsai park and garden theme park has opened.
    Along with the main building, the Blue House filming set.
    A bonsai greenhouse, ecological forest experience center, and wood culture experience center have been created.
    Both adults and children can enjoy being in nature. In addition, in order to attract dramas and movies, writers, PDs, film directors, and screenwriters from broadcasting stations across the country are encouraged to participate.
    By actively promoting the advantages of video theme parks,
    In planning and producing future works,
    To actively utilize Hapcheon Film Theme Park
    We plan to provide support.
        '''
#추천 장소 4곳
rec_place = ['Maritime Filming Location', 'Sancheong Hwangmaesan Mountain', 'Thousand Buddha Tower', 'Hill of Wind']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/인화/해양드라마.jpg', './img/인화/황매산.jpg', './img/인화/천불천탑.jpg', './img/인화/바람의언덕.jpg']
#추천 장소 설명 4개
rec_caption = ['The marine drama set is a travel destination that takes you back to the Gaya period in a time machine.\
                Operating hours: 09:00~18:00 Summer season 09:00~17:00 Winter season',
                'The Hwangmaesan Azalea Festival will be held from 2024.04.27 to 2024.05.12.',
                '10,000 won (wish ribbon / once a year)',
                'It was the filming location for the TV dramas "The Painter of Eve" (2003), "Carousel" (2004), and the movie "Palm Forest" (2005).']
# 관광지 Image 1
image1 = './img/인화/합천영상테마파크.jpg'
#Wordcloud Image 2
image2 = './img/인화/합천영상테마파크 워드클라우드.png'
#파이차트 경로
data = 'data/경남/합천영상테마파크.csv'
#Positive 개수
pos_cnt = 42
#Negative 개수
neg_cnt = 30
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/인화/합천영상테마파크그래프.png'
#영어 후기
# nice place to go to refreshing

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab2, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)


# --------------------------(스파더스페이스)-------------------------
#관광지명
name = list[2]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%8A%A4%ED%8C%8C%EB%8D%94%EC%8A%A4%ED%8E%98%EC%9D%B4%EC%8A%A4/data=!3m2!1e3!4b1!4m6!3m5!1s0x356f292357b3b50f:0x144321ad5b661382!8m2!3d35.1306029!4d128.5612855!16s%2Fg%2F11kjlj8qvs?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
        A complex space where you can do everything to rest and recharge
    Hot springs filled with luxury prepared by top experts
    Spider Space is a premium complex healing care center located in Yusan, Changwon. Hot spring and hot spring water infinity pool in a vast space of 6,500 pyeong
    Fitness center, golf, food, coffee, relaxation
    Enjoy it all at once.
    Spider Space is a multi-use facility, and to protect water quality and maintain a clean environment, the following food and items are prohibited. We ask for your cooperation.
    We strive to provide a pleasant environment by prioritizing safety and hygiene.
    Lactic acid hot springs refer to slightly alkaline mineral hot springs containing a large amount of calcium, sodium, etc., and lactic acid hot springs are already becoming known to more people in various countries in Europe and the United States due to the development of medical science called “medical spa” as a preventative medicine and disease treatment. do.
    How about taking the time to relieve your fatigue while treating various ailments in the Yusan hot springs with clear and clean water??
        '''
#추천 장소 4곳
rec_place = ['Gwangam Beach', 'Mageumsan Wontang Boyang Hot Springs', 'Baekdu Mountain Cheonji Hot Springs', 'Lotte Water Park']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/인화/광암해수욕장.jpg', './img/인화/마금산온천.jpg', './img/인화/백두산천지온천.jpg', './img/인화/롯데워터파크.jpg']
#추천 장소 설명 4개
rec_caption = ['Gwangam Beach, the only beach in Changwon City\
                Admission fee: Free',
                'As the origin of Mageumsan Hot Springs (Bukmyeon Hot Springs), it is a hot spring with a long history, with records remaining in historical books including the Joseon Dynasty\'s Sejong Annals of Geography (1453) and Dongguk Yeoji Seungnam (1481).',
                'Gajo Baekdu Mountain Cheonji Hot Springs is a hot spring that preserves the mystery of Baekdu Mountain as the Gajo area reproduces the appearance of Baekdu Mountain Cheonji when viewed from above.',
                'Bomunjeong boasts such beautiful scenery that it was once introduced as "Korea\’s Secret Place" on CNN.\
                Cherry trees and maple trees are planted around the octagonal pavilion and two ponds,\
                making it a place to enjoy the scenery in any season.',
               'Admission fee [High season]\
                - All-day ticket: Adults 56,000 won / Children 46,000 won\
                - Afternoon ticket: Adults 49,000 won / Children 39,000 won\
                [Gold Season]\
                - All-day ticket: Adults 75,000 won / Children 61,000 won\
                - Afternoon ticket: Adults 68,000 won / Children 56,000 won']
# 관광지 Image 1
image1 = './img/인화/스파더스페이스.jpg'
#Wordcloud Image 2
image2 = './img/인화/스파더스페이스 워드클라우드.png'
#파이차트 경로
data = 'data/경남/스파더스페이스.csv'
#Positive 개수
pos_cnt = 89
#Negative 개수
neg_cnt = 57
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/인화/스파더스페이스그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab3, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)

# --------------------------(동피랑벽화마을)-------------------------

#관광지명
name = list[3]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EB%8F%99%ED%94%BC%EB%9E%91+%EB%B2%BD%ED%99%94%EB%A7%88%EC%9D%84/data=!3m1!1e3!4m10!1m2!2m1!1z64-Z7ZS8656R67K97ZmU66eI7J2E!3m6!1s0x356ec7152e48d9a9:0xaddbae2cac707f35!8m2!3d34.8456408!4d128.4276137!15sChXrj5ntlLzrnpHrsr3tmZTrp4jsnYRaGiIY64-ZIO2UvOuekSDrsr3tmZQg66eI7J2EkgESdG91cmlzdF9hdHRyYWN0aW9u4AEA!16s%2Fg%2F11bttqgjxq?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
        The name ‘Dongpirang’ was created by combining the words ‘east’ and ‘birang.’ ‘Birang’ is a Tongyeong dialect word for ‘vital’, and it is made by adding only ‘dong’ from the word ‘east’, so people came to call it ‘Dongpirang.’ The Green Tongyeong 21 Promotion Council gathered people nationwide to paint on Dongpirang Road in October 2007. Those people painted pictures all over the village walls, walls, roads, etc., and the seaside hill village was reborn as a painting. Dongpirang Alley has dozens of branches. A village with paintings in every alley and touching the sky. The paintings there are enough to turn the village into a fairyland. Additionally, the Gangguan seascape seen from the village is also worth seeing.
        Tongyeong City initially had a plan to demolish Dongpirang Village and restore Dongporu, the old Jejeongyeong building installed by Chungmugong. In 2007, a civic group called 'Blue Tongyeong 21' opened the 'Dongpirang Coloring - National Mural Contest' in Dongpirang Village under the slogan, "Even a daldongnae can become beautiful if you take care of it." Accordingly, art students from all over the country gathered and began painting murals on old walls in every alley.
        '''
#추천 장소 4곳
rec_place = ['Dipirang','Tongyeong Cable Car',' SKYLINE Luge Tongyeong','Undersea Tunnel']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/인화/디피랑.jpg', './img/인화/통영케이블.jpg', './img/인화/스카이라인루지.jpg', './img/인화/해저터널.jpg']
#추천 장소 설명 4개
rec_caption = ['On a pitch-black night, when a large moon rises in the sky, the erased murals of Mural Village come to life at the top of the mountain! We invite you to the mysterious festival of murals that were liberated from Mt. Nammang’s Dipirang.',
                'The Tongyeong Cable Car installed on Mireuksan Mountain in Tongyeong is Korea\'s only bi-cable automatic circulation gondola system installed using the latest Swiss technology, and its length of 1975m is the longest among cable cars for general tourists in Korea.',
                'Many people gather to ride sleds in Tongyeong, a southern city full of warm spring energy. This is to ride the ‘Skyline Luge’, which can only be enjoyed in 6 places around the world. Luge is an amusement facility where you ride a specially designed cart without a special power device and run on a track using only the slope of the ground and gravity.',
                'The Tongyeong Undersea Tunnel is an undersea tunnel built to connect Tongyeong and Mireukdo Island. It is the first underwater tunnel in Asia, built over a period of 1 year and 4 months from 1931 to 1932, and is 483m long, 5m wide, and 3.5m high.']
# 관광지 Image 1
image1 = './img/인화/동피랑.jpg'
#Wordcloud Image 2
image2 = './img/인화/동피랑벽화마을 워드클라우드.png'
#파이차트 경로
data = 'data/경남/동피랑벽화마을.csv'
#Positive 개수
pos_cnt = 90
#Negative 개수
neg_cnt = 38
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/인화/동피랑벽화마을그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab4, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)
# --------------------------(스카이라인 루지 통영)-------------------------

#관광지명
name = list[4]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%8A%A4%EC%B9%B4%EC%9D%B4%EB%9D%BC%EC%9D%B8%EB%A3%A8%EC%A7%80+%ED%86%B5%EC%98%81/data=!3m2!1e3!4b1!4m6!3m5!1s0x356ec7605ac895f5:0xb6f0ed7f4a2a9932!8m2!3d34.8240977!4d128.4237574!16s%2Fg%2F11c1_vdmtl?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''
         Many people gather to ride sleds in Tongyeong, a southern city full of warm spring energy. This is to ride the ‘Skyline Luge’, which can only be enjoyed in 6 places around the world. Luge is an amusement facility where you ride a specially designed cart without a special power device and run on a track using only the slope of the ground and gravity. It was first invented in Rotorua, New Zealand, and opened in Tongyeong as the 6th location, following New Zealand (2 locations), Canada (2 locations), and Singapore (1 location).
    As soon as it opened in February 2017, it was so crowded with users that people had to wait in line for more than two hours on weekends. Still, luge’s popularity does not fade. There are relatively few users early on weekend mornings or on weekdays, so if you want to use it leisurely, it is best to avoid crowded times.
    Skyline Luge has the same name as the winter sport luge, but it is much safer and easier. You can think of it as a sled with steering wheels and wheels that can control direction. The operation is as simple as a sled, so even children taller than 110cm can ride on their own. Children between 85 and 110 cm tall must be accompanied by a guardian.
        '''
#추천 장소 4곳
rec_place = ['Geoje Panoramic Cable Car','Tongyeong Cable Car','Sacheon Sea Cable Car','Hadong Cable Car']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/인화/거제케이블.jpg', './img/인화/통영케이블.jpg', './img/인화/사천케이블.jpg', './img/인화/하동케이블.jpg']
#추천 장소 설명 4개
rec_caption = ['Geoje Panorama Cable Car is a 1.56km cable car that connects Hakdong Pass to the summit of Nojasan Mountain.\
                From the upper observatory, you can enjoy a 360-degree view of Nojasan Mountain and Dadohae without boundaries.',
                'The Tongyeong Cable Car installed on Mireuksan Mountain in Tongyeong is Korea\'s only bi-cable automatic circulation gondola system installed using the latest Swiss technology, and its length of 1975m is the longest among cable cars for general tourists in Korea.',
                'Sacheon Sea Cable Car is famous as Korea\'s first cable car that connects the sea, islands, and mountains, allowing you to enjoy both the mountains and the sea at the same time.',
                'The cable car is the best landmark in Hadong, offering a panoramic view of the pristine Namhae Hallyeohaesang National Park. A trail has been created near the summit of Geumosan Mountain, allowing visitors to enjoy nature through leisurely walks and attractions.']
# 관광지 Image 1
image1 = './img/인화/스카이라인루지.jpg'
#Wordcloud Image 2
image2 = './img/인화/스카이라인 루지 통영 워드클라우드.png'
#파이차트 경로
data = 'data/경남/스카이라인 루지 통영.csv'
#Positive 개수
pos_cnt = 90
#Negative 개수
neg_cnt = 38
#Bigram NetworkX Graph 이미지 첨부
image3 = './img/인화/스카이라인루지통영그래프.png'

#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab5, name, googlelink, intro, image1, image2, data, pos_cnt, neg_cnt, image3)



