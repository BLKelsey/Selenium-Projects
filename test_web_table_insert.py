from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_web_table_page_loads():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    # -------------------------------
    # Verify page loaded
    # -------------------------------
    heading = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1"))
    )
    assert heading.text == "Web Tables"

    # -------------------------------
    # Open Add Record form
    # -------------------------------
    add_button = wait.until(
        EC.element_to_be_clickable((By.ID, "addNewRecordButton"))
    )
    add_button.click()

    # -------------------------------
    # Fill form fields
    # -------------------------------
    wait.until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys("Brian")
    driver.find_element(By.ID, "lastName").send_keys("Kelsey")
    driver.find_element(By.ID, "age").send_keys("56")
    driver.find_element(By.ID, "userEmail").send_keys("brian@example.com")
    driver.find_element(By.ID, "salary").send_keys("86500")
    driver.find_element(By.ID, "department").send_keys("Quality Assurance")

    # -------------------------------
    # Submit form
    # -------------------------------
    driver.find_element(By.ID, "submit").click()

    # -------------------------------
    # WAIT for React table to update
    # -------------------------------
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "div.ReactTable"),
            "Brian"
        )
    )

    # -------------------------------
    # Assertion
    # -------------------------------
    cells = driver.find_elements(By.CSS_SELECTOR, "div.rt-td")

    assert any("Brian" in cell.text for cell in cells), \
        "Row was not submitted to the table"

    driver.quit()
