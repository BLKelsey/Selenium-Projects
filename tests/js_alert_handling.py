from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_js_confirm_alert():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://testpages.herokuapp.com/pages/basics/alerts-javascript/")
    print("Page loaded")

    # Locate confirm button
    confirm_button = wait.until(
        EC.presence_of_element_located((By.ID, "confirmexample"))
    )

    driver.execute_script(
        "arguments[0].scrollIntoView(true);",
        confirm_button
    )

    confirm_button.click()
    print("Clicked Show confirm box")

    wait.until(EC.alert_is_present())
    print("Confirm alert is present")

    alert = driver.switch_to.alert

    assert alert.text == "I am a confirm alert", "Unexpected alert text"

    alert.accept()
    print("Confirm alert accepted")

    driver.quit()