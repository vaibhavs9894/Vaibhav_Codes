
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
website_url = "https://www.google.com/search"

search_term="earbuds"
driver.get(website_url+"?q="+search_term)