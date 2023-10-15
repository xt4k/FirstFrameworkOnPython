import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

default_home_page ="https://rahulshettyacademy.com/angularpractice/shop"

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="define: chrome or firefox"
    )

    parser.addoption(
        "--home_page", action="store", default=default_home_page, help="set home_page"
    )

# @pytest.fixture
# def get_browser(request):
#     return request.config.getoption("--browser_name")


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    home_page = request.config.getoption("--home_page")


    print(f"----- selected browser:`{browser_name}` --------.")
    print(f"----- home_page:`{home_page}` --------.")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        # options.add_argument("headless")
        options.add_argument("--ignore-certificate-errors")
        service_obj = Service()
        # driver = webdriver.Chrome(service=service_obj, options=options)
        driver = webdriver.Chrome(service=service_obj)

    elif browser_name == "firefox":
        # service_obj = Service()
        # driver = webdriver.Firefox(service=service_obj)

        options = webdriver.FirefoxOptions()
        # options.add_argument("-headless")

        service_obj = webdriver.FirefoxService(log_output='gecko.log', service_args=['--log', 'debug'])
        driver = webdriver.Firefox(service=service_obj, options=options)
    else:
        AssertionError("browser is undefined")

    driver.implicitly_wait(2)
    driver.maximize_window()
    # driver.get(home_page)

    request.cls.driver = driver

    yield
    driver.close()
