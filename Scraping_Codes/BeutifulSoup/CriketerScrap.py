import pandas as pd
import requests
from bs4 import BeautifulSoup

url=requests.get("https://www.cricbuzz.com/cricket-team/india/2/stats")
html = url.content
soup= BeautifulSoup(html,"html.parser")
main=soup.find('table', class_='table table-responsive cb-series-stats')
data=[]

for vs in main.find_all('tr', class_='cb-srs-stats-tr'):
    name=vs.text
    player=    data.append({
        "Player":name})
print(data)
pd.DataFrame(data).to_csv("CriketTeam.csv")