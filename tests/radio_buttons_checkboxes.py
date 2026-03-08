from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

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

# -------------------------------------------------
# FIRST RADIO GROUP — Select YES
# -------------------------------------------------
heading1 = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//p[contains(normalize-space(),'Select any one')]")
    )
)

print(f"Located 1st radio heading: '{heading1.text}'")

yes_radio_1 = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[@type='radio' and @name='selectOne' and @value='yes']")
    )
)

yes_radio_1.click()

assert yes_radio_1.is_selected(), "FAIL: First radio group 'Yes' was not selected"

# -------------------------------------------------
# SECOND RADIO GROUP — Select NO
# -------------------------------------------------
heading2 = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//p[contains(normalize-space(),'Confirm you can select only one radio button')]")
    )
)

print(f"Located 2nd radio heading: '{heading2.text}'")

no_radio_2 = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[@type='radio' and @name='confirm' and @value='no']")
    )
)

no_radio_2.click()

assert no_radio_2.is_selected(), "FAIL: Second radio group 'No' was not selected"

# -------------------------------------------------
# CHECKBOX — Verify checked by default
# -------------------------------------------------
checkbox_heading = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//p[contains(normalize-space(),'Find if the checkbox is selected')]")
    )
)

print(f"Located checkbox heading: '{checkbox_heading.text}'")

checkbox = wait.until(
    EC.presence_of_element_located((By.XPATH, "//button[@role='checkbox']"))
)

assert checkbox.get_attribute("data-state") == "checked", "FAIL: Checkbox is NOT checked by default"

# -------------------------------------------------
# Cleanup
# -------------------------------------------------
driver.quit()