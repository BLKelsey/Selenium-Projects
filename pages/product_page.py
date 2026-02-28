from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):

    PRODUCT_TITLE = (By.CLASS_NAME, "name")
    ADD_TO_CART_BTN = (By.LINK_TEXT, "Add to cart")

    def get_product_title(self):
        return self.get_text(self.PRODUCT_TITLE)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)
        
    def accept_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        return alert_text