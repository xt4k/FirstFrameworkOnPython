from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage
from page_objects.ShopPage import ShopPage


class HomePage(BasePage):
    shop = (By.CSS_SELECTOR, "a[href='/angularpractice/shop']")
    name = (By.NAME,"name")
    email = (By.NAME,"email")
    password = (By.ID,"exampleInputPassword1")
    ice_cream_checkbox = (By.ID, "exampleInputPassword1")
    date_of_birth = (By.NAME,"bday")
    gender_dropdown = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH,'//input[@value="Submit"]')
    success = (By.XPATH,'//div[contains(@class,"alert")]')


    def shop_button(self):
        self.driver.find_element(*HomePage.shop).click()
        return ShopPage(self.driver)

    def set_name(self, text):
        self.driver.find_element(*HomePage.name).send_keys(text)
        return HomePage(self.driver)

    def set_email(self, text):
        self.driver.find_element(*HomePage.email).send_keys(text)
        return HomePage(self.driver)

    def set_password(self, text):
        self.driver.find_element(*HomePage.password).send_keys(text)
        return HomePage(self.driver)

    def check_love_ice_cream(self):
        self.driver.find_element(*HomePage.ice_cream_checkbox).click()
        return HomePage(self.driver)

    def submit_form(self):
        self.driver.find_element(*HomePage.submit).click()
        return HomePage(self.driver)

    def get_success_message(self):
       return self.driver.find_element(*HomePage.success).text

    def get_gender_dropdown(self):
       return self.driver.find_element(*HomePage.gender_dropdown)
