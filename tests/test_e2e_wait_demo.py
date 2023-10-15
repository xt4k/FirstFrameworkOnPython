import time

from page_objects.BasePage import BasePage
from page_objects.PlantsCartPage import PlantsCartPage
from utils.BaseClass import BaseClass

start_page = "https://rahulshettyacademy.com/seleniumPractise/#/"
promo_code_valid = "rahulshettyacademy"
search_pattern = "ber"
expected_list = ["Cucumber", "Raspberry", "Strawberry"]


class TestThird(BaseClass):
    def test_e2e_third(self):
        log = self.get_logger()
        log.info(f"---------------------started test!----------------------")

        BasePage(self.driver).open_page(start_page)

        plants_cart_page = PlantsCartPage(self.driver)
        plants_cart_page.shot_to("e2e_po_3_1")

        plants_cart_page.text_search(search_pattern)
        time.sleep(2)
        results = plants_cart_page.get_plants()

        exercise_list = plants_cart_page.get_product_names()
        for text_element in exercise_list:
            log.info(f"here is product name{text_element.text}")
            assert search_pattern in text_element.text
            check = any(item in text_element.text for item in expected_list)
            log.info(check)
            assert check

        for found_item in results:
            log.info(f"found element with text:`{found_item.text}`.")
            plants_cart_page.add_to_cart(found_item)

        cart_popup = plants_cart_page.go_cart()
        cart_popup.shot_to("e2e_po_3_4")

        cart_page = cart_popup.proceed_to_checkout()
        time.sleep(2)

        cart_page.shot_to("e2e_po_3_5")
        page_sum = int(cart_page.get_total_amount())
        prices = cart_page.get_prices()
        price_from_cell = 0
        for price in prices:
            price_from_cell = price_from_cell + int(price.text)

        log.info(f"From table cell:`{price_from_cell}`")
        log.info(f"From Summary cell :`{page_sum}`")

        assert price_from_cell == page_sum

        cart_page.set_promo_code(promo_code_valid)
        cart_page.shot_to("e2e_po_3_7")
        cart_page.apply_promo_code()
        cart_page.shot_to("e2e_po_3_8")
        self.verify_element_presence(cart_page.promo_info)
        cart_page.shot_to("e2e_po_3_9")

        discount_percent = int(cart_page.get_discount_percent())
        page_sum_discounted = float(cart_page.get_sum_discounted())

        log.info(f"float price with discount `{page_sum_discounted}`")
        log.info(f"Total amount:`{page_sum}`")
        log.info(f"Total amount:`{discount_percent}`")
        log.info(f"Total amount with discount:`{page_sum_discounted}`")

        result_sum = page_sum * (1 - discount_percent / 100)
        log.info(f"process summary:`{result_sum}`")

        assert page_sum_discounted < page_sum
        assert page_sum_discounted == page_sum_discounted

        log.info(f"last test step text: `{cart_page.get_promo_info()}`.")
        log.info(f"---------------------completed test!----------------------")
