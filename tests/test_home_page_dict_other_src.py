import pytest

from page_objects.BasePage import BasePage
from page_objects.HomePage import HomePage
from test_data.home_page_data import HomePageData
from utils.BaseClass import BaseClass

home_page_url = "https://rahulshettyacademy.com/angularpractice/"


class TestHomePage(BaseClass):
    def test_form_submission(self, data_set):
        log = self.get_logger()
        log.info(f"---------------------started test!----------------------")
        BasePage(self.driver).open_page(home_page_url)

        home_page = HomePage(self.driver)
        home_page.set_name(data_set["first_name"] + " " + data_set["last_name"])
        home_page.set_email(data_set["email"])
        home_page.set_password(data_set["password"])
        home_page.check_love_ice_cream()
        home_page.shot_to("py_po_submit_form_1_" + data_set["first_name"])

        self.select_option_by_text(home_page.get_gender_dropdown(), data_set["gender"])

        home_page.submit_form()

        alert_info = home_page.get_success_message()
        home_page.shot_to("py_po_submit_form_2_" + data_set["first_name"])

        assert "Success" in alert_info
        log.info(f"---------------------completed test!----------------------")

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def data_set(self, request):
        return request.param
