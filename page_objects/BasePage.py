from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def shot_to(self, file_path):
        full_path = "shots/" + file_path+".png"
        print(f"shot will be saved to {full_path}")
        self.driver.save_screenshot(full_path)

    def get_item_name(self, element):
        return element.find_element(By.TAG_NAME, 'h4').text

    def get_image_path(self, element):
        return element.find_element(By.TAG_NAME, "img").get_attribute("src")

    def open_page(self, url):
        self.driver.get(url)
        return BasePage(self.driver)


    def wait_refresh(self, url):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(url))
