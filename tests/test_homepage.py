#Test Senaryosu 6
import time
import softest
from constants import constant
from constants.login_page_constants import LoginPageConstants
from pages.homepage import HomePage
from pages.login_page import LoginPage
from tests.base_test import BaseTest


class TestHomepage(BaseTest, softest.TestCase):
    # Case 1: Giriş Sayfasının Gösterilmesi
    def test_redirect_platform_page_after_valid_login(self):
        homepage = HomePage(self.driver)
        homepage.go_to(constant.BASE_URL)
        homepage.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.enter_email(LoginPageConstants.VALID_EMAIL)
        login_page.enter_password(LoginPageConstants.VALID_PASSWORD)
        login_page.click_login_button()
        time.sleep(2)  # sayfanın açılması
        assert homepage.get_current_url() == constant.LOGGED_IN_HOMEPAGE_URL

    # Case 4: Kişisel Alan Kontrolü
    def test_personal_field_control(self):
        homepage = HomePage(self.driver)
        homepage.go_to(constant.LOGIN_PAGE_URL)
        login_page = LoginPage(self.driver)
        login_page.enter_email(LoginPageConstants.VALID_EMAIL)
        login_page.enter_password(LoginPageConstants.VALID_PASSWORD)
        login_page.click_login_button()
        self.soft_assert(self.assertEqual, login_page.get_current_url(), constant.LOGGED_IN_HOMEPAGE_URL)
        homepage.click_create_your_profile_start_button()
        self.soft_assert(self.assertEqual, homepage.get_current_url(), constant.PERSONAL_INFORMATIONS_URL)
        homepage.back_previous_page()
        homepage.click_evaluate_yourself_start_button()
        self.soft_assert(self.assertEqual, homepage.get_current_url(), constant.EXAMINATIONS_URL)
        homepage.back_previous_page()
        homepage.click_start_learning_start_button()
        self.soft_assert(self.assertEqual, homepage.click_start_learning_start_button(), constant.CATALOG_URL)
