from numpy.lib.function_base import percentile
import pandas as pd
from bs4 import BeautifulSoup
import requests
import streamlit as st


search = "earbuds"
url=requests.get("https://www.flipkart.com/search?q=earbuds")

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