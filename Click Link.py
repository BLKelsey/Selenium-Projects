from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
 

driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
driver.get("https://www.qaplayground.com/practice")

# Wait for the link to be clickable
link = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Click")))

time.sleep(2)  # Just to visually confirm the link is ready

# Click the link
print("Clicking the link...")
link.click()
print("Link clicked.")

# Wait for navigation to complete

home_btn = wait.until(
    EC.element_to_be_clickable((By.ID, "button-color")))
time.sleep(2)  # Just to visually confirm the link is ready
home_btn.click()
time.sleep(2)  # Just to visually confirm the link is ready

print("Navigated back to home page.")

driver.quit()