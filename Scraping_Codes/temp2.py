from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

url ="https://www.himalayanwritingretreat.com/bestselling-books-in-india/#tve-jump-17aaf315541"
driver.get(url)
time.sleep(2)

main_area = driver.find_element_by_css_selector("div.thrv_wrapper thrv_table tcb-fixed tcb-mobile-table")
movie_titles = main_area.find_elements_by_css_selector("td.titleColumn")
movie_ratings = main_area.find_elements_by_css_selector('td.ratingColumn.imdbRating')

data = []
for vs in zip(main_area):
    name=vs
    data.append({
        "name":name
            })

driver.close()
print(data)
#pd.DataFrame(data).to_csv("top_movies.csv")