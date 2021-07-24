from os import name
from numpy import dot
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import streamlit as st
import pandas as pd

df = pd.read_csv("vaccination_all_tweets.csv")
st.sidebar.title("Welcome all covid vaccine tweet sentiment analysis")

sia = SentimentIntensityAnalyzer()

if st.sidebar.checkbox("view dataset"):
    st.write(df.head())

df=df[:200]

option=st.sidebar.selectbox("Choose any option",['sentiment analysis of all tweets','top 10 positive tweets','top 10 negative tweets'])

if option == 'sentiment analysis of all tweets':
     for sentence in df['text']:
                  
        polarity = sia.polarity_scores(sentence)
        pos = polarity["pos"]
        neu = polarity["neu"]
        neg = polarity["neg"]
    
        pos=round(pos*100,2)
        neu=round(neu*100,2)
        neg=round(neg*100,2)
        
st.text(type(pos))

st.text(pos)
print("hi my name is vaibhav shrimali this is a new program"
"where you can clearly see whqat you want to do")
"this is a new prograsm why would you wana do that here what is your propblem this is so messed up"
"here")    