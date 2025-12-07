from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/js/")
wait = WebDriverWait(driver, 10)

login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
login_link.click()

Username = "oleg"
Password = "090908"

username = driver.find_element(By.NAME, "username")
username.clear()
username.send_keys(Username)
password = driver.find_element(By.NAME, "password")
password.clear()
password.send_keys(Password)
password.send_keys(Keys.RETURN)


quotes = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "text")))

for e in quotes:
    print(e.text)
    
driver.close()

