from page_objects.BasePage import BasePage
from page_objects.PlantTablePage import PlantTablePage
from utils.BaseClass import BaseClass

unsorted_list = []
sorted_list = []
first_page = "https://rahulshettyacademy.com/seleniumPractise/#/offers"


class TestSecond(BaseClass):

    def test_e2e_sort_table(self):
        log = self.get_logger()
        log.info(f"---------------------started test!----------------------")

        base_page = BasePage(self.driver)
        base_page.open_page(first_page)

        selenium_practice_page = PlantTablePage(self.driver)
        selenium_practice_page.select_page_size(2)

        unsorted = selenium_practice_page.get_vegetable_list()
        for item in unsorted:
            unsorted_list.append(item.text)
        log.info(f"unsorted list:`{unsorted_list}`.")

        selenium_practice_page.sort_table_by_name()

        sorted_name = selenium_practice_page.get_vegetable_list()
        for item in sorted_name:
            sorted_list.append(item.text)
        unsorted_list.sort()
        log.info(f"actual sorted list:                   `{sorted_list}`  .")
        log.info(f"initially unsorted list aster sorting:`{unsorted_list}`.")

        assert sorted_list == unsorted_list
        log.info(f"---------------------completed test!----------------------")
