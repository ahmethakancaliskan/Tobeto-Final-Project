import pytest
from constants import constant, password_reset_page_constants
from constants.login_page_constants import LoginPageConstants
from pages.password_reset_page import PasswordResetPage
from tests.base_test import BaseTest


class TestPasswordResetPage(BaseTest):

    @pytest.mark.smoke
    def test_sending_password_reset_mail(self):
        password_reset_page = PasswordResetPage(self.driver)
        password_reset_page.go_to(constant.PASSWORD_RESET_URL)
        password_reset_page.enter_email(LoginPageConstants.VALID_EMAIL)
        password_reset_page.click_submit_button()
        assert password_reset_page.get_warning_massage() == password_reset_page_constants.VALID_PASSWORD_RESET

    @pytest.mark.smoke
    def test_using_invalid_mail_on_the_password_reset_page(self):
        password_reset_page = PasswordResetPage(self.driver)
        password_reset_page.go_to(constant.PASSWORD_RESET_URL)
        password_reset_page.enter_email("geçersiz@gmail")
        password_reset_page.click_submit_button()
        assert password_reset_page.get_warning_massage() == password_reset_page_constants.EXPECTED_INVALID_MAIL_RESET

    @pytest.mark.smoke
    def test_reset_password_using_unregistered_mail(self):
        password_reset_page = PasswordResetPage(self.driver)
        password_reset_page.go_to(constant.PASSWORD_RESET_URL)
        password_reset_page.enter_email("ğağağğağağğağağğağağağğağağa@gmail.com")
        password_reset_page.click_submit_button()
        assert password_reset_page.get_warning_massage() == password_reset_page_constants.EXPECTED_INVALID_MAIL_RESET
