from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
website_url = "https://www.google.co.in/search"

# load a website
search_term = "earbuds"
driver.get(website_url+"?q="+search_term) 
# driver.get(f"{website_url}?q={search_term}")