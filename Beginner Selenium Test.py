from selenium import webdriver                                    # Main Selenium browser controller
from selenium.webdriver.common.by import By                       # Used to locate elements (id, text, xpath, etc.)
from selenium.webdriver.support.ui import WebDriverWait           # Allows waiting for conditions
from selenium.webdriver.support import expected_conditions as EC  # Common wait conditions
import time                                                       # Used for pauses (sleep)

#first test

# ─────────────────────────────
# Start browser
# ─────────────────────────────
driver = webdriver.Chrome()                         # Launch a new Chrome browser
wait = WebDriverWait(driver, 10)                    # Reusable wait object

driver.get("https://thefederalist.com")             # Open the Federalist homepage

# Make sure page loads
wait.until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)

driver.maximize_window()                            # Maximize browser window (avoid mobile layout)
print("Home page loaded")                           # Console message for debugging

# ─────────────────────────────
# Click "Latest"
# ─────────────────────────────
latest_link = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Latest']")
    )
)

print("Clicking Latest...")
latest_link.click()

# ─────────────────────────────
# Verify navigation
# ─────────────────────────────
WebDriverWait(driver, 15).until(
    EC.url_contains("latest")
)

print("Latest page loaded")

# ─────────────────────────────
# Slow scrolling
# ─────────────────────────────
print("Starting slow scroll...")

for i in range(8):
    driver.execute_script("window.scrollBy(0, 90);")
    time.sleep(1)

print("Scrolling finished")

# ─────────────────────────────
# Keep browser open
# ─────────────────────────────
input("Press ENTER to close the browser...")
driver.quit()
