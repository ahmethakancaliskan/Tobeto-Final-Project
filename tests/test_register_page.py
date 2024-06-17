# Test Senaryosu 2

import time

import pytest
from selenium.webdriver import Keys
from constants.register_page_constants import RegisterPageConstants
from pages.register_page import RegisterPage
from constants import constant
from tests.base_test import BaseTest


class TestRegisterPage(BaseTest):

    # Case 1 : Başarılı Kayıt Ol Kontrolü
    def test_valid_registration(self):  # Başarılı Kayıt Olma Testi
        register_page = RegisterPage(self.driver)
        register_page.go_to(constant.LOGIN_PAGE_URL)
        register_page.click_sign_up()
        register_page.enter_name("Deneme")
        register_page.enter_last_name("Test3A")
        register_page.enter_mail("galatasaray@gmail.com")
        register_page.enter_password("12345")
        register_page.enter_password_again("12345")
        register_page.click_sign_up_button()
        assert register_page.get_alert_massage() == RegisterPageConstants.ALERT_POPUP_TITLE_TEXT  # Kayıt oluşturmak için gerekli sözleşmeler alert sayfasının açıldığını doğruluyor
        register_page.click_acik_riza_metni()
        register_page.click_membership_contrat()
        register_page.click_email_confirmation()
        register_page.click_phone_confirmation()
        register_page.click_phone_number_button("5308522975")
        time.sleep(5)  # reCaptcha doğrulamasını manuel olarak atlamak için
        register_page.click_continue_button()

    # Case 2: Kayıt Ol Sırasında İstenen Telefon Numarası Karakter Kontrolü
    def test_phone_number_must_be_10_character(self):  # telefon alanına girilen <10 karakter kontrolü
        register_page = RegisterPage(self.driver)
        register_page.go_to(constant.LOGIN_PAGE_URL)
        register_page.click_sign_up()
        register_page.enter_name("Deneme")
        register_page.enter_last_name("Test3A")
        register_page.enter_mail("galatasaray@gmail.com")
        register_page.enter_password("Gs12345")
        register_page.enter_password_again("Gs12345")
        register_page.click_sign_up_button()
        assert register_page.get_alert_massage() == RegisterPageConstants.ALERT_POPUP_TITLE_TEXT  # Kayıt oluşturmak için gerekli sözleşmeler alert sayfasının açıldığını doğruluyor
        register_page.click_acik_riza_metni()
        register_page.click_membership_contrat()
        register_page.click_email_confirmation()
        register_page.click_phone_confirmation()
        register_page.click_phone_number_button("530852297")  # 9 karakter girilir
        time.sleep(5)  # reCaptcha doğrulamasını manuel olarak atlamak için
        register_page.click_continue_button()
        assert register_page.get_phone_number_character_warning() == RegisterPageConstants.WARNING_AT_LEAST_10_CHARACTER

    # Case 3 : Geçersiz E-posta Kontrolü
    def test_invalid_email(self):  # Geçersiz email kontrolü
        register_page = RegisterPage(self.driver)
        register_page.go_to(constant.LOGIN_PAGE_URL)
        register_page.click_sign_up()
        register_page.enter_name("Deneme")
        register_page.enter_last_name("Test3A")
        register_page.enter_mail("e")
        assert register_page.get_invalid_email() == RegisterPageConstants.WARNING_INVALID_EMAIL
        register_page.enter_mail(Keys.BACKSPACE)
        assert register_page.get_email_input_must_fill() == RegisterPageConstants.WARNING_EMPTY_EMAIL_INPUT_MUST_FILL

    #Case 4 : Girdiğiniz E Posta Adresi İle Kayıtlı Üyelik Bulunmaktadır Uyarısının Alınması
    def test_email_already_exist(self):  # kayıtlı email ile yeniden kayıt olamama
        register_page = RegisterPage(self.driver)
        register_page.go_to(constant.LOGIN_PAGE_URL)
        register_page.click_sign_up()
        register_page.enter_name("Deneme")
        register_page.enter_last_name("Test3A")
        register_page.enter_mail("caliskanahmethakan@gmail.com")
        register_page.enter_password("Gs12345")
        register_page.enter_password_again("Gs12345")
        register_page.click_sign_up_button()
        assert register_page.get_alert_massage() == RegisterPageConstants.ALERT_POPUP_TITLE_TEXT  # Kayıt oluşturmak için gerekli sözleşmeler alert sayfasının açıldığını doğruluyor
        register_page.click_acik_riza_metni()
        register_page.click_membership_contrat()
        register_page.click_email_confirmation()
        register_page.click_phone_confirmation()
        register_page.click_phone_number_button("5308522975")
        time.sleep(5)  # reCaptcha doğrulamasını manuel olarak atlamak için
        register_page.click_continue_button()
        assert register_page.get_right_corner_warning_massage() == RegisterPageConstants.WARNING_MAIL_ALREADY_EXIST

    #Case 5: Şifrenin Karakter Sayı Kontrolü
    def test_password_character_must_be_at_least_6_character(self):  #şifre alanına girilen karakter sayısı kontrolü
        register_page = RegisterPage(self.driver)
        register_page.go_to(constant.LOGIN_PAGE_URL)
        register_page.click_sign_up()
        register_page.enter_name("Deneme")
        register_page.enter_last_name("Test3A")
        register_page.enter_mail("galatasaray@gmail.com")
        register_page.enter_password("Gs123")
        register_page.enter_password_again("Gs123")
        register_page.click_sign_up_button()
        assert register_page.get_alert_massage() == RegisterPageConstants.ALERT_POPUP_TITLE_TEXT  # Kayıt oluşturmak için gerekli sözleşmeler alert sayfasının açıldığını doğruluyor
        register_page.click_acik_riza_metni()
        register_page.click_membership_contrat()
        register_page.click_email_confirmation()
        register_page.click_phone_confirmation()
        register_page.click_phone_number_button("5308522975")
        time.sleep(5)  # reCaptcha doğrulamasını manuel olarak atlamak için
        register_page.click_continue_button()
        assert register_page.get_right_corner_warning_massage() == RegisterPageConstants.WARNING_PASSWORD_CHARACTER_QUANTITY

    #Case 6: Şifre Tekrarı Kontrolü
    def test_password_again_must_be_same_as_password(self):  # şifre tekrarı kontrolü
        register_page = RegisterPage(self.driver)
        register_page.go_to(constant.LOGIN_PAGE_URL)
        register_page.click_sign_up()
        register_page.enter_name("Deneme")
        register_page.enter_last_name("Test3A")
        register_page.enter_mail("galatasaray@gmail.com")
        register_page.enter_password("Gs123456")
        register_page.enter_password_again("Gs123598")
        register_page.click_sign_up_button()
        assert register_page.get_alert_massage() == RegisterPageConstants.ALERT_POPUP_TITLE_TEXT  # Kayıt oluşturmak için gerekli sözleşmeler alert sayfasının açıldığını doğruluyor
        register_page.click_acik_riza_metni()
        register_page.click_membership_contrat()
        register_page.click_email_confirmation()
        register_page.click_phone_confirmation()
        register_page.click_phone_number_button("5308522975")
        time.sleep(5)  # reCaptcha doğrulamasını manuel olarak atlamak için
        register_page.click_continue_button()
        assert register_page.get_right_corner_warning_massage() == RegisterPageConstants.WARNING_PASSWORDS_DO_NOT_MATCH

    #Case 7: Girilen Bilgilerde 2 Farklı Hatalı Kısım Olduğunda
    def test_two_wrong_information(self):  # 2 farklı hatalı kısım olduğunda @fail
        register_page = RegisterPage(self.driver)
        register_page.go_to(constant.LOGIN_PAGE_URL)
        register_page.click_sign_up()
        register_page.enter_name("Deneme")
        register_page.enter_last_name("Test3A")
        register_page.enter_mail("geçersiz@gmail.com")  # geçersiz mail
        register_page.enter_password("asdas")  # geçersiz sifreler
        register_page.enter_password_again("asdas")
        register_page.click_sign_up_button()
        assert register_page.get_alert_massage() == RegisterPageConstants.ALERT_POPUP_TITLE_TEXT  # Kayıt oluşturmak için gerekli sözleşmeler alert sayfasının açıldığını doğruluyor
        register_page.click_acik_riza_metni()
        register_page.click_membership_contrat()
        register_page.click_email_confirmation()
        register_page.click_phone_confirmation()
        register_page.click_phone_number_button("5308522975")
        time.sleep(5)  # reCaptcha doğrulamasını manuel olarak atlamak için
        register_page.click_continue_button()
        assert register_page.get_right_corner_warning_massage() == RegisterPageConstants.WARNING_TWO_ERROR
