from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#-------------------------------------------
#TO FAIL ON PURPOSE (hard assertion failure)
#-------------------------------------------

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/notification_message_rendered")

h3_element = wait.until(                                   # Wait until an <h3> element is visible on the page
    EC.visibility_of_element_located((By.TAG_NAME, "h3"))  # Locate the element by its HTML tag <h3>
)

actual_text = h3_element.text.strip()                     # Read the text inside <h3> and remove extra spaces
expected_text = "Maintenance Notification"                # Define the text we expect to see

assert actual_text == expected_text, (                    # Force test to FAIL if text does not match
    f"TEST FAILED ❌\n"                                   # Clear failure indicator
    f"Expected h3 text: '{expected_text}'\n"              # Show what was expected
    f"Actual h3 text:   '{actual_text}'")                  # Show what the UI actually displayed

print("TEST PASSED ✅")  # If assertion passes, indicate success

driver.quit()
