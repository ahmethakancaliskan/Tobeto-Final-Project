from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import keyboard
from constants import constant
from pages.base_page import BasePage
from pages.homepage import HomePage
from pages.login_page import LoginPage
from constants.login_page_constants import LoginPageConstants
from pages.user_profile_page import UserProfilePage


class MyCertificatesPage(BasePage):
    certificate_name = (By.NAME, "CertificateName")
    certificate_date = (By.CSS_SELECTOR, "input[placeholder='Seçiniz']")
    upload_certificate = (By.CSS_SELECTOR, ".uppy-u-reset")
    save_button = (By.CSS_SELECTOR, ".btn-primary")

    def precondition(self):
        login_page = LoginPage(self.driver)
        login_page.go_to(constant.LOGIN_PAGE_URL)
        login_page.enter_email(LoginPageConstants.VALID_EMAIL)
        login_page.enter_password(LoginPageConstants.VALID_PASSWORD)
        login_page.click_login_button()
        homepage = HomePage(self.driver)
        homepage.click_create_your_profile_start_button()
        user_profile_page = UserProfilePage(self.driver)
        user_profile_page.click_my_certificates()

    def enter_certificate_name(self, name):
        self.wait_until_element_visible(self.certificate_name)
        self.find_element(self.certificate_name).send_keys(name)

    def enter_certificate_date(self, date):
        self.wait_until_element_visible(self.certificate_date)
        self.find_element(self.certificate_date).send_keys(date, Keys.ENTER)

    def click_upload_certificate(self):
        self.wait_until_element_visible(self.upload_certificate)
        self.find_element(self.upload_certificate).click()
        keyboard.write("github.jpg")
        keyboard.send("enter")

    def click_save_button(self):
        self.wait_until_element_visible(self.save_button)
        self.find_element(self.save_button).click()
