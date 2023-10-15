from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class PlantTablePage(BasePage):
    page_menu = (By.ID, "page-menu")
    elements = (By.XPATH, "//tr/td[1]")
    sort_by_name = (By.XPATH, "//span[text()='Veg/fruit name']")

    def select_page_size(self, size):
        self.driver.find_element(*PlantTablePage.page_menu).click()
        self.driver.find_element(*PlantTablePage.page_menu).send_keys(size)
        self.driver.find_element(*PlantTablePage.page_menu).click()
        return self

    def get_vegetable_list(self):
        return self.driver.find_elements(*PlantTablePage.elements)

    def sort_table_by_name(self):
        self.driver.find_element(*PlantTablePage.sort_by_name).click()
