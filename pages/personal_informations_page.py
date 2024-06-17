import time
import keyboard
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from constants import constant
from constants.login_page_constants import LoginPageConstants
from pages.base_page import BasePage
from constants.personal_information_page_constants import PersonalInformationPageLocators, PersonalInformationPageConstants
from pages.homepage import HomePage
from pages.login_page import LoginPage


class PersonalInformationPage(BasePage):

    def precondition(self):
        personal_informations_page = PersonalInformationPage(self.driver)
        login_page = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        personal_informations_page.go_to(constant.LOGIN_PAGE_URL)
        login_page.enter_email(LoginPageConstants.VALID_EMAIL)
        login_page.enter_password(LoginPageConstants.VALID_PASSWORD)
        login_page.click_login_button()
        homepage.click_create_your_profile_start_button()

    def enter_name(self, name):
        self.wait_until_element_visible(PersonalInformationPageLocators.name)
        self.find_element(PersonalInformationPageLocators.name).clear()
        self.find_element(PersonalInformationPageLocators.name).send_keys(name)

    def enter_surname(self, surname):
        self.wait_until_element_visible(PersonalInformationPageLocators.surname)
        self.find_element(PersonalInformationPageLocators.surname).clear()
        self.find_element(PersonalInformationPageLocators.surname).send_keys(surname)

    def enter_gender(self, gender):
        self.wait_until_element_visible(PersonalInformationPageLocators.gender)
        self.find_element(PersonalInformationPageLocators.gender).click()
        self.find_element(PersonalInformationPageLocators.gender).send_keys(gender, Keys.ENTER)

    def enter_military_status(self, status):
        self.wait_until_element_visible(PersonalInformationPageLocators.military_status)
        self.find_element(PersonalInformationPageLocators.military_status).click()
        self.find_element(PersonalInformationPageLocators.military_status).send_keys(status, Keys.ENTER)

    def enter_disability_status(self, status):
        self.wait_until_element_visible(PersonalInformationPageLocators.disability)
        self.find_element(PersonalInformationPageLocators.disability).click()
        self.find_element(PersonalInformationPageLocators.disability).send_keys(status, Keys.ENTER)

    def enter_phone(self, phone):
        self.wait_until_element_visible(PersonalInformationPageLocators.phone)
        self.find_element(PersonalInformationPageLocators.phone).clear()
        self.find_element(PersonalInformationPageLocators.phone).send_keys(phone)

    def enter_birthdate(self, birthdate):
        self.wait_until_element_visible(PersonalInformationPageLocators.birth_date)
        self.find_element(PersonalInformationPageLocators.birth_date).send_keys(birthdate)

    def enter_national_identity(self, identity):
        self.wait_until_element_visible(PersonalInformationPageLocators.national_identity)
        self.find_element(PersonalInformationPageLocators.national_identity).send_keys(identity)
        self.scroll_page_down(250)

    def enter_github_address(self, github):
        self.wait_until_element_visible(PersonalInformationPageLocators.github_adress)
        self.find_element(PersonalInformationPageLocators.github_adress).clear()
        self.find_element(PersonalInformationPageLocators.github_adress).send_keys(github)

    def enter_country(self, country):
        self.wait_until_element_visible(PersonalInformationPageLocators.country)
        self.find_element(PersonalInformationPageLocators.country).send_keys(country)

    def enter_city(self, city):
        self.wait_until_element_visible(PersonalInformationPageLocators.city)
        dropdown = self.find_element(PersonalInformationPageLocators.city)
        select = Select(dropdown)
        select.select_by_visible_text(city)
        self.scroll_end_of_the_page()

    def enter_district(self, district):
        self.wait_until_element_visible(PersonalInformationPageLocators.district)
        dropdown = self.find_element(PersonalInformationPageLocators.district)
        select = Select(dropdown)
        select.select_by_visible_text(district)

    def enter_address(self, address):
        self.wait_until_element_visible(PersonalInformationPageLocators.address)
        self.find_element(PersonalInformationPageLocators.address).send_keys(address)

    def enter_about(self,text):
        self.wait_until_element_visible(PersonalInformationPageLocators.about_me)
        self.find_element(PersonalInformationPageLocators.about_me).send_keys(text)

    def click_save_button(self):
        self.wait_until_element_visible(PersonalInformationPageLocators.save_button)
        self.find_element(PersonalInformationPageLocators.save_button).click()

    def get_warning_massage(self):
        self.wait_until_element_visible(PersonalInformationPageLocators.warning)
        massage = self.find_element(PersonalInformationPageLocators.warning)
        return massage.text

    def upload_profile_picture(self):
        self.wait_until_element_visible(PersonalInformationPageLocators.upload_picture_button)
        self.find_element(PersonalInformationPageLocators.upload_picture_button).click()
        self.wait_until_element_visible(PersonalInformationPageLocators.upload_picture)
        photo = self.find_element(PersonalInformationPageLocators.upload_picture)
        photo.send_keys("../data/mauroIcardi.jpg")
        self.save_screenshot("../Screenshots/personal_information_page/UploadedProfilePicture.png")
