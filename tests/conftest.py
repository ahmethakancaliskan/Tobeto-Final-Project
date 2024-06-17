from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def setup(request, browser="edge"):
    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        print("PLEASE ENTER A VALID BROWSER")

    driver.maximize_window()
    driver.implicitly_wait(20)
    request.cls.driver = driver
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

#BaseTest Sınıfında driver Özelliğini Tanımlamak:
#BaseTest sınıfında driver özelliğini tanımlayarak, PyCharm'ın bu özelliği anlamasını sağlayabilirsiniz.'''
