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
        home_page.set_name(data_provider[0] + " " + data_provider[1])
        home_page.set_email(data_provider[2])
        home_page.set_password(data_provider[3])
        home_page.check_love_ice_cream()
        home_page.shot_to("py_po_submit_form_1_" + data_provider[0])

        self.select_option_by_text(home_page.get_gender_dropdown(), data_provider[4])

        home_page.submit_form()

        alert_info = home_page.get_success_message()
        home_page.shot_to("py_po_submit_form_2_" + data_provider[0])

        assert "Success" in alert_info
        log.info(f"---------------------completed test!----------------------")

    @pytest.fixture(params=[("first_name1", "last_name1", "e@mai.l1", "Password_1", "Male"),
                            ("first_name2", "last_name2", "e@mai.l2", "Password_2", "Female")])
    def data_provider(self, request):
        return request.param
