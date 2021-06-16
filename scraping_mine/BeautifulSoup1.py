import requests
from bs4 import BeautifulSoup

req= requests.get("https://www.rottentomatoes.com/top/bestofrt/")

soup= BeautifulSoup(req.content,"html.parser")
a=soup.prettify()
#print(soup.prettify())
#print(a)
reqs=soup.title
#print(reqs.prettify())
anchors= soup.find_all('tr') 
#print(anchors)
print(soup.find('tr')['class'])
print(soup.find_all("tr", class_="tvTopListTitle"))
