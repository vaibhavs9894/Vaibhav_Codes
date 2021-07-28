import pandas as pd
from bs4 import BeautifulSoup
import requests
import streamlit as st

search = "earbuds"
url=requests.get("https://www.amazon.in/s?k=earbuds")
#url=(url+search)
html = url.content
soup= BeautifulSoup(html,"html.parser")

#main=soup.find('div', class_='s-main-slot s-result-list s-search-results sg-row')
main=soup.namefind_all('div', {'data-asin': True, 'data-component-type': 's-search-result'})
data=[]
for vs in main:
    h2=vs.h2
    title=h2.text.strip()
    price=vs.find('span', class_='a-price-whole').text.strip('.').strip()
    print(price)
#print(data)
#print(len(data))
#pd.DataFrame(data).to_csv("Amazon_price.csv")