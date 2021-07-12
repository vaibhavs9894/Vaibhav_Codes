import streamlit as st
import pandas as pd
import folium
from folium import plugins # for clusters
from streamlit_folium import folium_static

df = pd.read_csv(".\data\police_dept.csv",parse_dates=['Date'])
st.sidebar.title("Welcome to San Francisco")

sf_coords=(37.7754,-122.4034)

if st.sidebar.checkbox("view dataset"):
    st.write(df.head())

menu=st.sidebar.selectbox("select option",['view map empty','view map markers',"view map clusters"])
if menu == 'view map empty':
    
    map = folium.Map(location=sf_coords,zoom_start=12)
    folium_static(map)

if menu == "view map markers":
    st.subheader("showing 100 crimes in sanfrancisco")
    map = folium.Map(location=sf_coords,zoom_start=12)
    df = df[:100]
    latitudes = df['Y']
    longitudes = df['X']
    categories = df['Category']
    descriptions = df['Descript']

    for lat,lng,cat,des in zip(latitudes,longitudes,categories,descriptions):
        folium.Marker((lat,lng),popup=cat,tooltip=des).add_to(map)

    folium_static(map)
    

if menu == "view map clusters":
    st.header("Marker clusters")

    category = st.sidebar.selectbox("select a category",df['Category'].unique())
    category_filter = df['Category'] == category
    cdf = df[category_filter]
    cdf = cdf[:1000] # for saving memory
    if st.sidebar.checkbox("show map"):
        st.subheader(f"showing info about {category} incidents")
        map = folium.Map(location=sf_coords,zoom_start=12)
        icluster = plugins.MarkerCluster().add_to(map)
        latitudes = cdf['Y']
        longitudes = cdf['X']
        categories = cdf['Category']
        descriptions = cdf['Descript']

        for lat,lng,cat,des in zip(latitudes,longitudes,categories,descriptions):
            folium.Marker((lat,lng),popup=cat,tooltip=des).add_to(icluster)

        folium_static(map)