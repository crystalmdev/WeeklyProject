import streamlit as st
from streamlit.components.v1 import html

# 페이지 설정
st.set_page_config(page_title="Korea on Map User-Guide", page_icon="📘", layout="wide")

# 스타일
style = """
<style>
    .title-wrapper {
        padding: 10px 0;
    }
    h1, h2, h3 {
        color: #4A90E2;
    }
    .streamlit-container {
        margin: 20px;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        background-color: #EDF2F7;
    }
    img {
        border-radius: 8px;
    }
    .streamlit-expander {
        margin-bottom: 20px;
    }
</style>
"""

# 타이틀 및 소개
st.title("🌏 How to Use 'Korea on Map' Travel Guide")
st.image("https://images.studentuniverse.com/new/suwebui/photos/marketing-us/landing-pages/header/header-SEL.jpg",
         caption="Explore Korea")
st.markdown("""
            Dive into the vibrant culture, breathtaking landscapes, and unforgettable experiences that Korea has to offer. 
            Let's make your travel planning exciting and effortless!""")

st.divider()

st.markdown("""
            ### 💡Why Use This Dashboard?
            - **Discover Hidden Gems**: Explore locations through high-quality images and engaging descriptions.
            - **Explore locations to plan your trip**: Explore popular destinations and check out visitor reviews.
            - **Embark on an Adventure**: Discover a journey to unearth exciting destinations handpicked through similarity analysis.
            """, unsafe_allow_html=True)

st.divider()

# 대시보드 사용 가이드(지역/관광지 선택)
with st.container():
    st.header("🔍 How to Use This Dashboard")
    row1_col1, row1_col2 = st.columns([1, 1])
    row2_col1, row2_col2 = st.columns([1, 1])

    with row1_col1:
        st.markdown("### 1. Select a Region")
        st.markdown("<span style='font-size:18px;'>"
                    "Click on the section you want to expand and explore in-depth information about each tourist spot.</span>",
                    unsafe_allow_html=True)

    with row1_col2:
        st.image("img/select.png", width=400, caption="Choose your destination")

    with row2_col1:
        st.markdown("### 2. Explore Attractions")
        st.markdown("<span style='font-size:18px;'>Each region features up to 5 top attractions selected through the analysis of reviews and transportation data.</span>",
                    unsafe_allow_html=True)

    with row2_col2:
        st.image("img/select2.png", width=400, caption="Discover popular attractions")

    st.markdown("### 3. Ready to Explore?")
    st.markdown(
        "To start your journey, choose a region and discover abundant attractions and cultural activities!🎒")

st.divider()

# 관광지 위치 및 교통
with st.container():
    st.header("📌 Detailed Information on Attractions")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Google Maps")
        st.markdown("View the location on Google Maps.")
        st.markdown("[View on Google Maps](https://maps.google.com)", unsafe_allow_html=True)
        st.image("img/google_map.png", caption="Map View")

    with col2:
        st.markdown("### Train Bookings")
        st.markdown("Visit Korail to book train tickets.")
        st.markdown("[Book Trains on Korail](http://www.letskorail.com)")
        st.image("img/train.png", caption="Train Tickets")

    with col3:
        st.markdown("### Bus Bookings")
        st.markdown("Access Kobus to book bus tickets.")
        st.markdown("[Book Buses on Kobus](http://www.kobus.co.kr)")
        st.image("img/bus.png", caption="Bus Tickets")

st.divider()

# 유사관광지
col1, col2 = st.columns([1.5, 1.5])
with col1:
    st.header("📊 Interact with the Data")
    st.markdown("""
                Click on a tourist spot that interests you. Our data dashboard uses advanced cosine 
                similarity analysis to recommend four other tourist spots with similar characteristics 
                to the one you selected.<br><br>
                By analyzing visitor reviews of the selected spot, we recommend 
                places based on ratings and accessibility. This helps you discover new places that you 
                might be interested in.""", unsafe_allow_html=True)

with col2:
    st.image("img/like.png", width=500)

st.divider()

# 시각화
st.header("🌟 Additional Features")
col1, col2 = st.columns(2)
with col1:
    col1.metric("Keyword Analysis", "Cloud Image")
    st.image("img/다율/상소동산림욕장 워드클라우드.png", width=350)
    st.markdown("""
                The Keyword Analysis feature generates a Word Cloud visualizing the frequency of words in a text corpus. 
                It provides a quick overview of the most commonly used words, allowing users to identify prominent 
                themes or topics extracted from visitor reviews.""")

with col2:
    col2.metric("Popular Months", "Donut Chart")
    st.image("img/donut.png", width=350)
    st.markdown("""
                The Popular Months feature displays data in a Donut Chart format, illustrating the distribution 
                of a categorical variable across different categories. It allows users to easily grasp the relative 
                proportions of each category within the dataset, based on the analysis of review dates.""")

st.write('   ')
st.write('   ')

col3, col4 = st.columns(2)
with col3:
    st.metric("Sentiment Analysis", "Emoji Representation")
    st.image("img/emoji.png", width=440)
    st.markdown("""
                The sentiment analysis provides a visual representation of review data, allowing users to 
                interpret the sentiment of customer feedback more intuitively. By analyzing the words used 
                in the reviews, it categorizes them as positive or negative and represents the feedback 
                using appropriate emojis for easier interpretation.
                """)

with col4:
    col4.metric("Bigram NetworkX Graph", "Graph Image")
    st.image("img/다율/스파크랜드그래프.png", width=350)
    st.markdown("""
                The Bigram NetworkX Graph visualizes the co-occurrence of words in a corpus using a graph structure. 
                It helps to identify patterns and relationships between words based on their proximity and frequency 
                of occurrence.""")

st.divider()

# FAQ
st.header("❓ Frequently Asked Questions")
with st.expander("How do I navigate between different regions?"):
    st.markdown("Use the sidebar to select the region you want to explore. "
                "Each region has its own dedicated page with information on top attractions.")

with st.expander("What if I encounter issues with booking?"):
    st.markdown("You can contact our support team via the 'Help' section in the sidebar or directly through "
                "the contact page linked at the bottom of the dashboard.")

st.divider()

# 피드백
st.header("📢 We'd Love to Hear from You!")
st.markdown("Please share your thoughts and experiences using this dashboard. "
            "Your feedback is invaluable to us!")

# 피드백 입력
feedback = st.text_area("Enter your feedback here:", height=150)
if st.button('Submit Feedback'):
    if feedback:
        st.success("Thank you for your feedback!")
    else:
        st.error("Please enter some feedback before submitting.")

st.divider()

# 마무리
st.subheader("🤗 We hope this guide enhances your travel planning experience!")
st.caption("For any assistance, feel free to contact our support team.")

# 웹사이트 보면 있길래...
st.text("Korea Travel Dashboard Guide © 2024")
