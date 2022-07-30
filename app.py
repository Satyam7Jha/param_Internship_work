import streamlit as st

from pull_news import get_news

header = st.container()
input_ = st.container()
body = st.container()


st.markdown(
    """
    <style>
    .main{
    background-color: #F5F5F5;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with header:
    st.title("Welcom to my Project")
    st.text("In this Project I use web scraping to fetch the news.")

    # taking input

    # topic = st.selectbox("Select Topic: ", options=["India", "Business"])
    topic = st.text_input("Search for topics,locations & sources", "India")

news_data = get_news(topic)


with body:
    for news in news_data:
        try:

            st.markdown(f"## {news['publisher']}")
            image, text = st.columns(2)
            image.markdown(f"![Image not available!!]({news['imgUrl']})")
            text.markdown(f"#### {news['title']}.")
            text.text(f"{news['time']}.")
            text.markdown(f"[View Full article]({news['url']})")
            st.markdown("--------------------------------------------------------")
        except:
            pass
