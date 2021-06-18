from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.rottentomatoes.com/top/bestofrt/"
driver.get(url)
time.sleep(2)

target = driver.find_element_by_css_selector("table.table")
rows = target.find_elements_by_css_selector("a.unstyled articleLink")
#print(len(rows),'records found')
print(rows.txt)

for i in rows:
    c= i.find_element_by_css_selector('td:nth-child(1)').text
    print(i)


'''
for record in rows:
    country = record.find_element_by_css_selector('td:nth-child(1)').text
    rank = record.find_element_by_css_selector('td:nth-child(2)').text
    score = record.find_element_by_css_selector('td:nth-child(3)').text
    pop = record.find_element_by_css_selector('td:right hidden-xs').text

    print(country, rank, score, pop)
'''
driver.close()