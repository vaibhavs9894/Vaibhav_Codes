import requests
from bs4 import BeautifulSoup
import pandas as ps
from selenium import webdriver
from webdriver_manager import driver_cache
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
url="https://www.sarkariresult.com/latestjob/"
driver.get(url)

main_area=driver.find_element_by_css_selector("")