from temp6 import Price_compare
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

url ="https://www.amazon.in/s?k=earbuds"
driver.get(url)
time.sleep(2)

main_area = driver.find_element_by_css_selector("div.s-desktop-width-max.s-opposite-dir")
name = main_area.find_elements_by_css_selector("span.a-size-medium a-color-base a-text-normal")
price = main_area.find_elements_by_css_selector('span.a-price-whole')

data = []
for a,b in zip(name,price):
    data.append({
        "name":a,
        'price':b})

driver.close()
pd.DataFrame(data).to_csv("Amazon_price.csv")