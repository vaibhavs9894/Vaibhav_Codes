import streamlit as st
import pandas as pd
import folium
from folium import plugins # for clusters
from streamlit_folium import folium_static
import plotly.express as px

st.set_page_config(layout='wide')

def load_data():
    df = pd.read_excel("analysis/data/Canada.xlsx",engine='openpyxl',
                   sheet_name="Canada by Citizenship", skiprows=20,
                   nrows=195)
    # cols_to_drop = ['Unnamed: 43','Unnamed: 44', 'Unnamed: 45', 'Unnamed: 46', 'Unnamed: 47','Unnamed: 48', 'Unnamed: 49', 'Unnamed: 50']
    # df.drop(labels=cols_to_drop,axis=1,inplace=True)
    df.rename({'OdName':'Country','AreaName':'Continent','RegName':'Region','DevName':'Status'},axis=1, inplace=True)
    df.set_index('Country',inplace=True)
    cols = ['Type','Coverage','AREA','REG','DEV']
    df.drop(cols,axis=1,inplace=True)
    years = list(range(1980,2014))
    df['Total'] = df[years].sum(axis=1)
    return df

geofile = "analysis/world_countries.json"

df = load_data()
st.write(df.head())
st.title("choropleth")
year = st.sidebar.select_slider("select year",list(range(1980,2014))+["Total"])
map = folium.Map(location=(0,0),zoom_start=2)
map.choropleth(
    geo_data=geofile,
    data =df,
    columns =[df.index,year],
    key_on='feature.properties.name',
    fill_color='Set1',
    fill_opacity=0.7,
    line_opacity=.4,
    line_color='blue',
    legend_name='Total Immigration to Cananda',)


folium_static(map,width=1200)