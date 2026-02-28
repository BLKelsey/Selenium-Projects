from pages.home_page import HomePage
from pages.product_page import ProductPage

def test_add_samsung_s6_to_cart(driver):

    home = HomePage(driver)
    product = ProductPage(driver)

    home.open()
    home.select_samsung_s6()

    assert product.get_product_title() == "Samsung galaxy s6"

    product.add_to_cart()

    alert_text = product.accept_alert()

    assert alert_text == "Product added"