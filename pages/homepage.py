import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    __login_button = (By.CSS_SELECTOR, ".text-light")
    __create_your_profile_start_button = (
        By.CSS_SELECTOR, "div[class='details pack-bg-2'] button[class='btn btn-primary w-100 ']")
    __evaluate_yourself_start_button = (
        By.CSS_SELECTOR, "div[class='details pack-bg-3'] button[class='btn btn-primary w-100 ']")
    __start_learning_start_button = (
        By.CSS_SELECTOR, "div[class='details pack-bg-1'] button[class='btn btn-primary w-100 ']")

    def click_login_button(self):
        self.scroll_page_down(250)
        self.wait_until_element_visible(self.__login_button)
        self.find_element(self.__login_button).click()
        time.sleep(1)

    def click_create_your_profile_start_button(self):
        self.wait_implicitly()
        self.scroll_end_of_the_page()
        self.wait_until_element_visible(self.__create_your_profile_start_button)
        self.find_element(self.__create_your_profile_start_button).click()

    def click_evaluate_yourself_start_button(self):
        self.scroll_end_of_the_page()
        self.wait_until_element_visible(self.__evaluate_yourself_start_button)
        self.find_element(self.__evaluate_yourself_start_button).click()

    def click_start_learning_start_button(self):
        self.scroll_end_of_the_page()
        self.wait_until_element_visible(self.__start_learning_start_button)
        self.find_element(self.__start_learning_start_button).click()
