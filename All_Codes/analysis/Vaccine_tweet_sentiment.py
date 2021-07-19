from os import name
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import streamlit as st
import pandas as pd

df = pd.read_csv("vaccination_all_tweets.csv")
st.sidebar.title("Welcome all covid vaccine tweet sentiment analysis")

sia = SentimentIntensityAnalyzer()

if st.sidebar.checkbox("view dataset"):
    st.write(df.head())

sentences = []
df=df[:200]

option=st.sidebar.selectbox("Choose any option",['sentiment analysis of all tweets','top 10 positive tweets','top 10 negative tweets'])

class Student:

    def __init__(self, name, cls, marks):
        self.name = name
        self.cls = cls
        self.marks = marks

    def show(self):
        print("name  =>",self.name)
        print(" cls  =>",self.cls)
        print("marks =>",self.marks)

    # convert object to string when printed
    def __str__(self):
        return f"{self.name} in {self.cls}"

    def __gt__(self,other):
        return self.marks > other.marks

    def __repr__(self):
        return self.name

    def __add__(self,other):
        return self.marks + other.marks



if option == 'sentiment analysis of all tweets':
     for sentence in df['text']: 
                  
        polarity = sia.polarity_scores(sentence)   
        pos = polarity["pos"]
        neu = polarity["neu"]
        neg = polarity["neg"]
    
        pos=round(pos*100,2)
        neu=round(neu*100,2)
        neg=round(neg*100,2)

        aa = df['user_name']
        bb = df['user_followers']
        cc = df['text']
        dd = df['user_verified']
        
        usertweet['sentiment']['pos'] = pos 
        usertweet['sentiment']['neg'] = neg
        usertweet['sentiment']['neu'] = neu        

        for a,b,c,d in zip(aa,bb,cc,dd):
            usertweet['name'] = df['user_name']
            usertweet['followers'] = df['user_followers']
            usertweet['text'] = df['text']
            usertweet['verified'] = df['user_verified']
st.text(type(pos))

st.text(pos)
         

    