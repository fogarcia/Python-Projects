from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Correct the path and initialize the Service
driver_path = r"C:\Users\garci\Downloads\chrome-win64\chrome.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Open a website to test if Chrome launches
driver.get("https://google.com")
