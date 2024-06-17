from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PasswordResetPage(BasePage):
    __mail_input = (By.XPATH, "//input[@type='email']")
    __submit_button = (By.XPATH, "//button[@class='btn btn-primary w-100 mt-6']")
    __warning_massage = (By.CSS_SELECTOR, ".toast-body")

    def enter_email(self, mail):
        self.wait_until_element_visible(self.__mail_input)
        self.find_element(self.__mail_input).send_keys(mail)

    def click_submit_button(self):
        self.wait_until_element_visible(self.__submit_button)
        self.find_element(self.__submit_button).click()

    def get_warning_massage(self):
        self.wait_until_element_visible(self.__warning_massage)
        massage = self.find_element(self.__warning_massage)
        return massage.text
