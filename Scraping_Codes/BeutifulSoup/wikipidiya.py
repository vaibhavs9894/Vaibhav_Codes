import pandas as pd
import requests
from bs4 import BeautifulSoup


url=requests.get("https://en.wikipedia.org/wiki/Amitabh_Bachchan")
html = url.content
soup= BeautifulSoup(html,"html.parser")

main=soup.find('div',  class_='toc')

print(main)
data=[]

for vs in main.find_all('span', class_='toctext'):
    name=vs.text
    player=    data.append({
        "wikipedia":name})
print(data)
pd.DataFrame(data).to_csv("amitabh.csv")