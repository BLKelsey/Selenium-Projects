from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://www.qaplayground.com/practice")

# -------------------------------------------------
# Navigate to Toggle section
# -------------------------------------------------
toggle_link = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Toggle']"))
)
toggle_link.click()
print("Navigated to Toggle section.")
time.sleep(2)

# -------------------------------------------------
# FIRST RADIO GROUP — Select YES
# -------------------------------------------------
heading1 = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//p[contains(normalize-space(), 'Select any one')]")
    )
)
print(f"Located 1st radio heading: '{heading1.text}'")
time.sleep(1)

yes_radio_1 = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[@type='radio' and @name='selectOne' and @value='yes']")
    )
)
yes_radio_1.click()
time.sleep(1)

assert yes_radio_1.is_selected(), "FAIL: First radio group 'Yes' was not selected"
print("PASS: First radio group - 'Yes' is selected.")
time.sleep(2)

# -------------------------------------------------
# SECOND RADIO GROUP — Select NO
# -------------------------------------------------
heading2 = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//p[contains(normalize-space(), 'Confirm you can select only one radio button')]")
    )
)
print(f"Located 2nd radio heading: '{heading2.text}'")
time.sleep(1)

no_radio_2 = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[@type='radio' and @name='confirm' and @value='no']")
    )
)
no_radio_2.click()
time.sleep(1)

assert no_radio_2.is_selected(), "FAIL: Second radio group 'No' was not selected"
print("PASS: Second radio group - 'No' is selected.")
time.sleep(2)

# -------------------------------------------------
# CHECKBOX — Verified checked by default
# -------------------------------------------------
checkbox_heading = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//p[contains(normalize-space(), 'Find if the checkbox is selected')]")
    )
)
print(f"Located checkbox heading: '{checkbox_heading.text}'")
time.sleep(1)

checkbox = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//button[@role='checkbox']")
    )
)

assert checkbox.get_attribute("data-state") == "checked", (
    "FAIL: Checkbox is NOT checked by default"
)
print("PASS: Checkbox is checked by default.")
time.sleep(2)

# -------------------------------------------------
# Final cleanup
# -------------------------------------------------
driver.quit()
print("Test completed successfully.")
