import streamlit as st
import requests
import utils

header = st.container()
child = st.container()
input_data = st.container()

body = st.container()

weather_data = utils.get_weather_details()
covid_data = utils.get_covid_details()

st.markdown(
    """
    <style>
    
    img {border: 5px solid white;border-radius:10px}
    .main{
    background-color: #F5F5F5;
    span {
      content: "\00B0";
    } 
    }

    </style>
    """,
    unsafe_allow_html=True,
)

with header:
    st.title("Welcom to my Project")
    st.text("In this Project I use web scraping to fetch the news.")
    st.text("And also showing Covid and Weather updates.")

    # taking input

    # topic = st.selectbox("Select Topic: ", options=["India", "Business"])


with child:

    col1, col2 = st.columns(2)

    col1.markdown("## Covid")
    col1.markdown(
        f"""
        <div style="display:flex;flex-Direction:row;border:2px solid white;justify-content:space-between;padding:10px;border-radius:5px;margin-bottom:20px">
            <div>
                <p>Active</p>
                <p>{covid_data['activeCasesNew']}</p>
                <p>{covid_data['activeCases']}</p>
            </div>
            <div>
                <p style="color:#00D100">Recorverd</p>
                <p style="color:#00D100">+{covid_data['recoveredNew']}</p>
                <p style="color:#00D100">{covid_data['recovered']}</p>
            </div>
            <div>
                 <p style="color:grey">Deaths</p>
                 <p style="color:grey">+{covid_data['deathsNew']}</p>
                 <p style="color:grey">{covid_data['deaths']}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col2.markdown("## Weather")

    col2.markdown(
        f"""
        <div style="display:flex;flex-Direction:row;border:2px solid white;justify-content:space-between;padding:10px;border-radius:5px">
            <div >
                <p>{weather_data['region']}</p>
                <p>{weather_data['location']}</p>
            </div>
            <div>
                <p>{weather_data['temp']}<span>&#176;</span>C</p>
                <p>{weather_data['wind']}km/hr</p>
            </div>
            <div>
                <img src="{weather_data['icon']}" style="width:40px;border:0px solid white;"/>
                 <p>{weather_data['condition']}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with input_data:

    topic = col1.text_input("Search for topics,locations & sources", "India")

news_data = utils.get_news(topic)


with body:
    for news in news_data:
        try:

            st.markdown(f"## {news['publisher']}")
            image, text = st.columns(2)
            image.markdown(
                f"""
                <img src="{news['imgUrl']}"/>
                """,
                unsafe_allow_html=True,
            )
            text.markdown(f"#### {news['title']}.")
            text.text(f"{news['time']}.")
            text.markdown(f"[View Full article]({news['url']})")
            st.markdown("--------------------------------------------------------")
        except:
            pass

