import pandas as pd
import requests
from bs4 import BeautifulSoup


url=requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/men/batting")
html = url.content
soup= BeautifulSoup(html,"html.parser")

main=soup.find('div', class_='cb-col cb-col-100 cb-padding-left0')


data=[]

for vs in main.find_all('div', class_='cb-col cb-col-67 cb-rank-plyr'):
    name=vs.text
    player=    data.append({
        "Player":name})
print(data)
pd.DataFrame(data).to_csv("crick_man.csv")