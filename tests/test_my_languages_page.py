from pages.my_languages_page import MyLanguagesPage
from tests.base_test import BaseTest
from constants.my_languages_page_constants import MyLanguagesPageConstants

class TestMyLanguagesPage(BaseTest):
    #Case 1: Başarılı Dil Eklenmesi
    def test_add_language_succesfully(self):
        my_languages_page = MyLanguagesPage(self.driver)
        my_languages_page.precondition()
        my_languages_page.add_language("İngilizce")
        my_languages_page.enter_language_level("Orta")
        my_languages_page.click_save_button()
        assert my_languages_page.get_warning_massage() == MyLanguagesPageConstants.SUCCESSFULLY_ADDED