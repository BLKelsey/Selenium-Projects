from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_fill_in_text_boxes():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://demoqa.com/text-box")  

    # -------------------------------------------------
    # Enter text into Full Name field
    # -------------------------------------------------
    full_name_field = wait.until(
        EC.visibility_of_element_located((By.ID, "userName"))
    )
    full_name_field.send_keys("Brian Kelsey")
    print("Entered Full Name.")    

    # -------------------------------------------------
    # Enter text into Email field
    # -------------------------------------------------
    email_field = wait.until(
        EC.visibility_of_element_located((By.ID, "userEmail"))
    )
    email_field.send_keys("blkelsey@gmail.com")
    print("Entered Email.")

    # -------------------------------------------------
    # Enter text into Current Address field
    # -------------------------------------------------
    current_address_field = wait.until(
        EC.visibility_of_element_located((By.ID, "currentAddress"))
    )
    current_address_field.send_keys("123 Main Street")
    print("Entered Current Address.")

    # -------------------------------------------------
    # Enter text into Permanent Address field
    # -------------------------------------------------
    permanent_address_field = wait.until(
        EC.visibility_of_element_located((By.ID, "permanentAddress"))
    )
    permanent_address_field.send_keys("123 Oak Avenue")
    print("Entered Permanent Address.")

    # -------------------------------------------------
    # Click Submit button
    # -------------------------------------------------
    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()
    print("Clicked Submit button.")

    driver.quit()
