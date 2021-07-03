from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.cricbuzz.com/cricket-team/india/2/stats'
driver.get(url)
time.sleep(2)
table = driver.find_element_by_css_selector('.cb-series-stats')
target = table.find_element_by_css_selector("tbody")
rows =  target.find_elements_by_css_selector('.cb-srs-stats-tr')
print(len(rows))
for row in rows:
    player = row.find_element_by_css_selector('td:nth-child(1)')
    matches = row.find_element_by_css_selector('td:nth-child(2)')
    inns = row.find_element_by_css_selector('td:nth-child(3)')
    runs = row.find_element_by_css_selector('td:nth-child(4)')
    avg = row.find_element_by_css_selector('td:nth-child(5)')
    sr = row.find_element_by_css_selector('td:nth-child(6)')
    print(player.text)
    print(matches.text)
    print(inns.text)
    print(runs.text)
    print(avg.text)
    print(sr.text)
    print()
driver.close()