from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://worldpopulationreview.com/country-rankings/happiest-countries-in-the-world"
driver.get(url)
time.sleep(2)

target = driver.find_element_by_css_selector("tbody.jsx-2642336383")
rows = target.find_elements_by_css_selector('tr')
print(len(rows),' records found')

for record in rows:
    country = record.find_element_by_css_selector('td:nth-child(1)').text
    rank = record.find_element_by_css_selector('td:nth-child(2)').text
    score = record.find_element_by_css_selector('td:nth-child(3)').text
    pop = record.find_element_by_css_selector('td:nth-child(4)').text

    print(country, rank, score, pop)

driver.close()