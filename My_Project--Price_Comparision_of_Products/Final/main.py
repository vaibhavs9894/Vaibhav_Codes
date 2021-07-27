import pandas as pd
from bs4 import BeautifulSoup
import requests
import streamlit as st
import base64


#Scraping from Amazon
search = "earbuds"
url=requests.get("https://www.amazon.in/s?k=earbuds")

html = url.content
soup= BeautifulSoup(html,"html.parser")

main=soup.find('div', class_='s-main-slot s-result-list s-search-results sg-row')

data1=[]
for vs in main.find_all('div', class_='sg-col-inner'):
    name=vs.find('span', class_='a-size-medium a-color-base a-text-normal').text
    price=vs.find('span', class_='a-price-whole').text
    
    data1.append({"name":name,
        "price":price})
print(data1)
print(len(data1))
pd.DataFrame(data1).to_csv("Amazon_price.csv")

#Scraping from Flipkart
url=requests.get("https://www.flipkart.com/search?q=earbuds")

html = url.content
soup= BeautifulSoup(html,"html.parser")

main=soup.find('div', class_='_1YokD2 _2GoDe3')

data2=[]
for vs in main.find_all('div', class_='_4ddWXP'):
    name=vs.find('a', class_='s1Q9rs').text
    price=vs.find('div', class_='_30jeq3').text
    
    data2.append({"name":name,
        "price":price})
print(data2)
print(len(data2))
pd.DataFrame(data2).to_csv("Flipkart_price.csv")

st.set_page_config(page_title='Price Comparision of Product')
st.sidebar.header("Lets Compare")
st.sidebar.image("up.png",width=100)

main_bg = "sample.jpg"
main_bg_ext = "jpg"

side_bg = "sample.jpg"
side_bg_ext = "jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)