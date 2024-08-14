import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

while True:
    try:
        # Install and set up the Chrome driver
        #service = Service(ChromeDriverManager().install())
        driver = webdriver.Firefox()

        # Go to the login page
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # Please replace with the actual URL

        # Find the username and password fields
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))  # Adjust the locator as needed
        )
        password_field = driver.find_element(By.NAME, "password")  # Adjust the locator as needed

        # Enter your credentials (be careful with sensitive information!)
        username_field.send_keys("Admin")  # Replace with your username
        password_field.send_keys("admin123")  # Replace with your password

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Wait until the next page loads (you might need to adjust the condition)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "orangehrm-dashboard-widget-name")))  # Adjust the condition as needed

        link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/web/index.php/pim/viewMyDetails']"))  # Adjust the href value as needed
        )

        # Click the link
        link.click()   

        text_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "firstName"))  # Adjust the locator as needed
        )

        # Get the value of the text field
        text_value = text_field.get_attribute("value")

        time.sleep(2)
        print(text_value)

    except Exception as e:
        print(f"Oh no, something went wrong: {e}")

    finally:
        # Close the browser after a short delay to see the result
        
        time.sleep(5)
        driver.quit()