import pandas as pd
from bs4 import BeautifulSoup
import requests
import streamlit as st

st.set_page_config(page_title='Price Comparision of Product')

st.sidebar.header("Compare Product between Amazon and Flipkart")
st.sidebar.image("https://media.giphy.com/media/SpopD7IQN2gK3qN4jS/giphy.gif", width=300)


df = pd.read_csv('Flipkart_price.csv')
st.write(df.head(50))
da= pd.read_csv('Amazon_price.csv')
st.write(da.head(50))
option=st.sidebar.selectbox("Choose any option",['costliest','Cheapest','Average'])

if option == 'costliest':
    st.header("Costliest Product Price is")
    #all=[]
    #all=df['price']
    #st.write(all)
    #a=max(all)
    #st.write(a)
    p=df['price'].max()
    st.success(p)
    
    

if option == 'Cheapest':
    st.header('Cheapest Product Price is')
    q=df['price'].min()
    st.success(q)


if option == 'Average':
    st.header('Average Product Price is')
    l=len(all)
    x=0
    for i in all:
        x=x+1
        if i==l:
            st.write(i)


if(st.button("Feeling Lucky")):
    st.image("https://media.giphy.com/media/fUYhyT9IjftxrxJXcE/giphy.gif", width=300)

st.beta_container()