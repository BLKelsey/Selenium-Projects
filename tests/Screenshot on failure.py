import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

try:
    username = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password = driver.find_element(By.ID, "password")

    username.clear()
    password.clear()

    username.send_keys("invalid_user")
    password.send_keys("wrong_password")
    password.send_keys(Keys.RETURN)

    flash_message = wait.until(EC.presence_of_element_located((By.ID, "flash")))

    # INTENTIONALLY WRONG ASSERTION → forces failure
    assert "Welcome" in flash_message.text

    print("✅ Test passed")

except AssertionError:
    print("❌ Test failed – taking screenshot")

    screenshot_path = os.path.expanduser(
        "~/Documents/Selenium-Projects/Test pics/Failures/screenshot_on_failure.png"
    )

    driver.get_screenshot_as_file(screenshot_path)
    print(f"📸 Screenshot saved to: {screenshot_path}")

finally:
    input("Press ENTER to close the browser...")
    driver.quit()
