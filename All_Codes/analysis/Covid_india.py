import streamlit as st
import pandas as pd
import folium
from folium import plugins # for clusters
from streamlit_folium import folium_static

df = pd.read_csv("time_series_covid_19_confirmed_US.csv")
st.sidebar.title("Welcome")

my_expander = st.beta_expander(label='Expand me')
with my_expander:
    'Hello there!'
    clicked = st.button('Click me!')

sf_coords=(41.8781,87.6298)

if st.sidebar.checkbox("view dataset"):
    st.write(df.head())

menu=st.sidebar.selectbox("select option",['view map empty','view map markers',"view map clusters"])
if menu == 'view map empty':
    
    map = folium.Map(location=sf_coords,zoom_start=12)
    folium_static(map)

if menu == "view map markers":
    st.subheader("showing Covid Cases in Chicago")
    map = folium.Map(location=sf_coords,zoom_start=12)
    df = df[:100]
    latitudes = df['Lat']
    longitudes = df['Long_']
    categories = df['Admin2']
    descriptions = df['Combined_Key']

    for lat,lng,cat,des in zip(latitudes,longitudes,categories,descriptions):
        folium.Marker((lat,lng),popup=cat,tooltip=des).add_to(map)

    folium_static(map)
    
if menu == "view map clusters":
    st.header("Marker clusters")

    category = st.sidebar.selectbox("select a category",df['Combined_Key'].unique())
    category_filter = df['Combined_Key'] == category
    cdf = df[category_filter]
    cdf = cdf[:1000] # for saving memory
    if st.sidebar.checkbox("show map"):
        st.subheader(f"showing Covid Cases in {category} ")
        map = folium.Map(location=sf_coords,zoom_start=12)
        icluster = plugins.MarkerCluster().add_to(map)
        latitudes = df['Lat']
        longitudes = df['Long_']
        categories = df['Admin2']
        descriptions = df['Combined_Key']

        for lat,lng,cat,des in zip(latitudes,longitudes,categories,descriptions):
            folium.Marker((lat,lng),popup=cat,tooltip=des).add_to(icluster)

        folium_static(map)
