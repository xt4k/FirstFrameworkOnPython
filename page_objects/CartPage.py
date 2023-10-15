from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.BasePage import BasePage


class CartPage(BasePage):
    total_amount = (By.CSS_SELECTOR, ".totAmt")
    prices = (By.CSS_SELECTOR, "tr td:nth-child(5) p")

    promo_code = (By.CLASS_NAME, "promoCode")
    promo_button = (By.CLASS_NAME, "promoBtn")
    promo_info = (By.CLASS_NAME, "promoInfo")

    discount_percent = (By.CSS_SELECTOR, ".discountPerc")
    sum_discounted = (By.CSS_SELECTOR, ".discountAmt")



    def get_total_amount(self):
        return self.driver.find_element(*CartPage.total_amount).text

    def get_prices(self):
        return self.driver.find_elements(*CartPage.prices)

    def set_promo_code(self, promo_code):
        self.driver.find_element(*CartPage.promo_code).send_keys(promo_code)

    def apply_promo_code(self):
        self.driver.find_element(*CartPage.promo_button).click()

    def wait_for_info(self):
        wait = (WebDriverWait(self.driver, 10))
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))


    def get_discount_percent(self):
        return self.driver.find_element(*CartPage.discount_percent).text[:-1]

    def get_sum_discounted(self):
        return self.driver.find_element(*CartPage.sum_discounted).text

    def get_promo_info(self):
        return self.driver.find_element(*CartPage.promo_info).text


