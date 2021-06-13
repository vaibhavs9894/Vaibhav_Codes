#EDA on world happiness report 2021

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

url ="https://worldpopulationreview.com/country-rankings/happiest-countries-in-the-world"
driver.get(url)
time.sleep(2)

main_area = driver.find_element_by_css_selector("section-container clearfix")
tr:nth-child(1)

'''
movie_titles = main_area.find_elements_by_css_console('$0')
movie_ratings = main_area.find_elements_by_css_selector('td.ratingColumn.imdbRating')

data = []
for title,rating in zip(movie_titles,movie_ratings):
    title_n_year = title.text
    name = title_n_year.split(maxsplit=1)[1].rsplit(maxsplit=1)[0]
    year = title_n_year.rsplit(maxsplit=1)[1][1:-1]
    data.append({
        "name":name,
        'year':year,
        'rating':float(rating.text)
    })

#driver.close()
pd.DataFrame(data).to_csv("top_movies.csv")'''