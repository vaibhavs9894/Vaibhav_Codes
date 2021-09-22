#EDA on world happiness report 2021

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

url ="https://www.himalayanwritingretreat.com/bestselling-books-in-india/"
driver.get(url)
time.sleep(2)

main_area = driver.find_element_by_css_selector("tbody.tve-u-17aa9ae96d3")
print(main_area)
'''
Book_titles = main_area.find_elements_by_css_selector("td.titleColumn")
Book_author = main_area.find_elements_by_css_selector('td.ratingColumn.imdbRating')

data = []
for title,rating in zip(Book_titles,Book_author):
    title_n_year = title.text
    name = title_n_year.split(maxsplit=1)[1].rsplit(maxsplit=1)[0]
    year = title_n_year.rsplit(maxsplit=1)[1][1:-1]
    data.append({
        "name":name,
        'year':year,
        'rating':float(rating.text)
    })

driver.close()
print(data)
pd.DataFrame(data).to_csv("Top_Selling_Books.csv")
'''