import pytest

from page_objects.BasePage import BasePage
from page_objects.HomePage import HomePage
from utils.BaseClass import BaseClass

home_page_url = "https://rahulshettyacademy.com/angularpractice/"


class TestHomePage(BaseClass):
    def test_form_submission(self, data_provider):
        log = self.get_logger()
        log.info(f"---------------------started test!----------------------")

        BasePage(self.driver).open_page(home_page_url)
        home_page = HomePage(self.driver)
        home_page.set_name(data_provider["first_name"] + " " + data_provider["last_name"])
        home_page.set_email(data_provider["email"])
        home_page.set_password(data_provider["password"])
        home_page.check_love_ice_cream()
        home_page.shot_to("py_po_submit_form_1_" + data_provider["first_name"])

        self.select_option_by_text(home_page.get_gender_dropdown(), data_provider["gender"])

        home_page.submit_form()

        alert_info = home_page.get_success_message()
        home_page.shot_to("py_po_submit_form_2_" + data_provider["first_name"])

        assert "Success" in alert_info
        log.info(f"---------------------completed test!----------------------")

    @pytest.fixture(params=[{"first_name": "first_1", "last_name": "last_1", "email": "e@mai.l1", "password": "Password_1", "gender": "Male"},
                            {"first_name": "first_2", "last_name": "last_2", "email": "e@mai.l2","password": "Password_2", "gender": "Female"}])
    def data_provider(self, request):
        return request.param
