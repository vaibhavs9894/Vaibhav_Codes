import pandas as pd
import requests
from bs4 import BeautifulSoup


url=requests.get("https://www.youtube.com/")
html = url.content
soup= BeautifulSoup(html,"html.parser")

main=soup.find('div', class_='style-scope ytd-rich-grid-renderer')


data=[]

for vs in main.find_all('video-title-link'):
    name=vs.text
    player=    data.append({
        "title":name})
print(data)
pd.DataFrame(data).to_csv("youtube.csv")