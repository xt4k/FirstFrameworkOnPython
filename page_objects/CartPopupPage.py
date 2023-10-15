from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from page_objects.CartPage import CartPage


class CartPopupPage(BasePage):
    proceed_checkout = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    def proceed_to_checkout(self):
        self.driver.find_element(*CartPopupPage.proceed_checkout).click()
        return CartPage(self.driver)

