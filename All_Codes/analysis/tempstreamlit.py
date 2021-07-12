import streamlit as st    
import pandas as pd
import numpy as np 
st.title("New world of sreamlit")
st.write("Hello there")
   



chart_data = pd.DataFrame(
np.random.randn(20, 3),
columns=['a', 'b', 'c'])
st.line_chart(chart_data)

map_data = pd.DataFrame(
np.random.randn(1000, 2) / [10, 10] + [37.76, -122.4],
columns=['lat', 'lon'])
st.map(map_data)

