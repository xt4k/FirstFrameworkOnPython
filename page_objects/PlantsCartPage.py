from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from page_objects.CartPopupPage import CartPopupPage


class PlantsCartPage(BasePage):
    search_text = (By.CLASS_NAME, "search-keyword")
    plants_list = (By.XPATH, "//div[@class='products']/div")
    product_names = (By.CSS_SELECTOR, "div h4.product-name")
    plant_icon = (By.XPATH, "div/button")
    cart = (By.CSS_SELECTOR, "a.cart-icon")

    def text_search(self, text):
        return self.driver.find_element(*PlantsCartPage.search_text).send_keys(text)

    def get_plants(self):
        return self.driver.find_elements(*PlantsCartPage.plants_list)

    def get_product_names(self):
        return self.driver.find_elements(*PlantsCartPage.product_names)

    def add_to_cart(self, element):
        return element.find_element(*PlantsCartPage.plant_icon).click()

    def go_cart(self):
        self.driver.find_element(*PlantsCartPage.cart).click()
        return CartPopupPage(self.driver)

