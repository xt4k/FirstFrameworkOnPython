from page_objects.HomePage import HomePage
from utils.BaseClass import BaseClass

expected_product_name = "Blackberry"
initial_url = "https://rahulshettyacademy.com/angularpractice/shop"


class TestOne(BaseClass):

    def test_e2e_select(self):
        log = self.get_logger()
        log.info(f"---------------------started test!----------------------")

        home_page = HomePage(self.driver)
        home_page.open_page(initial_url)

        shop_page = home_page.shop_button()
        shop_page.shot_to("python-e2e-select-1")

        shop_item_list = shop_page.get_items()
        shop_page.shot_to("python-e2e-2")
        log.info(f"shop_item_list:`{shop_item_list}`.")

        for element in shop_item_list:
            actual_element_text = shop_page.get_item_name(element)
            image_url = shop_page.get_image_path(element)
            log.info(f"element text:`{actual_element_text}`, image_url:`{image_url}`.")

            if actual_element_text == expected_product_name:
                log.info(f"actual_element_text:`{actual_element_text}`, expected_product_name:`{expected_product_name}`.")
                assert expected_product_name.lower() in image_url.lower()

        shop_page.shot_to("python-e2e-3")
        log.info(f"---------------------completed test!----------------------")
