import pandas as pd
import requests
from bs4 import BeautifulSoup

url=requests.get("https://www.imdb.com/chart/toptv/")
html = url.content
soup= BeautifulSoup(html,"html.parser")
main=soup.find('tbody', class_='lister-list')
data=[]
print(main)
for vs in main.find_all('td', class_='titleColumn'):
    name=vs.text
    player=    data.append({
        "Title":name})
print(data)
pd.DataFrame(data).to_csv("TV_Show.csv")