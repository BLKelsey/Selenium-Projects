import time                                    # Used for small, controlled delays (menu animations)
from selenium import webdriver                 # Core Selenium WebDriver
from selenium.webdriver.common.by import By    # Locator strategies (ID, CSS, XPATH, etc.)
from selenium.webdriver.support.ui import WebDriverWait  # Explicit wait mechanism
from selenium.webdriver.support import expected_conditions as EC  # Conditions for waits
from selenium.webdriver.common.action_chains import ActionChains  # For hover interactions
from selenium.webdriver.chrome.options import Options              # Chrome configuration


# ─────────────────────────────
# Browser setup
# ─────────────────────────────

options = Options()                            # Create Chrome options object
options.page_load_strategy = "eager"           # Load DOM early (don’t wait for analytics)

driver = webdriver.Chrome(options=options)     # Start Chrome browser with options
print("Browser started")

driver.set_page_load_timeout(15)               # Prevent infinite page-load hangs
wait = WebDriverWait(driver, 15)                # Global explicit wait (15 seconds)
actions = ActionChains(driver)                  # ActionChains for hover behavior


# ─────────────────────────────
# Open site
# ─────────────────────────────

try:
    driver.get("https://www.dtcc.com")          # Navigate to DTCC homepage
    print("Opened DTCC homepage")
except:
    print("Page load timed out, continuing anyway")  # Continue even if full load times out

driver.maximize_window()                        # Maximize browser window
print("Browser window maximized")


# ─────────────────────────────
# Handle cookie consent
# ─────────────────────────────

try:
    accept_cookies = WebDriverWait(driver, 5).until(   # Short wait for cookie modal
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Accept All Cookies']")))  
    accept_cookies.click()                      # Accept cookies to unblock UI
    print("Accepted cookies")
except:
    print("No cookie banner present")           # Continue if banner doesn’t appear


# ─────────────────────────────
# Verify homepage heading
# ─────────────────────────────

heading = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "main_0_slidesRpt_h2Title_0")))    # Locate homepage heading
print("Located homepage heading")

heading_text = heading.text                    # Extract visible text from heading
print("Heading text:", heading_text)

assert "Navigating Transformation" in heading_text  # Validate expected heading content
print("Verified homepage heading")


# ─────────────────────────────
# Hover Products & Services
# ─────────────────────────────

products_services_container = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "ctl14_header_1_rptFirstLevelNavigation_li2LevelsSubLinks_0")))

actions.move_to_element(products_services_container).perform()  # Hover parent menu container
print("Hovered over Products & Services container")

time.sleep(1)                                # Allow submenu animation to complete


# ───────────────────────────────────────
# Click Repository & Derivatives Services
# ───────────────────────────────────────

repo_services = wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "a.main-navigation__secondary-item-link.side-arrow")))

wait.until(EC.visibility_of(repo_services))   # Ensure submenu link is visible
print("Repository & Derivatives Services link is visible")

repo_services.click()                         # Click submenu link
print("Clicked Repository & Derivatives Services")


# ──────────────────────────────────────
# EXPECTED RESULT: BOT PROTECTION BLOCK
# ──────────────────────────────────────

block_message = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(), 'you have been blocked')]")))

block_text = block_message.text.lower()       # Normalize text for assertion
print("Block page message detected:", block_text)

assert "blocked" in block_text                # Validate expected bot-protection behavior
print("✅ Verified DTCC blocks automated browser access as expected")


# ─────────────────────────────
# Cleanup
# ─────────────────────────────

input("Press ENTER to close the browser...")   # Pause so user can view result
driver.quit()                                 # Close browser and end session
print("Browser closed")
