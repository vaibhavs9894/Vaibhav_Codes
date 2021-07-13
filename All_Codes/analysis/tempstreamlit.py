import streamlit as st

import pandas as pd

st.title("Welcome to Product inventory adder")
name = st.text_input('product name')
price = st.number_input('product price')
brand = st.text_input('product brand')


op = st.checkbox("show products from database")
if op:
    df = pd.read_sql('products',engine)
    st.write(df)
