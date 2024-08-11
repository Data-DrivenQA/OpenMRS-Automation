from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the OpenMRS login page
driver.get("https://qa.kenyahmis.org/openmrs/spa/login")

try:
    # Step 1: Enter the username and click "Continue"
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_field.send_keys("admin")

    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    continue_button.click()

    # Step 2: Wait for password field to appear, then enter password and click "Continue"
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_field.send_keys("Admin123")

    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    continue_button.click()

    # Step 3: Verify successful login by checking for the presence of a unique element
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-extension-id='active-visits-tile']"))
    )

    print("Login successful! Dashboard element found.")

finally:
    # Close the browser
    driver.quit()
