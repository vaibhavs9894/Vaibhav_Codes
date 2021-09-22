import pandas as pd
from bs4 import BeautifulSoup
import requests
url=requests.get("https://www.himalayanwritingretreat.com/bestselling-books-in-india/")

html=url.content
soup=BeautifulSoup(html,"html.parser")
main=soup.find('table',class_='tve-u-17aa9ae96d3')

data=[]
for vs in main.find_all('p', class_='thrv_wrapper thrv_text_element'):
    name=vs.text
    data.append({
        "Bookname":name})
print(data)
pd.DataFrame(data).to_csv("Books_MOst_selling.csv")
    
    
