from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://www.qaplayground.com/practice")

# Navigate to "Select By"
select_by_link = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Select By']")))

select_by_link.click()
print("Navigated to Select By section.")

# Locate dropdown
dropdown = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']"))
)

# Verify placeholder
print(f"Initial dropdown text: '{dropdown.text}'")
assert dropdown.text.strip() == "Select Fruit"

# Open dropdown
dropdown.click()

# Select Banana
banana_option = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[@role='option' and normalize-space()='Banana']")))
banana_option.click()

# ✅ Verify selection via visible text (correct for this UI)
wait.until(
    EC.text_to_be_present_in_element(
        (By.XPATH, "//button[@role='combobox']"),
        "Banana"))

assert dropdown.text.strip() == "Banana"

print("SUCCESS: Banana was selected correctly within the dropdown.")
