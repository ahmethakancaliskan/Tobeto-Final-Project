from selenium.webdriver import Keys

from constants import constant
from constants.login_page_constants import LoginPageConstants
from pages.base_page import BasePage
from constants.my_languages_page_constants import MyLanguagesPageLocators
from pages.homepage import HomePage
from pages.login_page import LoginPage
from pages.user_profile_page import UserProfilePage


class MyLanguagesPage(BasePage):
    def precondition(self):
        login_page = LoginPage(self.driver)
        login_page.go_to(constant.LOGIN_PAGE_URL)
        login_page.enter_email(LoginPageConstants.VALID_EMAIL)
        login_page.enter_password(LoginPageConstants.VALID_PASSWORD)
        login_page.click_login_button()
        homepage = HomePage(self.driver)
        homepage.click_create_your_profile_start_button()
        user_profile_page = UserProfilePage(self.driver)
        user_profile_page.click_my_languages_from_sidebar()

    def add_language(self, language):
        self.wait_until_element_visible(MyLanguagesPageLocators.languages)
        self.find_element(MyLanguagesPageLocators.languages).send_keys(language, Keys.ENTER)

    def enter_language_level(self, level):
        self.wait_until_element_visible(MyLanguagesPageLocators.level)
        self.find_element(MyLanguagesPageLocators.level).send_keys(level, Keys.ENTER)

    def click_save_button(self):
        self.wait_until_element_visible(MyLanguagesPageLocators.save_button)
        self.find_element(MyLanguagesPageLocators.save_button).click()

    def get_warning_massage(self):
        self.wait_until_element_visible(MyLanguagesPageLocators.warning)
        massage = self.find_element(MyLanguagesPageLocators.warning)
        return massage.text
