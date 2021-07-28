import pandas as pd
from bs4 import BeautifulSoup
import requests
import streamlit as st

search = st.text_input('Enter the product')
k="https://www.flipkart.com/search?q="
l = k+search
url=requests.get(l)

html = url.content
soup= BeautifulSoup(html,"html.parser")

main=soup.find('div', class_='_1YokD2 _2GoDe3')

data=[]
for vs in main.find_all('div', class_='_4ddWXP'):
    name=vs.find('a', class_='s1Q9rs').text
    price=vs.find('div', class_='_30jeq3').text
    
    data.append({"name":name,
        "price":price})
print(data)
print(len(data))
pd.DataFrame(data).to_csv("Flipkart_price.csv")