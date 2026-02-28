from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    SAMSUNG_S6_LINK = (By.LINK_TEXT, "Samsung galaxy s6")

    def open(self):
        self.driver.get("https://www.demoblaze.com/")

    def select_samsung_s6(self):
        self.click(self.SAMSUNG_S6_LINK)