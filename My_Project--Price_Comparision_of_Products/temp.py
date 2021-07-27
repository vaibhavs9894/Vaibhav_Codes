import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title='Price Comparision of Product')
st.sidebar.header("Lets Compare")
st.sidebar.image("up.png",width=100)

main_bg = "sample.jpg"
main_bg_ext = "jpg"

side_bg = "sample.jpg"
side_bg_ext = "jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)


@st.cache
def load_data():
    return pd.read_csv('NIFTY50_all.csv',parse_dates=['Date'])

def home(title):
    df = load_data()
    st.title("Stock data Analysis")
    st.image('image.png',width=400)
    st.write(" ")
    st.header("Raw dataset")
    st.write(" ")
    st.write(df.head(10))
    st.markdown("<hr>", unsafe_allow_html= True)
    col1, col2 = st.beta_columns(2)
    col1.subheader("Number of Rows:")
    col1.write(df.shape[0])
    col2.subheader("Number of Columns:")
    col2.write(df.shape[1])
    st.markdown("<hr>", unsafe_allow_html= True)
    st.write(" ")
    st.header("Dataset Summary")
    st.write(" ")
    st.write(df.describe())

    st.header("Columns description")
    for i in df.columns:
        st.subheader(i)
        col1, col2 = st.beta_columns(2)
        col1.caption("Unique Values")
        col1.write(len(df[i].unique()))
        col2.caption("Type of Data")
        col2.write("String of Characters" if type(df[i].iloc[0]) is str else "Numerical")
        st.markdown("<hr>",unsafe_allow_html = True)


def page1(title):
    df = load_data()
    st.title(title)
    stock = st.sidebar.selectbox("Choose a stock:-", list(df.Symbol.unique()))
    sd = df[df.Symbol == stock]
    st.header("Close price Line graph")
    st.plotly_chart(px.line(sd, 'Date', 'Close'))
    st.header("Candlestick Plot")
    st.plotly_chart(go.Figure(data=[go.Candlestick(x=sd['Date'],open=sd['Open'],high=sd['High'],low=sd['Low'],close=sd['Close'])]))
    st.header("High price Histogram")
    st.plotly_chart(px.histogram(sd,x='Date',y='High'))
    st.header('VWAP over time')
    fig = go.Figure([go.Scatter(x=sd.index, y=sd['VWAP'])])
    fig.update_xaxes(title="Date")
    fig.update_yaxes(title="VWAP")
    st.plotly_chart(fig)
    st.header("Trades over time")
    st.plotly_chart(px.scatter(sd,'Date','Trades'))
    st.header("Volume over time")
    st.plotly_chart(px.line(sd,'Date','Volume'))
    st.header("Turnover")
    st.plotly_chart(px.scatter(sd,'Date','Turnover'))

def page2(title):
    data = load_data()
    st.title(title)
    st.header("Latest Close price comparison")
    st.plotly_chart(px.bar(data[data.Date==max(data.Date)],'Symbol','Close'))
    st.header("Latest VWAP comparison")
    st.plotly_chart(px.bar(data[data.Date==max(data.Date)],'Symbol','VWAP'))
    st.header("Highest Trades comparison")
    st.plotly_chart(px.bar(data.groupby('Symbol',as_index=False).max(),'Symbol','Trades'))
    st.header("Top 10 highest Volume")
    st.plotly_chart(px.pie(data[data.Date==max(data.Date)].head(10),'Symbol','Volume'))
    st.header("Top 10 All time highest Turnover")
    st.plotly_chart(px.pie(data.groupby('Symbol',as_index=False).max().head(10),'Symbol','Turnover'))


pages = {'Introduction':home,'Analysing a single stock':page1,'Comparison between Stocks':page2}
page = st.sidebar.selectbox('Choose a page:-',list(pages.keys()))

pages[page](page)
# This app is for educational purpose only. Insights gained is not financial advice. Use at your own risk!
import streamlit as st
from PIL import Image
import pandas as pd
import base64
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import json
import time
#---------------------------------#
# New feature (make sure to upgrade your streamlit library)
# pip install --upgrade streamlit

#---------------------------------#
# Page layout
## Page expands to full width
st.set_page_config(layout="wide")
#---------------------------------#
# Title

image = Image.open('logo.jpg')

st.image(image, width = 500)

st.title('Crypto Price App')
st.markdown("""
This app retrieves cryptocurrency prices for the top 100 cryptocurrency from the **CoinMarketCap**!
""")
#---------------------------------#
# About
expander_bar = st.beta_expander("About")
expander_bar.markdown("""
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn, BeautifulSoup, requests, json, time
* **Data source:** [CoinMarketCap](http://coinmarketcap.com).
* **Credit:** Web scraper adapted from the Medium article *[Web Scraping Crypto Prices With Python](https://towardsdatascience.com/web-scraping-crypto-prices-with-python-41072ea5b5bf)* written by [Bryan Feng](https://medium.com/@bryanf).
""")


#---------------------------------#
# Page layout (continued)
## Divide page to 3 columns (col1 = sidebar, col2 and col3 = page contents)
col1 = st.sidebar
col2, col3 = st.beta_columns((2,1))

#---------------------------------#
# Sidebar + Main panel
col1.header('Input Options')

## Sidebar - Currency price unit
currency_price_unit = col1.selectbox('Select currency for price', ('USD', 'BTC', 'ETH'))

# Web scraping of CoinMarketCap data
@st.cache
def load_data():
    cmc = requests.get('https://coinmarketcap.com')
    soup = BeautifulSoup(cmc.content, 'html.parser')

    data = soup.find('script', id='__NEXT_DATA__', type='application/json')
    coins = {}
    coin_data = json.loads(data.contents[0])
    listings = coin_data['props']['initialState']['cryptocurrency']['listingLatest']['data']
    for i in listings:
      coins[str(i['id'])] = i['slug']

    coin_name = []
    coin_symbol = []
    market_cap = []
    percent_change_1h = []
    percent_change_24h = []
    percent_change_7d = []
    price = []
    volume_24h = []

    for i in listings:
      coin_name.append(i['slug'])
      coin_symbol.append(i['symbol'])
      price.append(i['quote'][currency_price_unit]['price'])
      percent_change_1h.append(i['quote'][currency_price_unit]['percent_change_1h'])
      percent_change_24h.append(i['quote'][currency_price_unit]['percent_change_24h'])
      percent_change_7d.append(i['quote'][currency_price_unit]['percent_change_7d'])
      market_cap.append(i['quote'][currency_price_unit]['market_cap'])
      volume_24h.append(i['quote'][currency_price_unit]['volume_24h'])

    df = pd.DataFrame(columns=['coin_name', 'coin_symbol', 'market_cap', 'percent_change_1h', 'percent_change_24h', 'percent_change_7d', 'price', 'volume_24h'])
    df['coin_name'] = coin_name
    df['coin_symbol'] = coin_symbol
    df['price'] = price
    df['percent_change_1h'] = percent_change_1h
    df['percent_change_24h'] = percent_change_24h
    df['percent_change_7d'] = percent_change_7d
    df['market_cap'] = market_cap
    df['volume_24h'] = volume_24h
    return df

df = load_data()

## Sidebar - Cryptocurrency selections
sorted_coin = sorted( df['coin_symbol'] )
selected_coin = col1.multiselect('Cryptocurrency', sorted_coin, sorted_coin)

df_selected_coin = df[ (df['coin_symbol'].isin(selected_coin)) ] # Filtering data

## Sidebar - Number of coins to display
num_coin = col1.slider('Display Top N Coins', 1, 100, 100)
df_coins = df_selected_coin[:num_coin]

## Sidebar - Percent change timeframe
percent_timeframe = col1.selectbox('Percent change time frame',
                                    ['7d','24h', '1h'])
percent_dict = {"7d":'percent_change_7d',"24h":'percent_change_24h',"1h":'percent_change_1h'}
selected_percent_timeframe = percent_dict[percent_timeframe]

## Sidebar - Sorting values
sort_values = col1.selectbox('Sort values?', ['Yes', 'No'])

col2.subheader('Price Data of Selected Cryptocurrency')
col2.write('Data Dimension: ' + str(df_selected_coin.shape[0]) + ' rows and ' + str(df_selected_coin.shape[1]) + ' columns.')

col2.dataframe(df_coins)

# Download CSV data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="crypto.csv">Download CSV File</a>'
    return href

col2.markdown(filedownload(df_selected_coin), unsafe_allow_html=True)

#---------------------------------#
# Preparing data for Bar plot of % Price change
col2.subheader('Table of % Price Change')
df_change = pd.concat([df_coins.coin_symbol, df_coins.percent_change_1h, df_coins.percent_change_24h, df_coins.percent_change_7d], axis=1)
df_change = df_change.set_index('coin_symbol')
df_change['positive_percent_change_1h'] = df_change['percent_change_1h'] > 0
df_change['positive_percent_change_24h'] = df_change['percent_change_24h'] > 0
df_change['positive_percent_change_7d'] = df_change['percent_change_7d'] > 0
col2.dataframe(df_change)

# Conditional creation of Bar plot (time frame)
col3.subheader('Bar plot of % Price Change')

if percent_timeframe == '7d':
    if sort_values == 'Yes':
        df_change = df_change.sort_values(by=['percent_change_7d'])
    col3.write('*7 days period*')
    plt.figure(figsize=(5,25))
    plt.subplots_adjust(top = 1, bottom = 0)
    df_change['percent_change_7d'].plot(kind='barh', color=df_change.positive_percent_change_7d.map({True: 'g', False: 'r'}))
    col3.pyplot(plt)
elif percent_timeframe == '24h':
    if sort_values == 'Yes':
        df_change = df_change.sort_values(by=['percent_change_24h'])
    col3.write('*24 hour period*')
    plt.figure(figsize=(5,25))
    plt.subplots_adjust(top = 1, bottom = 0)
    df_change['percent_change_24h'].plot(kind='barh', color=df_change.positive_percent_change_24h.map({True: 'g', False: 'r'}))
    col3.pyplot(plt)
else:
    if sort_values == 'Yes':
        df_change = df_change.sort_values(by=['percent_change_1h'])
    col3.write('*1 hour period*')
    plt.figure(figsize=(5,25))
    plt.subplots_adjust(top = 1, bottom = 0)
    df_change['percent_change_1h'].plot(kind='barh', color=df_change.positive_percent_change_1h.map({True: 'g', False: 'r'}))
    col3.pyplot(plt)