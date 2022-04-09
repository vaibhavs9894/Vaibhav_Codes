from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

url ="https://en.wikipedia.org/wiki/List_of_highest-grossing_films"
driver.get(url)
time.sleep(2)

main_area = driver.find_element_by_css_selector("div.mw-parser-output")
rows = main_area.find_elements_by_css_selector('title')
print(rows)
data = []
for title in zip(rows):
    title = title
    
    data.append({
        "name":title,
        
    })

driver.close()
print(data)
pd.DataFrame(data).to_csv("Dark_Web.csv")