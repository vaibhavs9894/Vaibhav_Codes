from bs4 import BeautifulSoup
import requests
import pandas as pd

r = requests.get("https://www.rottentomatoes.com/top/bestofrt/")
htmlContent = r.content   
soup= BeautifulSoup(htmlContent,"html.parser")
main=soup.find('table', class_='table')

data=[]

for vs in main.find_all('a', class_='unstyled articleLink'):
    vs=vs.text 
    
    data.append({
        "name":vs
        })
    
print(data)
pd.DataFrame(data).to_csv("top_rottenmovies.csv")
