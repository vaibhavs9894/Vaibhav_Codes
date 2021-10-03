import pandas as pd
from bs4 import BeautifulSoup
import requests
url=requests.get("https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW")

html=url.content
soup=BeautifulSoup(html,"html.parser")
main=soup.find('div',class_='a-section imdb-scroll-table-inner')
title=soup.find('a',class_ ='a-link-normal')
Boxoffice=soup.find('td',class_ ='a-text-right mojo-field-type-money')
data=[]
#for vs in main.find_all('tr', class_='cb-srs-stats-tr'):
  #  name=vs.text
i=1
j=2
a=0
for v in main.find_all('a'):
    a=a+1
    if a==i:
        i=i+2
        title=v.text
    if a==j:
        j=j+2
        year=v.text
        data.append({
        "Title":title,
        "year":year})
print(data)
pd.DataFrame(data).to_csv("Box_Office_Collections.csv")
    
    
