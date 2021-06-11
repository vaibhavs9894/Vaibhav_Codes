
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
search_term = "earbuds"
website_url = f"https://www.google.com/search?q={search_term}&sxsrf=ALeKk00TRZHhw6JKknTdM3nmlBTwq26Yxw:1623236778948&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjEseGctIrxAhVtgtgFHUcgDdIQ_AUoAnoECAEQBA&biw=1536&bih=760"


driver.get(website_url)
driver.execute_script('window.scrollTo(0,10000);")
time.sleep(5)

