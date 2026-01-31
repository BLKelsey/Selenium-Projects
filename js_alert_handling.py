import time                                  # Used to add visible pauses during execution
from selenium import webdriver               # Core Selenium WebDriver
from selenium.webdriver.common.by import By  # Locator strategies (ID, NAME, XPATH, etc.)
from selenium.webdriver.support.ui import WebDriverWait  # Explicit waits
from selenium.webdriver.support import expected_conditions as EC  # Wait conditions


# =========================
# SETUP: Browser & Page
# =========================

driver = webdriver.Chrome()                  # Launch Chrome browser
driver.get("https://testpages.herokuapp.com/pages/basics/alerts-javascript/")  # Open test page
print("Page loaded")                         # Confirm page navigation

time.sleep(1)                                # Short pause so page fully settles


# =========================
# JS CONFIRM ALERT
# =========================
# Behavior: Shows OK / Cancel dialog
# Selenium action: accept() or dismiss()

confirm_button = WebDriverWait(driver, 10).until(      # Wait for Confirm button to exist in DOM
    EC.presence_of_element_located((By.ID, "confirmexample")))

driver.execute_script(                        # Execute JavaScript in browser context
    "arguments[0].scrollIntoView(true);",     # Selenium will inject confirm_button as arguments[0]
    confirm_button)                           # Pass WebElement as arguments[0]

time.sleep(0.5)                              # Allow layout to stabilize after scrolling

confirm_button.click()                       # Click "Show confirm box"
print("Clicked Show confirm box")             # Log click action

WebDriverWait(driver, 10).until(              # Wait until confirm alert appears
    EC.alert_is_present())

print("Confirm alert is present")             # Confirm alert detection

alert = driver.switch_to.alert                # Switch Selenium focus to alert
print("Alert text:", alert.text)              # Output alert message

time.sleep(1)                                 # Pause so alert text can be read

alert.accept()                                # Click OK on confirm alert
print("Confirm alert accepted")               # Log acceptance


# =========================
# CLEANUP
# =========================

time.sleep(1)                                 # Small pause before cleanup
driver.quit()                                 # Close browser and end session
