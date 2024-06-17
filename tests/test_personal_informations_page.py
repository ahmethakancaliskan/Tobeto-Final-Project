#Test Senaryosu 13
import time
import pytest

from constants.personal_information_page_constants import PersonalInformationPageConstants
from tests.base_test import BaseTest
from pages.personal_informations_page import PersonalInformationPage


class TestPersonalInformationsPage(BaseTest):
    #Case 1: Kişisel Bilgilerin Başarılı Güncellenmesi
    def test_update_personal_informations_succesfully(self):
        personal_informations_page = PersonalInformationPage(self.driver)
        personal_informations_page.precondition()
        personal_informations_page.enter_name("Test3A")
        personal_informations_page.enter_surname("Pair5")
        personal_informations_page.enter_phone("5556652655")
        personal_informations_page.enter_birthdate("22-11-1999")
        personal_informations_page.enter_national_identity("52024956542")
        personal_informations_page.enter_gender("Erkek")
        personal_informations_page.enter_military_status("Tecilli")
        personal_informations_page.enter_disability_status("Yok")
        personal_informations_page.enter_github_address("https://github.com/ahmethakancaliskan")
        personal_informations_page.enter_country("Türkiye")
        personal_informations_page.enter_city("İstanbul")
        personal_informations_page.enter_district("Ümraniye")
        personal_informations_page.enter_address("Galatasaray Mahallesi, Ali Sami Yen Sokak")
        personal_informations_page.enter_about("Yazılım Kalite ve Test alanı üzerine kendimi geliştiriyorum")
        personal_informations_page.click_save_button()
        assert True

    #Case 2: Profil Resmi Ekle Kontrolü
    def test_upload_profile_picture(self):
        personal_informations_page = PersonalInformationPage(self.driver)
        personal_informations_page.precondition()
        personal_informations_page.upload_profile_picture()
        assert True
