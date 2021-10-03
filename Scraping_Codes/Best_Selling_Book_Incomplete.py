import pandas as pd
from bs4 import BeautifulSoup
import requests
url=requests.get("https://www.himalayanwritingretreat.com/bestselling-books-in-india/#tve-jump-17aaf315541")

html=url.content
soup=BeautifulSoup(html,"html.parser")
main=soup.find('div',class_='thrv_wrapper thrv_table tcb-fixed tcb-mobile-table')

data=[]
a=0
i=6
j=7
k=8
l=9
namee='Null'
author='Null'
rank='Null'
cat='Null'
for vs in main.find_all('div', class_='thrv_wrapper thrv_text_element'):
    a=a+1
    name=vs.text
    if a>5:
        if a==i:
            i=i+4
            rank=name
        if a==j:
            j=j+4
            namee=name
        if a==k:
            k=k+4
            author=name
        if a==l:
            l=l+3
            cat=name
            data.append({   
            "Rank":rank,
            "Name":namee,
            "Author":author,
            "Category":cat})        
print(data)
pd.DataFrame(data).to_csv("BEst_Selling_Novel.csv")

    
