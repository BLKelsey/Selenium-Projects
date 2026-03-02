# pyright: reportUnusedFunction=false

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_valid_login():
    # Create a new Chrome browser session
    driver = webdriver.Chrome()

    # Create explicit wait (max 10 seconds)
    wait = WebDriverWait(driver, 10)

    # Navigate to login page
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Enter valid username
    driver.find_element(By.NAME, "username").send_keys("student")

    # Enter valid password
    driver.find_element(By.NAME, "password").send_keys("Password123")

    # Click the login (submit) button
    driver.find_element(By.ID, "submit").click()

    # Wait until the URL changes to confirm successful login
    wait.until(EC.url_contains("logged-in-successfully"))

    # Verify success message is displayed on the page
    assert "Logged In Successfully" in driver.page_source

    # Close the browser session
    driver.quit()


def test_invalid_login():
    # Create a new Chrome browser session
    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 10)    
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Enter invalid username
    driver.find_element(By.NAME, "username").send_keys("invalid_user")

    # Enter invalid password
    driver.find_element(By.NAME, "password").send_keys("wrong_password")

    # Click login button
    driver.find_element(By.ID, "submit").click()

    # Wait for the error message element to appear
    wait.until(EC.presence_of_element_located((By.ID, "error")))

    # Verify that the correct error message is displayed
    assert "Your username is invalid!" in driver.page_source    

    # Close the browser session
    driver.quit()