from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class ShopPage(BasePage):
    shop_items = (By.XPATH, "//app-card/div")

    def get_items(self):
        return self.driver.find_elements(*ShopPage.shop_items)


