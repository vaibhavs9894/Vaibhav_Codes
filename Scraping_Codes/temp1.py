import pandas as pd
from bs4 import BeautifulSoup
import requests
url=requests.get("https://www.himalayanwritingretreat.com/bestselling-books-in-india/#tve-jump-17aaf315541")

html=url.content
soup=BeautifulSoup(html,"html.parser")
main=soup.find('div',class_='thrv_wrapper thrv_table tcb-fixed tcb-mobile-table')

data=[]
i= 0
for vs in main.find_all('div', class_='thrv_wrapper thrv_text_element'):
    i=i+1
    j=0
    k=1
    l=2
    m=3
    if i>5:
        if 
        name=vs.text
        data.append({   
        "Author":name})
print(data)
pd.DataFrame(data).to_csv("BEst_Selling_Novel.csv")

    
