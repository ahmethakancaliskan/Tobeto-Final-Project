#Test Senaryosu 14
import time

from constants.my_experiences_page_constants import MyExperiencesPageConstants
from pages.my_experiences_page import MyExperiencesPage
from tests.base_test import BaseTest


class TestMyExperiencesPage(BaseTest):
    #Case 1: Başarılı Deneyim Ekleme Kontrolü
    def test_add_experience_succesfully(self):
        my_experiences_page = MyExperiencesPage(self.driver)
        my_experiences_page.precondition()
        my_experiences_page.enter_company_name("TOBETO")
        my_experiences_page.enter_position("YAZILIM TEST")
        my_experiences_page.enter_experience_type("Staj")
        my_experiences_page.enter_sector_name("YAZILIM")
        my_experiences_page.enter_city("İstanbul")
        my_experiences_page.enter_start_date("11.02.2023")
        my_experiences_page.click_checkbox()
        my_experiences_page.enter_description("TOBETO")
        assert True

    # Case 3: “En Az “ Karakter Kontrolü
    def test_min_5_char(self):
        my_experiences_page = MyExperiencesPage(self.driver)
        my_experiences_page.precondition()
        my_experiences_page.enter_company_name("TOBE")
        assert my_experiences_page.get_char_warning() == MyExperiencesPageConstants.AT_LEAST_5_CHAR

    # Case 4: “En Fazla “ Karakter Kontrolü
    def test_max_50_char(self):
        my_experiences_page = MyExperiencesPage(self.driver)
        my_experiences_page.precondition()
        my_experiences_page.enter_company_name("tobeaaasddsdsdsdsdsdsdsdsdsdsdsasdasdasdhgjfghfghfgasdas")
        assert my_experiences_page.get_char_warning() == MyExperiencesPageConstants.MAX_50_CHAR

    # Case 5: Boş Bırakılması Kontrolü
    def test_empty_field(self):
        my_experiences_page = MyExperiencesPage(self.driver)
        my_experiences_page.precondition()
        my_experiences_page.enter_company_name("")
        assert my_experiences_page.get_char_warning() == MyExperiencesPageConstants.EMPTY_FIELD

