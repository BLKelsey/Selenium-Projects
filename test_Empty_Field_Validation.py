from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_bank_registers():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://parabank.parasoft.com/parabank/register.htm")

    # Fill required fields except SSN
    wait.until(EC.visibility_of_element_located((By.ID, "customer.firstName"))).send_keys("Brian")
    wait.until(EC.visibility_of_element_located((By.ID, "customer.lastName"))).send_keys("Kelsey")
    wait.until(EC.visibility_of_element_located((By.ID, "customer.address.street"))).send_keys("123 Main Street")
    wait.until(EC.visibility_of_element_located((By.ID, "customer.address.city"))).send_keys("Anytown")
    wait.until(EC.visibility_of_element_located((By.ID, "customer.address.state"))).send_keys("FL")
    wait.until(EC.visibility_of_element_located((By.ID, "customer.address.zipCode"))).send_keys("12345")
    wait.until(EC.visibility_of_element_located((By.ID, "customer.phoneNumber"))).send_keys("555-123-4567")
    wait.until(EC.visibility_of_element_located((By.ID, "customer.username"))).send_keys("myusername")
    wait.until(EC.visibility_of_element_located((By.ID, "customer.password"))).send_keys("mypassword")
    wait.until(EC.visibility_of_element_located((By.ID, "repeatedPassword"))).send_keys("mypassword")

    # Click Register BEFORE checking validation
    register_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[type='submit'][value='Register']")
        )
    )
    register_button.click()

    # Now wait for SSN validation error
    ssn_error = wait.until(
        EC.presence_of_element_located((By.ID, "customer.ssn.errors")) )

    expected_message = "Social Security Number is required."
    assert ssn_error.text.strip() == expected_message
    print(f"Expected Error: '{expected_message}'")
    if ssn_error.text.strip() != expected_message:
        print(f"Actual: '{ssn_error.text.strip()}'")


    driver.quit()