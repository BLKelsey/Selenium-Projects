from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


def test_travel_agency_booking():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:

        driver.get("https://blazedemo.com/")

        # Select departure city
        driver.find_element(By.NAME, "fromPort").send_keys("Paris")

        # Select destination city
        driver.find_element(By.NAME, "toPort").send_keys("Cairo")

        # Click Find Flights
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='Find Flights']"))).click()

        # Choose Lufthansa flight
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//tr[td[normalize-space()='Lufthansa']]//input[@value='Choose This Flight']"))).click()

        # Fill purchase form
        driver.find_element(By.ID, "inputName").send_keys("Test User")
        driver.find_element(By.ID, "address").send_keys("123 Test Street")
        driver.find_element(By.ID, "city").send_keys("New York")
        driver.find_element(By.ID, "state").send_keys("NY")
        driver.find_element(By.ID, "zipCode").send_keys("10001")
        driver.find_element(By.ID, "creditCardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "nameOnCard").send_keys("Test User")

        # Click Purchase Flight
        driver.find_element(By.XPATH, "//input[@value='Purchase Flight']").click()

        # Verify confirmation page
        confirmation = wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )

        assert confirmation.text == "Thank you for your purchase today!"

        # Extract booking table
        rows = driver.find_elements(By.CSS_SELECTOR, "table tr")

        # Create an empty dictionary to store booking details extracted from the table
        data = {}

        # Loop through each row of the confirmation table
        for row in rows:

            # Find all table cells (td elements/data) inside the current row
            cols = row.find_elements(By.TAG_NAME, "td")

            # Only process rows that contain exactly two cells
            # (first cell = label, second cell = value)
            if len(cols) == 2:

                # Extract the label text from the first column
                key = cols[0].text.strip()

                # Extract the corresponding value from the second column
                value = cols[1].text.strip()

                # Store the key-value pair in the dictionary
                data[key] = value

        # Verify booking values
        assert data["Status"] == "PendingCapture"
        assert "USD" in data["Amount"]

        # Print JSON-style output for visibility
        print(json.dumps(data, indent=4))

    finally:
        driver.quit()