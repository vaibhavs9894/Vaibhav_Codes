import pandas as pd
from bs4 import BeautifulSoup
import requests
import streamlit as st
import base64


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
st.sidebar.image("https://media.giphy.com/media/SpopD7IQN2gK3qN4jS/giphy.gif", width=300)


df = pd.read_csv('Flipkart_price.csv')
st.write(df.head())


option=st.sidebar.selectbox("Choose any option",['costliest','Cheapest','Average'])

if option == 'costliest':
    st.header("this is costliest Box")
    

if option == 'Cheapest':
    st.header('this is Cheapest Box')


if option == 'Average':
    st.header('this is Average Box')
