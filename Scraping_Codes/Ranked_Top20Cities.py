from typing import Collection
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

url ="https://www.forbes.com/sites/laurabegleybloom/2020/03/20/ranked-20-happiest-countries-2020/?sh=3438a4587850"
driver.get(url)
time.sleep(2)

main_area = driver.find_element_by_css_selector("div.article-body.fs-article.fs-responsive-text.current-article")
City_titles = main_area.find_elements_by_css_selector("td.a-text-left.mojo-field-type-title")
movie_Collection = main_area.find_elements_by_css_selector('td.a-text-right.mojo-field-type-money')
#print(main_area.text)

data = []
for t in main_area.find_elements_by_css_selector("li"):
    
    data.append({
        "Title":t.text        
            })

driver.close()
print(data)
pd.DataFrame(data).to_csv("Ranked_top20Cities.csv")
