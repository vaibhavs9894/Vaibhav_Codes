from bs4.element import AttributeValueWithCharsetSubstitution
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


r = requests.get("https://www.rottentomatoes.com/top/bestofrt/")
htmlContent = r.content   
soup= BeautifulSoup(htmlContent,"html.parser")
print(soup.prettify)
title=soup.title
print(title)
paras= soup.find_all('p')

anchors=soup.find_all('a')
print(anchors)
print(soup.find('p'))
print(soup.find('p')['class'])

print(soup.find_all('a', class_="unstyled articleLink"))
print(soup.find("p").get_text())
print(soup.get_text())