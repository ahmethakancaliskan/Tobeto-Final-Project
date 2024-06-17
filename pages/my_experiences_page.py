from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from constants import constant
from constants.login_page_constants import LoginPageConstants
from pages.base_page import BasePage
from constants.my_experiences_page_constants import MyExperiencesPageLocators
from pages.homepage import HomePage
from pages.login_page import LoginPage
from pages.user_profile_page import UserProfilePage


class MyExperiencesPage(BasePage):
    def precondition(self):
        login_page = LoginPage(self.driver)
        login_page.go_to(constant.LOGIN_PAGE_URL)
        login_page.enter_email(LoginPageConstants.VALID_EMAIL)
        login_page.enter_password(LoginPageConstants.VALID_PASSWORD)
        login_page.click_login_button()
        homepage = HomePage(self.driver)
        homepage.click_create_your_profile_start_button()
        user_profile_page = UserProfilePage(self.driver)
        user_profile_page.click_my_experiences_from_sidebar()

    def enter_company_name(self, name):
        self.wait_until_element_visible(MyExperiencesPageLocators.corporation_name)
        self.find_element(MyExperiencesPageLocators.corporation_name).send_keys(name, Keys.ENTER)

    def enter_position(self, position):
        self.wait_until_element_visible(MyExperiencesPageLocators.position)
        self.find_element(MyExperiencesPageLocators.position).send_keys(position)

    def enter_experience_type(self,type):
        self.wait_until_element_visible(MyExperiencesPageLocators.experience_type)
        self.find_element(MyExperiencesPageLocators.experience_type).click()
        self.find_element(MyExperiencesPageLocators.experience_type).send_keys(type, Keys.ENTER)

    def enter_sector_name(self,sector):
        self.wait_until_element_visible(MyExperiencesPageLocators.sector)
        self.find_element(MyExperiencesPageLocators.sector).send_keys(sector)

    def enter_city(self, city):
        self.wait_until_element_visible(MyExperiencesPageLocators.city)
        dropdown = self.find_element(MyExperiencesPageLocators.city)
        select = Select(dropdown)
        select.select_by_visible_text(city)

    def enter_start_date(self,date):
        self.wait_until_element_visible(MyExperiencesPageLocators.start_date)
        self.find_element(MyExperiencesPageLocators.start_date).send_keys(date, Keys.ENTER)

    def enter_end_date(self, date):
        self.wait_until_element_visible(MyExperiencesPageLocators.end_date)
        self.find_element(MyExperiencesPageLocators.end_date).send_keys(date, Keys.ENTER)
        self.scroll_end_of_the_page()

    def click_checkbox(self):
        self.wait_until_element_visible(MyExperiencesPageLocators.checkbox)
        self.find_element(MyExperiencesPageLocators.checkbox).click()

    def enter_description(self, description):
        self.wait_until_element_visible(MyExperiencesPageLocators.description)
        self.find_element(MyExperiencesPageLocators.description).send_keys(description)
        self.scroll_page_down(150)

    def click_save_button(self):
        self.wait_until_element_visible(MyExperiencesPageLocators.save_button)
        self.find_element(MyExperiencesPageLocators.save_button).click()

    def get_warning_massage(self):
        self.wait_until_element_visible(MyExperiencesPageLocators.warning)
        warning = self.find_element(MyExperiencesPageLocators.warning)

    def get_char_warning(self):
        self.wait_until_element_visible(MyExperiencesPageLocators.char_Warn)
        warning = self.find_element(MyExperiencesPageLocators.char_Warn)
        return warning.text
