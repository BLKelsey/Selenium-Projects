from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ─────────────────────────────
# Setup
# ─────────────────────────────
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)   # This doesn’t pause anything. It just initializes the wait object so you can use it later.
                                          # example:  wait.until(EC.visibility_of_element_located((By.ID, "login")))

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

# ─────────────────────────────
# Locate login fields
# ─────────────────────────────

username_field = wait.until(
    EC.presence_of_element_located((By.ID, "username"))          # Waits until the username input exists, then stores it for interaction
)
password_field = driver.find_element(By.ID, "password")     # Locates the password input field

# ─────────────────────────────
# TEST 1: Valid Login
# ─────────────────────────────
username_field.send_keys("tomsmith")
time.sleep(1)  # slow down typing

password_field.send_keys("SuperSecretPassword!")
time.sleep(1)

password_field.send_keys(Keys.RETURN)       # Submits the login form by pressing Enter
time.sleep(2)  # wait to see result

# Assert successful login
flash_message = wait.until(
    EC.presence_of_element_located((By.ID, "flash"))      # Waits for the login result message to appear
)

assert "You logged into a secure area!" in flash_message.text    # Verifies the success message is displayed

print("✅ Valid login passed")
time.sleep(3)

# Logout
driver.find_element(By.LINK_TEXT, "Logout").click()     # Clicks the Logout link to exit the secure area
time.sleep(2)

# ─────────────────────────────
# TEST 2: Invalid Login
# ─────────────────────────────
username_field = wait.until(
    EC.presence_of_element_located((By.ID, "username"))
)
password_field = driver.find_element(By.ID, "password")

username_field.clear()          # Clears the username input field
password_field.clear()

username_field.send_keys("invalid_user")
time.sleep(1)

password_field.send_keys("wrong_password")
time.sleep(1)

password_field.send_keys(Keys.RETURN)
time.sleep(2)

# Assert error message
flash_message = wait.until(
    EC.presence_of_element_located((By.ID, "flash"))     # Waits for the login result message to appear
)

assert "Your username is invalid!" in flash_message.text

print("✅ Invalid login passed")
time.sleep(3)

# ─────────────────────────────
# Cleanup
# ─────────────────────────────
input("Press ENTER to close the browser...")
driver.quit()
