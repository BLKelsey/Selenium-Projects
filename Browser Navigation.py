import time                             # Used for simple delays (sleep) when waiting for tab behavior
from selenium import webdriver          # Controls the browser
from selenium.webdriver.common.by import By   # Provides locator strategies (ID, LINK_TEXT, etc.)
from selenium.webdriver.support.ui import WebDriverWait   # Explicit wait utility
from selenium.webdriver.support import expected_conditions as EC  # Conditions used with waits

driver = webdriver.Chrome()             
print("Browser started") 

wait = WebDriverWait(driver, 10)
driver.get("https://DTCC.com/")
print("Opened DTCC homepage")

heading = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "main_0_slidesRpt_h2Title_0")))
print("Located homepage heading"
heading_text = heading.text
print("Heading text:", heading_text)

assert "Navigating Transformation" in heading_text
print("Verified homepage heading")

# Click Products & Services
products_services = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "PRODUCTS & SERVICES")))
products_services.click()
print("Clicked Products & Services")

# Click Repository & Derivatives Services
repo_services = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "a[href='/repository-and-derivatives-services']")))
repo_services.click()
print("Clicked Repository & Derivatives Services")






