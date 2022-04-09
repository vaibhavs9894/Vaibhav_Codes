from typing import Collection
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

url ="https://www.brandwatch.com/blog/top-most-instagram-followers/"
driver.get(url)
time.sleep(2)

main_area = driver.find_element_by_css_selector("div.mt9.c-blocktone-light-lightest.relative")
Celeb_name = main_area.find

print(Celeb_name.text)
'''
data = []
for t,c in zip(movie_titles,movie_Collection):
    
    data.append({
        "Title":t.text,
        "Lifetime_Grossing":c.text
        
            })

driver.close()
print(data)
pd.DataFrame(data).to_csv("Insta_Followers_Top_List.csv")
'''