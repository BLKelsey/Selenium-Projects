import os                               # Used to safely expand "~" into a full filesystem path
import time                             # Used for simple delays (sleep) when waiting for tab behavior
from selenium import webdriver          # Controls the browser
from selenium.webdriver.common.by import By   # Provides locator strategies (ID, LINK_TEXT, etc.)
from selenium.webdriver.support.ui import WebDriverWait   # Explicit wait utility
from selenium.webdriver.support import expected_conditions as EC  # Conditions used with waits

driver = webdriver.Chrome()             
print("Browser started")               

wait = WebDriverWait(driver, 10)         # Creates a wait object with a 10-second timeout

driver.get("https://webdriveruniversity.com")  
print("Opened WebDriver University homepage")  # Confirms navigation

driver.maximize_window()                
print("Browser window maximized")        

try:
    mastering_locators = wait.until(    # Waits until the "Mastering Locators" link is clickable
        EC.element_to_be_clickable((By.LINK_TEXT, "Mastering Locators"))
    )
    print("Mastering Locators button located")  

    mastering_locators.click()           # Clicks the "Mastering Locators" button
    print("Clicked Mastering Locators button")  

    # Give the browser a moment to open a new tab (if it will)
    time.sleep(2)                        # Small pause to allow new tab creation

  
    wait.until(EC.title_contains("Mastering Selectors"))  # Waits until Udemy page title loads
    print("Udemy page title loaded")       # Confirms title condition met

    page_title = driver.title                   # Retrieves the current page title
    print("Retrieved page title:", page_title)  # Prints the page title

    assert "Mastering Selectors" in page_title  # Verifies correct Udemy course page opened
    print("Verified page title contains expected text")  # Confirms assertion success

    print("✅ TEST PASSED")                # Final success message

except Exception as e:
    print("❌ TEST FAILED")                # Indicates test failure
    print("Failure reason:", e)            # Prints the exception message

    screenshot_path = os.path.expanduser( # Builds a valid absolute path for the screenshot
        "~/Documents/Selenium-Projects/Test pics/Failures/mastering_locators_failure.png")
   
    driver.get_screenshot_as_file(screenshot_path)  # Captures a screenshot of the failure state
    print("Screenshot captured at:", screenshot_path)  # Confirms screenshot location

finally:
    input("Press ENTER to close the browser...")  # Pauses execution so you can inspect the browser
    driver.quit()                                 # Closes the browser and ends the session
    print("Browser closed")                       # Confirms cleanup
