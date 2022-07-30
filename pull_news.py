import json
import requests
import streamlit as st

from bs4 import BeautifulSoup


@st.cache
def get_news(title):

    soup = BeautifulSoup(
        requests.get(f"https://news.google.com/search?q={title}&hl=en-IN&gl=IN&ceid=IN%3Aen").content,"html.parser",)

    divisions = soup.find_all("div", class_="NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc")

    news = []
    count, errorCount = 0, 0
    for div in divisions:

        try:

            data = dict()
            data["title"] = div.find("h3").text
            data["imgUrl"] = div.find("a").find("img")["srcset"].split("1x")[-1][2:-3]
            data["url"] = "https://news.google.com/" + div.find("a")["href"][2:]
            data["time"] = (
                div.find("div", class_="QmrVtf RD0gLb kybdz").find("time").text
            )
            data["publisher"] = (
                div.find("div", class_="QmrVtf RD0gLb kybdz").find("a").text
            )

            news.append(data)

        except:
            errorCount += 1
            pass

    return news
