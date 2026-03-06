from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://demo.guru99.com/test/delete_customer.php")

# Enter customer ID
driver.find_element(By.NAME, "cusid").send_keys("123")

# Click submit
driver.find_element(By.NAME, "submit").click()

# Wait for first alert
first_alert = wait.until(EC.alert_is_present())

# Capture the message
print("FirstAlert text: ", first_alert.text)

# Click OK
first_alert.accept()

# Wait for second alert to delete the customer
second_alert = wait.until(EC.alert_is_present())

# Capture the message
print("Second Alert text: ", second_alert.text)

# Click OK
second_alert.accept()

driver.quit()