import time
import json
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

f = open("cred.json")
creds = json.load(f)

username_field.send_keys(creds["username"])
password_field.send_keys(creds["password"]) 
password_field.send_keys(Keys.RETURN)

###
try:
    time.sleep(5)
    OK_btn = WebDriverWait(driver,30).until(
        EC.presence_of_element_located((By.ID,"ui-id-1"))
    )

    OK_btn.click()
except:
    pass

rows = 1+len(driver.find_elements(By.XPATH, 
    "//table[@id='SummaryTable']/tbody/tr")) 
  
# Obtain the number of columns in table 
cols = len(driver.find_elements(By.XPATH, 
    "//table[@id='SummaryTable']/tbody/tr[1]/td")) 
  
# Print rows and columns 


value = driver.find_element(By.XPATH, 
    "//table[@id='SummaryTable']/tbody/tr["+str(2)+"]/td["+str(7)+"]").text 
print(value)
availabe_usd_balance = value.replace("$","")

if (float(availabe_usd_balance)>200):
    print("new money")
else:
    print("no money no honey")

