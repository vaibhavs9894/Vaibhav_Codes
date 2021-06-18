import pandas as pd
from bs4 import BeautifulSoup
import requests
url=requests.get("https://www.deccanchronicle.com/lifestyle/books-and-art/271120/top-10-indian-best-selling-books-fiction-and-non-fiction.html")

html=url.content
soup=BeautifulSoup(html,"html.parser")
main=soup.find('div',class_='story-body')

data=[]
for vs in main.find_all('em'):
    name=vs.text
    data.append({
        "Player":name})
print(data)
pd.DataFrame(data).to_csv("Books.csv")
    
    
