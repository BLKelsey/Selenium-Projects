import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    
@pytest.fixture(scope="session")
def base_url():
   return "https://fakestoreapi.com/"
 
@pytest.fixture(scope="session")
def endpoint(base_url):
    return f"{base_url}/auth/login"
  
@pytest.fixture(scope="session")
def credentials():
    return {
        "username": "mor_2314",
        "password": "83r5^_"
    }