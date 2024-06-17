#Test Senaryosu 15
import pytest

from pages.my_education_life_page import MyEducationLifePage
from tests.base_test import BaseTest
from constants.my_education_life_constants import MyEducationLifeConstants


class TestMyEducationLifePage(BaseTest):
    #Case 1: Başarılı Eğitim Eklenmesi
    def test_add_education_succesfully(self):
        my_education_life_page = MyEducationLifePage(self.driver)
        my_education_life_page.precondition()
        my_education_life_page.choose_education_degree()
        my_education_life_page.enter_university_name("Erzincan Üniversitesi")
        my_education_life_page.enter_department("Yazılımm")
        my_education_life_page.enter_start_date("2018")
        my_education_life_page.enter_end_date("2022")
        my_education_life_page.click_save_button()
        assert my_education_life_page.get_add_warning() == MyEducationLifeConstants.WARNING_ADD_EDUCATION

    #Case 2: Eklenen Eğitimin Kaldırılması
    def test_delete_education(self):
        my_education_life_page = MyEducationLifePage(self.driver)
        my_education_life_page.precondition()
        my_education_life_page.click_delete_button()
        my_education_life_page.click_confirm_delete_button()
        assert my_education_life_page.get_remove_warning() == MyEducationLifeConstants.WARNING_REMOVE_EDUCATION
