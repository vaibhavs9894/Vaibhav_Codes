import pandas as pd
import requests
from bs4 import BeautifulSoup


url=requests.get("https://www.sarkariresult.com/")
html = url.content
soup= BeautifulSoup(html,"html.parser")

main=soup.find('tbody')

data=[]
for l in main.find_all('a'):
    name=l.text

    data.append({   
        "sarkari_result":name})
print(data)

pd.DataFrame(data).to_csv("Nibha.csv")