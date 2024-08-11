from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

print("Test Passed: Google website opened successfully.")
driver.quit()
