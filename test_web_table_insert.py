from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_web_table_page_loads():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    heading = driver.find_element(By.TAG_NAME, "h1")              # Locate the main page heading (<h1>)
    assert heading.text == "Web Tables", "Page title does not match expected title."

    table = wait.until(                                           # Wait until the web table exists
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.ReactTable"))
    )

    add_button = driver.find_element(By.ID, "addNewRecordButton") # Locate the "Add" button
    add_button.click()                                            # Simulate user clicking Add

    cells = table.find_elements(By.CSS_SELECTOR, "div.rt-td")     # Collect all visible table cells
    assert len(cells) > 0                                         # Ensure table is not empty

    driver.quit()                                                  # Close browser after test
    print("Web Table page loaded and table is present.")
