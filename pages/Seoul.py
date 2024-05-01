import streamlit as st
from PIL import Image
import numpy as np # TEST
st.header('Seoul')
list = ['Seoul Botanic Park', 'Lotte World', 'Gyeongbokgung Palace', 'Seokchonhosu Lake', "Seoul Children's Grand Park"]
tab1, tab2, tab3, tab4, tab5 = st.tabs(list)

def tabs(tabnum, name, googlelink, intro, image1, image2, image3):
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
            st.markdown('**Top Keywords about the Destination**')
            st.text('(based on Korean blog reviews)')
            st.image(Image.open(image2),
                     use_column_width=True)
        with col2:
            st.markdown('**스타차트로 변경**')
            st.text('(based on Korean blog reviews)')
            st.image(Image.open(image3),
                     use_column_width=True)

# --------------------------(서울식물원)-------------------------
#관광지명
name = list[0]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%84%9C%EC%9A%B8%EC%8B%9D%EB%AC%BC%EC%9B%90/data=!3m1!1e3!4m10!1m2!2m1!1z7ISc7Jq47Iud66y87JuQ!3m6!1s0x357c9d01503c1eeb:0x947516d30347709a!8m2!3d37.5694332!4d126.8350132!15sCg_shJzsmrjsi53rrLzsm5CSARBib3RhbmljYWxfZ2FyZGVu4AEA!16s%2Fg%2F11hbqpg8n5?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''The Seoul Botanical Garden was created in Magok, the last remaining development site in Seoul, to introduce native plants and horticulture of 12 different cities from around the world and raise ecological awareness in the city. Seoul Botanic Park integrates a botanical garden and a public park, and the area is the size of 70 soccer fields. It serves as a bridgehead and lifelong education institution with the aim of spreading urban garden culture while staying true to its original role as a plant research conservation institution through expanding endangered wild plant habitats, researching the proliferation of species, and developing varieties. The botanical garden is divided into four spaces: Open Forest, Themed Garden, Lake Garden, and Wetland Garden. The main highlight is the Themed Garden that comprises the Botanic Center, Mogok Cultural Hall, and an outdoor themed garden. '''
#추천 장소 4곳
rec_place = ['경복궁', '서울어린이대공원', '청계천', '서울어린이대공원 동물원']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/예시/ltseoul.png', './img/예시/everland.jpeg', './img/예시/gjworld.jpeg', './img/예시/carrbay.jpeg']
#추천 장소 설명 4개
rec_caption = ['theme park located in seoul... etc 기타 간단한 영어 설명 - 번역기 돌려도 됨', 'theme park located in seoul... etc',
               'theme park located in seoul... etc', 'theme park located in seoul... etc']
# 관광지 Image
image1 = './img/수정/서울식물원.jpeg'
#Wordcloud
image2 = './img/인화/대릉원 워드클라우드.png'
#그래프
image3 = './img/예시/graph.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab1, name, googlelink, intro, image1, image2, image3)

# --------------------------(롯데월드 어드밴처)-------------------------
#관광지명
name = list[1]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EB%A1%AF%EB%8D%B0%EC%9B%94%EB%93%9C/data=!3m1!1e3!4m10!1m2!2m1!1z66Gv642w7JuU65OcIOyWtOuTnOuypOyymA!3m6!1s0x357ca5a7250efe81:0x433df2c1fec03b98!8m2!3d37.5111158!4d127.098167!15sChnroa_rjbDsm5Trk5wg7Ja065Oc67Kk7LKYIgOIAQGSAQp0aGVtZV9wYXJr4AEA!16zL20vMDNqbGo5?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Operated by Lotte Group, Lotte World is the perfect spot for entertainment and sightseeing for Koreans and international tourists alike. The theme park is divided into the indoor Lotte World Adventure, and the outdoor lakeside Magic Island, with additional amenities including a shopping mall, folk museum, ice rink, hotel, and more. Lotte World Adventure is the world's largest indoor amusement park, complete with top-of-the-line rides, fantastic parades and performances, and food from around the world. The Folk Museum displays miniature models of Korea throughout 5,000 years in history. Lotte World Garden Stage presents various themed musicals to match each season and Lotte World Star Avenue is the perfect place to experience Korean stars and the entertainment world.'''
#추천 장소 4곳
rec_place = ['석촌호수 서호', '석촌호수 동호', '서울스카이', '서울어린이대공원 놀이동산']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/예시/ltseoul.png', './img/예시/everland.jpeg', './img/예시/gjworld.jpeg', './img/예시/carrbay.jpeg']
#추천 장소 설명 4개
rec_caption = ['theme park located in seoul... etc 기타 간단한 영어 설명 - 번역기 돌려도 됨', 'theme park located in seoul... etc',
               'theme park located in seoul... etc', 'theme park located in seoul... etc']
# 관광지 Image 1
image1 = './img/수정/롯데월드.png'
#Wordcloud Image 2
image2 = './img/인화/대릉원 워드클라우드.png'
#그래프 Image 3
image3 = './img/예시/graph.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab2, name, googlelink, intro, image1, image2, image3)

# --------------------------(경복궁)-------------------------
#관광지명
name = list[2]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EA%B2%BD%EB%B3%B5%EA%B6%81/data=!3m1!1e3!4m10!1m2!2m1!1z6rK967O16raB!3m6!1s0x357ca2c74aeddea1:0x8b3046532cc715f6!8m2!3d37.579617!4d126.977041!15sCgnqsr3rs7XqtoFaCyIJ6rK967O16raBkgERY3VsdHVyYWxfbGFuZG1hcmvgAQA!16zL20vMDJ2M3Q2?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Gyeongbokgung Palace was built as the official palace of the Joseon dynasty by Yi Seong-gye, who becomes King Taejo and the founder of the new regime. Gyeongbokgung Palace is commonly referred to as the Northern Palace because its location in the north of Changdeokgung Palace in the east and Gyeonghuigung Palace in the west. Gyeongbokgung Palace is arguably the most beautiful and is the largest of all five palaces. Many Joseon kings were crowned here, including the 2nd King Jeongjong, 4th King Sejong, 6th King Danjong, 7th King Sejo, 9th King Seongjong, 11th King Jungjong, and the 13th King Myeongjong. The premises were once destroyed by fire during the Imjin War (1592-1598). However, all of the palace buildings were later restored under the leadership of Heungseondaewongun during the reign of King Gojong. The assassination of Empress Myeongseong, however, resulted in Gyeongbokgung Palace losing its function as a royal palace, eventually witnessing the downfall of the Joseon dynasty. Gyeongbokgung Palace retains the original Gyeonghoeru Pavilion, a prime example of Joseon architecture, and the Hyangwonjeong Pavilion and pond. The sculptures in the Geunjeongjeon Hall exemplify Joseon-era sculpture techniques. The west side of the area outside Heungnyemun Gate is occupied by the National Palace Museum of Korea, while the eastern side of Hyangwonjeong Pavilion within the Gyeongbokgung Palace is occupied by the National Folk Museum of Korea.'''
#추천 장소 4곳
rec_place = ['서촌한옥마을', '덕수궁', '광화문', '창덕궁']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/예시/ltseoul.png', './img/예시/everland.jpeg', './img/예시/gjworld.jpeg', './img/예시/carrbay.jpeg']
#추천 장소 설명 4개
rec_caption = ['theme park located in seoul... etc 기타 간단한 영어 설명 - 번역기 돌려도 됨', 'theme park located in seoul... etc',
               'theme park located in seoul... etc', 'theme park located in seoul... etc']
# 관광지 Image 1
image1 = './img/수정/경복궁.webp'
#Wordcloud Image 2
image2 = './img/인화/대릉원 워드클라우드.png'
#그래프 Image 3
image3 = './img/예시/graph.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab3, name, googlelink, intro, image1, image2, image3)

# --------------------------(석촌호수 서호)-------------------------
#관광지명
name = list[3]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%84%9D%EC%B4%8C%ED%98%B8%EC%88%98(%EC%84%9C%ED%98%B8)/data=!3m2!1e3!4b1!4m6!3m5!1s0x357ca5a160554ffb:0x27d136ac3a9f1dba!8m2!3d37.5080556!4d127.1005556!16s%2Fg%2F1tk_m6rs?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Songpa Naru Park, also commonly referred to as Seokchonhosu Lake, is a citizen park in Seoul with a jogging course and walking trails. It has two lakes with Songpa-daero Boulevard running in between. Originally, a branch of the Hangang River ran through the site, forming one large lake, but the lake was divided into two with the construction of Songpa-daero Boulevard. The total size of the two lakes is 217,850 ㎡, and they hold about 737 tons of water. The depth of the lakes is 4-5 meters.'''
#추천 장소 4곳
rec_place = ['석촌호수 동호', '송리단길', '롯데월드 어드벤처', '서울스카이']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/예시/ltseoul.png', './img/예시/everland.jpeg', './img/예시/gjworld.jpeg', './img/예시/carrbay.jpeg']
#추천 장소 설명 4개
rec_caption = ['theme park located in seoul... etc 기타 간단한 영어 설명 - 번역기 돌려도 됨', 'theme park located in seoul... etc',
               'theme park located in seoul... etc', 'theme park located in seoul... etc']
# 관광지 Image 1
image1 = './img/수정/석촌호수.jpeg'
#Wordcloud Image 2
image2 = './img/인화/대릉원 워드클라우드.png'
#그래프 Image 3
image3 = './img/예시/graph.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab4, name, googlelink, intro, image1, image2, image3)

# --------------------------(서울어린이대공원)-------------------------
#관광지명
name = list[4]
#관광지 구글 링크
googlelink = 'https://www.google.com/maps/place/%EC%96%B4%EB%A6%B0%EC%9D%B4%EB%8C%80%EA%B3%B5%EC%9B%90/data=!3m2!1e3!4b1!4m6!3m5!1s0x357ca4d713856077:0x169df594b1f221cc!8m2!3d37.549363!4d127.0818126!16s%2Fm%2F0h3m64t?hl=ko&entry=ttu'
#관광지 소개 글
intro = '''Opened in May 1973, Seoul Children’s Grand Park is a theme park situated among green forests and fields with a total area of 56,552㎡. It contains a zoo, arboretum, amusement park, and performance venues. Seoul Children’s Grand Park has been a beloved part of Seoul, a paradise for children and a living venue for education. For grown-ups, it functions as an area of refuge and culture within the city. The Grand Park offers facilities that everyone in the family can enjoy, so everyone can find their own fun in the Grand Park.'''
#추천 장소 4곳
rec_place = ['서울어린이대공원 동물원', '서울어린이대공원 놀이동산', '남산서울타워', '우리유황온천']
#추천 장소 이미지 경로 4개
rec_place_img = ['./img/예시/ltseoul.png', './img/예시/everland.jpeg', './img/예시/gjworld.jpeg', './img/예시/carrbay.jpeg']
#추천 장소 설명 4개
rec_caption = ['theme park located in seoul... etc 기타 간단한 영어 설명 - 번역기 돌려도 됨', 'theme park located in seoul... etc',
               'theme park located in seoul... etc', 'theme park located in seoul... etc']
# 관광지 Image 1
image1 = './img/수정/서울어린이대공원.jpeg'
#Wordcloud Image 2
image2 = './img/인화/대릉원 워드클라우드.png'
#그래프 Image 3
image3 = './img/예시/graph.png'
#tabnum만 바꿔주기 (tab1, tab2, tab3, tab4, tab5)
tabs(tab5, name, googlelink, intro, image1, image2, image3)