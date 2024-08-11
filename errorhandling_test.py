from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the OpenMRS login page
driver.get("https://qa.kenyahmis.org/openmrs/spa/login")

try:
    # Step 1: Enter the username and click "Continue"
    username_field = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_field.send_keys("incorrect_username")  # Use a wrong username for testing

    continue_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    continue_button.click()

    # Step 2: Wait for the password field to appear, then enter the password and click "Continue"
    password_field = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_field.send_keys("Admin123")  # Use any password for testing

    continue_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    continue_button.click()

    # Step 3: Check for the "Invalid username or password" error message after password submission
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cds--inline-notification__subtitle"))
        )
        if "Invalid username or password" in error_message.text:
            print("Login failed: Invalid username or password.")
        else:
            print("Error message found but does not indicate invalid credentials.")
    except TimeoutException:
        # Check for any generic error message
        print("Error message not found; login might have succeeded or element might be missing.")
        # Capture the page source for further debugging
        with open("page_source.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)
        print("Page source saved as 'page_source.html' for debugging.")

except Exception as e:
    # Handle any other exceptions
    driver.save_screenshot('error_screenshot.png')
    print(f"An error occurred: {e}")
    print("Screenshot saved as 'error_screenshot.png'.")

finally:
    # Close the browser
    driver.quit()
