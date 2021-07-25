import pandas as pd
from bs4 import BeautifulSoup
import requests
import streamlit as st

search = "earbuds"
url=requests.get("https://www.amazon.in/s?k=earbuds")
#url=(url+search)
html = url.content
soup= BeautifulSoup(html,"html.parser")

main=soup.find('div', class_='s-main-slot s-result-list s-search-results sg-row')

data=[]
for vs in main.find_all('div', class_='sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20'):
    name=vs.find('span', class_='a-size-medium a-color-base a-text-normal').text
    price=vs.find('span', class_='a-price-whole').text
    
    data.append({"name":name,
        "price":price})
print(data)
print(len(data))
pd.DataFrame(data).to_csv("Amazon_price.csv")