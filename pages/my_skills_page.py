import time
from selenium.webdriver import Keys
from constants.my_skills_page_constants import MySkillsPageLocators
from constants import constant
from constants.login_page_constants import LoginPageConstants
from pages.base_page import BasePage
from pages.homepage import HomePage
from pages.login_page import LoginPage
from pages.user_profile_page import UserProfilePage


class MySkillsPage(BasePage):

    def precondition(self):
        login_page = LoginPage(self.driver)
        login_page.go_to(constant.LOGIN_PAGE_URL)
        login_page.enter_email(LoginPageConstants.VALID_EMAIL)
        login_page.enter_password(LoginPageConstants.VALID_PASSWORD)
        login_page.click_login_button()
        homepage = HomePage(self.driver)
        homepage.click_create_your_profile_start_button()
        user_profile_page = UserProfilePage(self.driver)
        user_profile_page.click_my_skills_from_sidebar()

    def add_skill(self, skill):
        self.wait_until_element_visible(MySkillsPageLocators.skills)
        self.find_element(MySkillsPageLocators.skills).click()
        self.wait_until_element_visible(MySkillsPageLocators.skills)
        self.find_element(MySkillsPageLocators.skills).send_keys(skill, Keys.ENTER)
        time.sleep(1)

    def get_warning_massage(self):
        self.wait_until_element_visible(MySkillsPageLocators.warning)
        massage = self.find_element(MySkillsPageLocators.warning)
        return massage.text

    def click_remove_button(self):
        self.wait_until_element_visible(MySkillsPageLocators.remove_button)
        self.find_element(MySkillsPageLocators.remove_button).click()

    def click_remove_confirm(self):
        self.wait_until_element_visible(MySkillsPageLocators.remove_confirm)
        self.find_element(MySkillsPageLocators.remove_confirm).click()

    def click_save_button(self):
        self.wait_until_element_visible(MySkillsPageLocators.save_button)
        self.find_element(MySkillsPageLocators.save_button).click()
