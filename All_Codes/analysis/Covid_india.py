import streamlit as st
import pandas as pd
import folium
from folium import plugins # for clusters
from streamlit_folium import folium_static

df = pd.read_csv(".\data\Covid_19_india.csv",parse_dates=['Date'])
st.sidebar.title("Welcome")

sf_coords=(26.8467,80.9462)

if st.sidebar.checkbox("view dataset"):
    st.write(df.head())

menu=st.sidebar.selectbox("select option",['view map empty','view map markers',"view map clusters"])
if menu == 'view map empty':
    
    map = folium.Map(location=sf_coords,zoom_start=12)
    folium_static(map)

if menu == "view map markers":
    st.subheader("showing Covid Cases in Lucknow")
    map = folium.Map(location=sf_coords,zoom_start=12)
    df = df[:100]
    latitudes = df['Y']
    longitudes = df['X']
    categories = df['Category']
    descriptions = df['Descript']

    for lat,lng,cat,des in zip(latitudes,longitudes,categories,descriptions):
        folium.Marker((lat,lng),popup=cat,tooltip=des).add_to(map)

    folium_static(map)
    
