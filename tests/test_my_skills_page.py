#Test Senaryosu 16
import pytest

from constants.my_skills_page_constants import MySkillsPageConstants
from pages.my_skills_page import MySkillsPage
from tests.base_test import BaseTest


class TestMySkillsPage(BaseTest):

    #Case 1: Başarılı Yetkinlik Eklenmesi
    def test_add_skill_succesfully(self):
        my_skills_page = MySkillsPage(self.driver)
        my_skills_page.precondition()
        my_skills_page.add_skill("Python")
        assert my_skills_page.get_warning_massage() == MySkillsPageConstants.expected_success_warning_massage

    # Case 2: Boş Bırakılan Yetkinlik Kontrol
    def test_add_empty_skill(self):
        my_skills_page = MySkillsPage(self.driver)
        my_skills_page.precondition()
        my_skills_page.click_save_button()
        assert my_skills_page.get_warning_massage() == MySkillsPageConstants.expected_empty_warning_massage
