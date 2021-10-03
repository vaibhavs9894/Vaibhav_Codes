from typing import Collection
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

url ="https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW"
driver.get(url)
time.sleep(2)

main_area = driver.find_element_by_css_selector("table.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.scrolling-data-table")
movie_titles = main_area.find_elements_by_css_selector("table.a-bordered.a-horizontal-stripes.a-td.a-text-left.mojo-field-type-title")
movie_Collection = main_area.find_elements_by_css_selector('table.a-bordered.a-horizontal-stripes.a-size-td.a-text-right.mojo-field-type-money')
print(movie_ti)
data = []
for title,Collect in zip(movie_titles,movie_Collection):
    data.append({
        "Title":title,
        "Collection":Collect
            })

driver.close()
print(data)
pd.DataFrame(data).to_csv("Box_Office_Collection.csv")