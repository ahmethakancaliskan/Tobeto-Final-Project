import pytest
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.usefixtures("setup")
class BaseTest:
    driver: WebDriver







