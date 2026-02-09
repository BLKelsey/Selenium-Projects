from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# -------------------------------
# Helper functions
# -------------------------------

def fill_field(driver, field_id, value):
    """Fill a form input by ID."""
    driver.find_element(By.ID, field_id).send_keys(value)


def get_row_count(driver):
    """Return number of visible table rows."""
    return len(driver.find_elements(By.CSS_SELECTOR, "div.rt-tr-group"))


# -------------------------------
# Test
# -------------------------------

def test_web_table_insert():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # -------------------------------
        # Arrange: Open page
        # -------------------------------
        driver.get("https://demoqa.com/webtables")
        driver.maximize_window()

        heading = wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )
        assert heading.text == "Web Tables"

        # -------------------------------
        # Arrange: Capture baseline
        # -------------------------------
        before_count = get_row_count(driver)
        print(f"Rows before insert: {before_count}")

        # -------------------------------
        # Act: Open Add Record form
        # -------------------------------
        driver.find_element(By.ID, "addNewRecordButton").click()

        # -------------------------------
        # Act: Fill form
        # -------------------------------
        form_data = {
            "firstName": "Brian",
            "lastName": "Kelsey",
            "age": "56",
            "userEmail": "brian@example.com",
            "salary": "86500",
            "department": "Quality Assurance",
        }

        for field_id, value in form_data.items():
            fill_field(driver, field_id, value)

        driver.find_element(By.ID, "submit").click()

        # -------------------------------
        # Assert: Row count increased
        # -------------------------------
        wait.until(
    lambda d: any("Brian" in cell.text for cell in d.find_elements(By.CSS_SELECTOR, "div.rt-td")))

        cells = driver.find_elements(By.CSS_SELECTOR, "div.rt-td")
        assert any("Brian" in cell.text for cell in cells), "Inserted row not found in table"

    finally:
        driver.quit()