import pandas as pd
import requests
from bs4 import BeautifulSoup


url=requests.get("https://www.w3schools.com/python/default.asp")
html = url.content
soup= BeautifulSoup(html,"html.parser")

main=soup.find('div', class_='w3-sidebar w3-collapse')


data=[]

for vs in main.find_all('a'):
    name=vs.text
    player=    data.append({
        "site":name})
print(data)
pd.DataFrame(data).to_csv("sites.csv")