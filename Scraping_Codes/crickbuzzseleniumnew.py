from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

url ="https://www.cricbuzz.com/cricket-team/india/2/stats"
driver.get(url)
time.sleep(2)

main_area = driver.find_element_by_css_selector("table.table table-responsive cb-series-statst")
rows = main_area.find_elements_by_css_selector("tr.cb-srs-stats-tr")


data = []   
for record in rows:
    print(record)
    name = record.find_element_by_css_selector('td:nth-child(1)').text
    matches = record.find_element_by_css_selector('td:nth-child(2)').text
    inns = record.find_element_by_css_selector('td:nth-child(3)').text
    runs = record.find_element_by_css_selector('td:nth-child(4)').text

    data.append({
        "name":name,
        'Matches':matches,
        'Inns':inns,
        'Runs':runs
    })

driver.close()
pd.DataFrame(data).to_csv("TopCriketerNew.csv")