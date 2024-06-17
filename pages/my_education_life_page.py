import time
from selenium.webdriver import Keys
from constants import constant
from constants.login_page_constants import LoginPageConstants
from pages.base_page import BasePage
from constants.my_education_life_constants import MyEducationLifeLocators
from pages.homepage import HomePage
from pages.login_page import LoginPage
from pages.user_profile_page import UserProfilePage


class MyEducationLifePage(BasePage):

    def precondition(self):
        login_page = LoginPage(self.driver)
        login_page.go_to(constant.LOGIN_PAGE_URL)
        login_page.enter_email(LoginPageConstants.VALID_EMAIL)
        login_page.enter_password(LoginPageConstants.VALID_PASSWORD)
        login_page.click_login_button()
        homepage = HomePage(self.driver)
        homepage.click_create_your_profile_start_button()
        user_profile_page = UserProfilePage(self.driver)
        user_profile_page.click_my_education_from_sidebar()
        self.scroll_end_of_the_page()

    def choose_education_degree(self):
        self.wait_until_element_visible(MyEducationLifeLocators.education_status)
        self.find_element(MyEducationLifeLocators.education_status).send_keys("Lisans", Keys.DOWN, Keys.ENTER)

    def enter_university_name(self, university_name):
        self.wait_until_element_visible(MyEducationLifeLocators.university)
        self.find_element(MyEducationLifeLocators.university).send_keys(university_name)

    def enter_department(self, department_name):
        self.wait_until_element_visible(MyEducationLifeLocators.department)
        self.find_element(MyEducationLifeLocators.department).send_keys(department_name)

    def enter_start_date(self, start_date):
        self.wait_until_element_visible(MyEducationLifeLocators.start_Date)
        self.find_element(MyEducationLifeLocators.start_Date).send_keys(start_date, Keys.ENTER)

    def enter_end_date(self, end_date):
        self.wait_until_element_visible(MyEducationLifeLocators.end_Date)
        self.find_element(MyEducationLifeLocators.end_Date).send_keys(end_date, Keys.ENTER)

    def click_save_button(self):
        self.wait_until_element_visible(MyEducationLifeLocators.save_button)
        self.find_element(MyEducationLifeLocators.save_button).click()

    def get_add_warning(self):
        self.wait_until_element_visible(MyEducationLifeLocators.warnings)
        warning = self.find_element(MyEducationLifeLocators.warnings)
        self.save_screenshot("../Screenshots/my_education_life_page/AddedEducation.png")
        return warning.text

    def get_remove_warning(self):
        self.wait_until_element_visible(MyEducationLifeLocators.warnings)
        warning = self.find_element(MyEducationLifeLocators.warnings)
        self.save_screenshot("../Screenshots/my_education_life_page/DeletedEducation.png")
        return warning.text

    # Eğitim Silme

    def click_delete_button(self):
        self.wait_until_element_visible(MyEducationLifeLocators.remove_added_education)
        self.find_element(MyEducationLifeLocators.remove_added_education).click()

    def click_confirm_delete_button(self):
        self.wait_until_element_visible(MyEducationLifeLocators.remove_yes)
        self.find_element(MyEducationLifeLocators.remove_yes).click()
        time.sleep(1)
