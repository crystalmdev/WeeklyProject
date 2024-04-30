import streamlit as st
from PIL import Image
import folium
import numpy as np

from streamlit_folium import st_folium
from streamlit_folium import st_folium, folium_static

st.header('Gyeongbuk')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Woljeonggyo Bridge', 'Hwangridan Street',\
                                        'Daereungwon', 'Cheomseongdae', 'Yeongildae Beach'])

with tab1:
    st.subheader('Woljeonggyo Bridge')
    with st.container(height=200):
        st.markdown('''The name Jeongjeong is recorded in Samguk Sagi (History of the Three Kingdoms) in the 19th year of King Gyeongdeok’s reign of Unified Silla: 
        “The palace will be located in Wolcheon, with two parts, Woljeong Bridge and Chunyang Bridge.”
        After 10 years of collaborative investigation, historical research, and restoration of what was lost and disappeared during the Joseon Dynasty, 
        all restoration was completed in April 2018. In 2013, the bridge was selected for restoration, and the gate tower (motor gate) of the bridge was built separately.
        On the second floor of the gate tower, there is an exhibition hall where you can view videos of the bridge's restoration process and excavated artifacts.
        We can see the entirety of Woljeong Bridge during the day, and Woljeong Bridge at night tempts us with another charm.
        The person on the other side of Woljeong Bridge is the person looking at Woljeong Bridge. You can capture Woljeong Bridge shining softly over the river.''')
    st.divider()

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('**Introduction**')
        st.image(Image.open('./img/인화/woljeong_bridge.jpg'),
                 use_column_width=True)
    with col2:
        st.markdown('**Similar Destinations**')
        row1 = st.columns(2)
        row2 = st.columns(2)
        rec_place = ['Donggung Palace and Wolji Pond', 'Cheonmachong', 'Bomun Tourist Complex', 'Bomunjeong']
        rec_place_img = ['./img/인화/dongpalace.jpg', './img/인화/cheonma.jpg', './img/인화/bomun.jpg', './img/인화/bomunjeong.jpg']
        rec_caption = ['Announcement time: 09:00 - 22:00 (ticket date 21:30), short break\
                        Fee: Adults 3,000 won / 2,000 won / Children 1,000 won', \
                       'Operating hours 09:00-22:00 \
                       Admission fee: Adults 3,000 / Soldiers, Youth 2,000 / Children 1,000',\
                       'Bomun Tourist Complex has leisure and tourist facilities scattered across a large area,\
                        so it is recommended to travel by car or bicycle. \
                        The public transportation infrastructure is good, so traveling by bus is not a problem.', \
                       'Bomunjeong boasts such beautiful scenery that it was once introduced as ‘Korea’s Secret Place’ on CNN.\
                       Cherry trees and maple trees are planted around the octagonal pavilion and two ponds, \
                       making it a place to enjoy the scenery in any season.']
        for i, col in enumerate(row1 + row2):
            tile = col.expander(rec_place[i])
            tile.image(Image.open(rec_place_img[i]),
                        caption=rec_caption[i],
                        use_column_width=True)
    st.divider()
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('**WordCloud**')
        st.text('(based on Korean blog reviews)')
        st.image(Image.open('./img/인화/월정교 워드클라우드.png'),
                 use_column_width=True)
    with col2:
        st.markdown('**Top 20 Keywords**')
        st.text('(based on Korean blog reviews)')
        st.image(Image.open('./img/인화/월정교 상위20개 단어빈도.png'),
                 use_column_width=True)

with tab2:
    st.subheader('Hwangridan Street')
    with st.container(height=200):
        st.markdown('''
        Hwangridan-gil is the youngest road in Gyeongju. It refers to the area around Hwangnam-dong and Sajeong-dong on both sides of the road starting from Naenam Intersection to Hwangnam Elementary School Intersection.
        A few years ago, young people began to gather here, and cafes with a nice atmosphere, cute props, souvenir shops, and unique restaurants opened.
        In the beginning, shops were built mainly along the roadside, but as the outer edge of Hwangridan-gil expanded, unique shops began popping up in every alley.
        It is so hot that it has become an essential course that cannot be missed when traveling to Gyeongju.
        Go to the cafe you were looking for, knock on the door of a restaurant that catches your eye while walking, or go to the last stage of your Gyeongju trip to get a cute souvenir to commemorate Gyeongju. Let’s eat, drink, and have fun on Hwangridan-gil.
        ''')
    st.divider()

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('**Introduction**')
        st.image(Image.open('./img/인화/hwanglidan.jpg'),
                 use_column_width=True)
    with col2:
        st.markdown('**Similar Destinations**')
        row1 = st.columns(2)
        row2 = st.columns(2)
        rec_place = ['Cheomseongdae', 'Bomunho Lake', 'Woljeonggyo Bridge', 'Daereungwon']
        rec_place_img = ['./img/인화/cheom.jpg', './img/인화/bomunlake.jpg', './img/인화/woljeong_bridge.jpg', './img/인화/daer.jpg']
        rec_caption = ['It is an astronomical observatory from the Silla period that observed the movement of celestial bodies.', \
                       'Bomun Lake, a huge artificial lake measuring 500,000 pyeong',\
                       'Opening hours: 09:00-22:00\
                       Admission fee: Free\
                        Parking information: Use Woljeonggyo public parking lot (153-5 Gyo-dong, free)', \
                       'Opening hours: 09:00-22:00 (ticket sales close at 21:30)\
                       Admission fee: Free (Cheonmachong Tomb paid)\
                       Parking: Daereungwon public parking lot (9 Gyerim-ro, paid), Nodong public parking lot (767 Taejong-ro, paid), Jjoksae temporary parking lot (Enter Wonhwa-ro 181beon-gil, free)']
        for i, col in enumerate(row1 + row2):
            tile = col.expander(rec_place[i])
            tile.image(Image.open(rec_place_img[i]),
                        caption=rec_caption[i],
                        use_column_width=True)
    st.divider()
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('**WordCloud**')
        st.text('(based on Korean blog reviews)')
        st.image(Image.open('./img/인화/황리단길 워드클라우드.png'),
                 use_column_width=True)
    with col2:
        st.markdown('**Top 20 Keywords**')
        st.text('(based on Korean blog reviews)')
        st.image(Image.open('./img/인화/황리단길 상위20개 단어빈도.png'),
                 use_column_width=True)

with tab3:
    st.subheader('Daereungwon')
    with st.container(height=200):
        st.markdown('''
        Tomb ruins are scattered throughout the area, centered around Daereungwon, where 23 tombs from the Silla period are gathered on a large land of 126,500 m2.
    Even just looking around the inside of Daereungwon will take quite a bit of time.
    Ancient tombs worth paying attention to include the tomb of King Michu, the 13th king, 
    Hwangnamdaechong Tomb, which catches the eye with its huge double-shaped tomb, and Cheonmachong Tomb, where you can look inside the tomb. 
    The picturesque photo zone of a magnolia tree standing between ancient tombs is a viewing point of Daereungwon that should not be missed.
        ''')
    st.divider()

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('**Introduction**')
        st.image(Image.open('./img/인화/daer.jpg'),
                 use_column_width=True)
    with col2:
        st.markdown('**Similar Destinations**')
        row1 = st.columns(2)
        row2 = st.columns(2)
        rec_place = ['Cheonmachong', 'Cheomseongdae', 'Woljeonggyo Bridge', 'Bomunjeong']
        rec_place_img = ['./img/인화/cheonma.jpg', './img/인화/cheom.jpg', './img/인화/woljeong_bridge.jpg', './img/인화/bomunjeong.jpg']
        rec_caption = ['Operating hours 09:00-22:00\
                        Admission fee: Adults 3,000 / Soldiers, Youth 2,000 / Children 1,000', \
                       'It is an astronomical observatory from the Silla period that observed the movement of celestial bodies.',\
                       'Opening hours: 09:00-22:00\
                       Admission fee: Free\
                        Parking information: Use Woljeonggyo public parking lot (153-5 Gyo-dong, free)', \
                       'Bomunjeong boasts such beautiful scenery that it was once introduced as ‘Korea’s Secret Place’ on CNN.\
                       Cherry trees and maple trees are planted around the octagonal pavilion and two ponds, \
                       making it a place to enjoy the scenery in any season.']
        for i, col in enumerate(row1 + row2):
            tile = col.expander(rec_place[i])
            tile.image(Image.open(rec_place_img[i]),
                        caption=rec_caption[i],
                        use_column_width=True)
    st.divider()
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('**WordCloud**')
        st.text('(based on Korean blog reviews)')
        st.image(Image.open('./img/인화/대릉원 워드클라우드.png'),
                 use_column_width=True)
    with col2:
        st.markdown('**Top 20 Keywords**')
        st.text('(based on Korean blog reviews)')
        st.image(Image.open('./img/인화/대릉원 상위20개 단어빈도.png'),
                 use_column_width=True)

with tab4:
    st.subheader('Cheomseongdae')
    with st.container(height=200):
        st.markdown('''
        It is an astronomical observatory from the Silla Dynasty that observed the movement of celestial bodies. It had a cylindrical part shaped like a liquor bottle on top of the stylobate, which served as a pedestal, and a crown shaped like the letter 井 on top. It is approximately 9m high.
    The cylindrical part is made of 27 layers of fan-shaped stones, and compared to the smooth and well-trimmed exterior, the interior walls are uneven due to the back roots of the stones sticking out. Centered around the southeastern window, the lower part is filled with masonry stones, and the upper part is open to the top and is hollow. The eastern half of the summit is blocked by flagstones, and the ends of long stones interlocked in the shape of the letter 井 protrude to the outside. This type of appearance is also found in levels 19 to 20 and levels 25 to 26, and appears to have been suitable for carrying a ladder inside. According to an old record, “people are supposed to go up in the middle,” and it appears that they placed a ladder outside, went inside through the window, and then used the ladder to climb to the top and observe the sky.
    Astronomy is deeply related to agriculture in that it can determine the timing of farming based on the movement of the sky, and is also related to politics, given that astrology, which predicted good or bad times for a country based on observation results, was considered important in ancient countries. You can see how deep this is. Therefore, it became a matter of great national interest from early on, and it is believed that this served as a good background for the construction of Cheomseongdae.
    It is believed to have been built during the reign of Queen Seondeok of Silla (reign 632-647). It is of great value as the oldest astronomical observatory in the East and can be said to be a valuable national heritage that shows the high level of science at the time.
        ''')
    st.divider()

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('**Introduction**')
        st.image(Image.open('./img/인화/cheom.jpg'),
                 use_column_width=True)
    with col2:
        st.markdown('**Similar Destinations**')
        row1 = st.columns(2)
        row2 = st.columns(2)
        rec_place = ['Woljeonggyo Bridge','Daereungwon','Donggung Palace and Wolji Pond','Cheonmachong']
        rec_place_img = ['./img/인화/woljeong_bridge.jpg', './img/인화/daer.jpg', './img/인화/dongpalace.jpg', './img/인화/cheonma.jpg']
        rec_caption = ['Opening hours: 09:00-22:00\
                       Admission fee: Free\
                        Parking information: Use Woljeonggyo public parking lot (153-5 Gyo-dong, free)', \
                       'Opening hours: 09:00-22:00 (ticket sales close at 21:30)\
                        Admission fee: Free (Cheonmachong Tomb paid)\
                        Parking: Daereungwon public parking lot (9 Gyerim-ro, paid), Nodong public parking lot (767 Taejong-ro, paid), Jjoksae temporary parking lot (Enter Wonhwa-ro 181beon-gil, free)', \
                       'Announcement time: 09: 00 - 22:00(ticket date 21: 30), short break \
                        Fee: Adults 3,000won / 2,000won / Children1,000won',\
                       'Operating hours 09:00-22:00\
                        Admission fee: Adults 3,000 / Soldiers, Youth 2,000 / Children 1,000'
                       ]
        for i, col in enumerate(row1 + row2):
            tile = col.expander(rec_place[i])
            tile.image(Image.open(rec_place_img[i]),
                        caption=rec_caption[i],
                        use_column_width=True)
    st.divider()
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('**WordCloud**')
        st.text('(based on Korean blog reviews)')
        st.image(Image.open('./img/인화/첨성대 워드클라우드.png'),
                 use_column_width=True)
    with col2:
        st.markdown('**Top 20 Keywords**')
        st.text('(based on Korean blog reviews)')
        st.image(Image.open('./img/인화/첨성대 상위20개 단어빈도.png'),
                 use_column_width=True)

with tab5:
    st.subheader('Yeongildae Beach')
    with st.container(height=200):
        st.markdown('''
         Pohang Yeongildae Beach, where roses and the sea come together
    Pohang Yeongildae Beach is a representative beach in Pohang. 
    It was originally called Bukbu Beach, but the name was changed to ‘Yeongildae Beach’ in June 2013 when ‘Yeongildae Marine Pavilion’ was built. 
    The night view of Yeongil University & POSCO is considered a representative night view attraction in Pohang, being designated as the 5th view among the 12 scenic views of Pohang.
        ''')
    st.divider()

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('**Introduction**')
        st.image(Image.open('./img/인화/youngildae.jpg'),
                 use_column_width=True)
    with col2:
        st.markdown('**Similar Destinations**')
        row1 = st.columns(2)
        row2 = st.columns(2)
        rec_place = ['Space Walk','Pohang Maritime skywalk','Chilpo Beach','Pohang--Songdo Beach']
        rec_place_img = ['./img/인화/spacewalk.jpg', './img/인화/pohangsky.jpg', './img/인화/chilpo.jpg', './img/인화/pohangsongdo.jpg']
        rec_caption = ['The Space Walk, located in Pohang Hwanhwa Park, was built with a track length of 333m and a number of stairs of 717.', \
                       'The height is 7m and the total length is 463m.\
                       The largest scale in the country\
                       This is a walking trail where you can walk on the beautiful sea of Pohang.', \
                       'Chilpo Beach, located 13km north of Pohang, was opened early as a beach with a wide white sand beach and clear, shallow water.',\
                       'Songdo Beach was a representative beach in Gyeongsangbuk-do, but was closed due to worsening erosion of the white sand beach, and has been redeveloped as a tourist destination since 2012.'
                       ]
        for i, col in enumerate(row1 + row2):
            tile = col.expander(rec_place[i])
            tile.image(Image.open(rec_place_img[i]),
                        caption=rec_caption[i],
                        use_column_width=True)
    st.divider()
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('**WordCloud**')
        st.text('(based on Korean blog reviews)')
        st.image(Image.open('./img/인화/영일대해수욕장 워드클라우드.png'),
                 use_column_width=True)
    with col2:
        st.markdown('**Top 20 Keywords**')
        st.text('(based on Korean blog reviews)')
        st.image(Image.open('./img/인화/영일대해수욕장 상위20개 단어빈도.png'),
                 use_column_width=True)
