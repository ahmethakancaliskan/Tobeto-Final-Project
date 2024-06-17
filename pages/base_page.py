from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


# BasePage classı tüm sayfalarda ortak kullanılan reusable selenium methodlarının toplandığı yerdir.
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def go_to(self, URL):
        self.driver.get(URL)

    def wait_until_element_visible(self, locator):
        WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(locator))

    def get_text(self, webelement):
        return self.driver.find_element(webelement).text

    def scroll_page_down(self, number):
        self.driver.execute_script(f"window.scrollTo(0, {number});")

    def scroll_end_of_the_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def save_screenshot(self,filename):
        self.driver.save_screenshot(filename)

    def back_previous_page(self):
        self.driver.back()

    def wait_implicitly(self):
        self.driver.implicitly_wait(10)


