import pytest
import inspect
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verify_link_presence(self, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def verify_element_presence(self, web_element):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(web_element))

    def select_option_by_text(self, web_element, text):
        sel = Select(web_element)
        sel.select_by_visible_text(text)

    def get_logger(self):
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        file_handler = logging.FileHandler("taf.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger
