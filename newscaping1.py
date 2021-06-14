from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
from PIL import Image
from pandas import pd
driver = webdriver.Chrome(ChromeDriverManager().install())

url ="https://worldpopulationreview.com/country-rankings/happiest-countries-in-the-world"
driver.get(url)
time.sleep(2)
