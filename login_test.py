from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the OpenMRS login page
driver.get("https://qa.kenyahmis.org/openmrs/spa/login")

try:
    # Step 1: Enter the username and click "Continue"
    try:
        username_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
        username_field.send_keys("admin")
    except TimeoutException:
        print("Username field not found or not visible.")
        driver.save_screenshot('username_field_error.png')
        driver.quit()
        exit(1)

    # Find the "Continue" button and click it after entering the username
    try:
        continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        continue_button.click()
    except TimeoutException:
        print("Continue button not found or not clickable.")
        driver.save_screenshot('continue_button_error.png')
        driver.quit()
        exit(1)

    # Step 2: Wait for the password field to appear, then enter the password
    try:
        password_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        password_field.send_keys("Admin123")
    except TimeoutException:
        print("Password field not found or not visible.")
        driver.save_screenshot('password_field_error.png')
        driver.quit()
        exit(1)

    # Click the "Continue" button after entering the password
    try:
        continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        continue_button.click()
    except TimeoutException:
        print("Continue button not found or not clickable after password entry.")
        driver.save_screenshot('continue_button_post_password_error.png')
        driver.quit()
        exit(1)

    # Wait for a few seconds to let the login process complete
    time.sleep(5)
finally:
    # Close the browser
    driver.quit()
