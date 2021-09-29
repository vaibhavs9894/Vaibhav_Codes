from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

url ="https://www.himalayanwritingretreat.com/bestselling-books-in-india/"
driver.get(url)
time.sleep(2)

main_area = driver.find_element_by_css_selector("tbody")  
print(main_area) 

'''

Book_titles = main_area.find_elements_by_css_selector("div.amzn-ad-prod-detail")
Book_author = main_area.find_elements_by_css_selector('div.thrv_wrapper thrv_text_element')

data = []
for title,author in zip(Book_titles,Book_author):
    name = title
    
    author = author
    data.append({
        "name":name,
        'author':author,
    })

driver.close()
print(data)
pd.DataFrame(data).to_csv("Top_Selling_Books.csv")
'''