import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Firefox()
driver.get("https://onlinebanking.bankmed.com.lb/index.html?module=login")

username_field = WebDriverWait(driver,15).until(
    EC.presence_of_element_located((By.ID,"login_username"))
)
password_field = driver.find_element(By.ID,"login_password")


username_field.send_keys("")
password_field.send_keys("") #why stalking?
password_field.send_keys(Keys.RETURN)

###
OK_btn = WebDriverWait(driver,30).until(
    EC.presence_of_element_located((By.XPATH,"//div[@class='button-container oj-flex']/button/div/span"))
)

OK_btn.click()


time.sleep(10)
