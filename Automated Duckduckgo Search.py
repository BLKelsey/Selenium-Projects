from selenium.webdriver.common.keys import Keys                   # Imports keyboard key constants (like ENTER, TAB, ESC, ARROW keys)
                                                                  # so Selenium can simulate real keyboard input,
from selenium import webdriver                                    # Main Selenium browser controller
from selenium.webdriver.common.by import By                       # Used to locate elements (id, text, xpath, etc.)
from selenium.webdriver.support.ui import WebDriverWait           # Allows waiting for conditions
from selenium.webdriver.support import expected_conditions as EC  # Common wait conditions
#import time                                                       # Used for pauses (sleep)

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://duckduckgo.com")
driver.maximize_window()

# Wait for search box
search_box = wait.until(
    EC.presence_of_element_located((By.NAME, "q"))
)

# Type query
search_box.send_keys("Selenium automation best practices")

# Submit search
search_box.send_keys(Keys.ENTER)

# ✅ Correct wait for DuckDuckGo results
wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "a.result__a")))


print("Search successful!")
print("Page title:", driver.title)

input("Press Enter to close the browser...")
driver.quit()
