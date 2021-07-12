import pandas as pd
from bs4 import BeautifulSoup
import requests
url=requests.get("https://www.celebritynetworth.com/list/top-100-richest-people-in-the-world/")

html=url.content
soup=BeautifulSoup(html,"html.parser")
main=soup.find('ul',class_='top_100_couples')

data=[]
for vs in main.find_all('h2'):
    name=vs.text
    data.append({   
        "Player":name[:-10]})
print(data)
pd.DataFrame(data).to_csv("top10NetWorth.csv")
    
    
