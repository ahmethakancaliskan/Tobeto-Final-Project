# Test Senaryosu 1

import pytest
from constants.login_page_constants import LoginPageConstants
from pages.base_page import BasePage
from pages.login_page import LoginPage
from constants import constant
from tests.base_test import BaseTest


class TestLoginPage(BaseTest):
    #Case 1 : Başarılı Giriş Kontrolü
    def test_valid_login(self):  # Başarılı Giriş
        login_page = LoginPage(self.driver)
        base_page = BasePage(self.driver)
        base_page.go_to(constant.LOGIN_PAGE_URL)
        login_page.enter_email(LoginPageConstants.VALID_EMAIL)
        login_page.enter_password(LoginPageConstants.VALID_PASSWORD)
        login_page.click_login_button()
        assert login_page.get_login_warning_massage() == LoginPageConstants.VALID_LOGIN_MASSAGE

    #Case 2 : Şifre Girilmediğinde
    def test_empty_password_login_input(self):  # Şifre alanı boş
        login_page = LoginPage(self.driver)
        base_page = BasePage(self.driver)
        base_page.go_to(constant.LOGIN_PAGE_URL)
        login_page.enter_email("alican@gmail.com")
        login_page.click_login_button()
        assert login_page.get_empty_inputs_error_massage() == LoginPageConstants.ERROR_EMPTY_PASSWORD_OR_MAIL

    #Case 2 : E-posta Girilmediğinde
    def test_empty_mail_login_input(self):  # mail alanı boş
        login_page = LoginPage(self.driver)
        base_page = BasePage(self.driver)
        base_page.go_to(constant.LOGIN_PAGE_URL)
        login_page.enter_password("123456")
        login_page.click_login_button()
        assert login_page.get_empty_inputs_error_massage() == LoginPageConstants.ERROR_EMPTY_PASSWORD_OR_MAIL

    #Case 2 : E-posta ve Şifre Girilmediğinde
    def test_empty_mail_and_password_inputs(self):  # şifre ve mail alanı boş
        login_page = LoginPage(self.driver)
        base_page = BasePage(self.driver)
        base_page.go_to(constant.LOGIN_PAGE_URL)
        login_page.click_login_button()
        assert login_page.get_empty_inputs_error_massage() == LoginPageConstants.ERROR_EMPTY_PASSWORD_OR_MAIL

    #Case 3 : E-posta veya Şifre Hatalı Girildiğinde
    @pytest.mark.parametrize("mail,password", LoginPage.get_data())
    def test_invalid_login(self, mail, password):  # Başarısız giriş
        login_page = LoginPage(self.driver)
        login_page.go_to(constant.LOGIN_PAGE_URL)
        login_page.enter_email(mail)
        login_page.enter_password(password)
        login_page.click_login_button()
        assert login_page.get_login_warning_massage() == LoginPageConstants.ERROR_INVALID_LOGIN_MASSAGE
