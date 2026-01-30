from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://practice-automation.com/")
currenet_url = driver.current_url
print("Opened Practice Automation homepage")

driver.maximize_window()
print("Browser window maximized")

page_title = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "h1")))

print("Located main heading element")

assert page_title.is_displayed(), "Main heading is not displayed on the page"
print("Verified main heading is displayed")

heading_text = page_title.text
print("Main heading text:", heading_text)

expected_text = "Welcome to your software automation practice website!"
assert heading_text == expected_text, f"Expected heading text '{expected_text}', but got '{heading_text}'"
print("Verified main heading text matches expected text")
    
  



    
    
    
    
  
