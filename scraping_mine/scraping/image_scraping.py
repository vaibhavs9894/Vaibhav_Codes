from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
search_term = "earbuds"
website_url = f"https://www.google.com/search?q={search_term}&newwindow=1&safe=active&sxsrf=ALeKk033gsfNuTuSJ1ItSqtxKNROaWNlew:1623237196014&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj0jNHjtYrxAhXBAnIKHSS2B6kQ_AUoAXoECAIQAw&cshid=1623237325608918&biw=958&bih=969"

driver.get(website_url) 
while True:
    driver.execute_script("window.scrollTo(0,10000);")
    time.sleep(2) # wait for 5 seconds
    print("scrolled")