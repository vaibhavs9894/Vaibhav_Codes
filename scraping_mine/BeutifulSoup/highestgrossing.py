import pandas as pd
from bs4 import BeautifulSoup
import requests

url=requests.get("https://en.wikipedia.org/wiki/List_of_highest-grossing_films")
html = url.content
soup= BeautifulSoup(html,"html.parser")

main=soup.find('table')

data=[]

for vs in main.find_all('i'):
    name=vs.text
    print(name)
    data.append({
        "Player":name})
print(data)
pd.DataFrame(data).to_csv("Highest movies.csv")