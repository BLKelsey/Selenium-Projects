from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://www.qaplayground.com/practice")

# Click on "Toggle" section
toggle_link = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Toggle']"))
)
toggle_link.click()
print("Navigated to Toggle section.")

# ✅ WAIT for the heading (NO iframe)
element = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//p[contains(normalize-space(), 'Select any one')]")
    )
)
print(f"Located heading: '{element.text}'")

# Locate radio button
yes_radio = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[@type='radio' and @name='selectOne' and @value='yes']")
    )
)
yes_radio.click()
# Validation — this should FAIL the test if wrong
assert yes_radio.is_selected(), "Yes radio button was not selected"
print("PASS: 'Yes' radio button is selected.")
