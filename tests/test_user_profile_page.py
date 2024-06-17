#Test Senaryosu 12

import time
import softest
from constants.user_profile_page_constants import UserProfileConstants
from constants import constant
from constants.login_page_constants import LoginPageConstants
from pages.homepage import HomePage
from pages.login_page import LoginPage
from pages.user_profile_page import UserProfilePage
from tests.base_test import BaseTest


class TestUserProfilePage(BaseTest, softest.TestCase):

    #Case 1 : Profil Başlıklarının Kontrolü
    def test_sidebar_check(self):
        login_page = LoginPage(self.driver)
        user_profile_page = UserProfilePage(self.driver)
        homepage = HomePage(self.driver)
        login_page.go_to(constant.LOGIN_PAGE_URL)
        login_page.enter_email(LoginPageConstants.VALID_EMAIL)
        login_page.enter_password(LoginPageConstants.VALID_PASSWORD)
        login_page.click_login_button()
        time.sleep(2)
        homepage.click_create_your_profile_start_button()
        assert user_profile_page.get_all_sidebar_menu() == UserProfileConstants.expected_sidebar

    #Case 2 : Profil Başlıklarının Açılmasının Kontrolü
    def test_sidebar_open(self):
        login_page = LoginPage(self.driver)
        user_profile_page = UserProfilePage(self.driver)
        homepage = HomePage(self.driver)
        login_page.go_to(constant.LOGIN_PAGE_URL)
        login_page.enter_email(LoginPageConstants.VALID_EMAIL)
        login_page.enter_password(LoginPageConstants.VALID_PASSWORD)
        login_page.click_login_button()
        time.sleep(2)
        homepage.click_create_your_profile_start_button()
        self.soft_assert(self.assertEqual, user_profile_page.get_current_url(),
                         UserProfileConstants.PERSONAL_INFORMATIONS_URL)
        user_profile_page.click_my_experiences_from_sidebar()
        self.soft_assert(self.assertEqual, user_profile_page.get_current_url(), UserProfileConstants.MY_EXPERIENCES_URL)
        user_profile_page.click_my_education_from_sidebar()
        self.soft_assert(self.assertEqual, user_profile_page.get_current_url(), UserProfileConstants.MY_EDUCATION_URL)
        user_profile_page.click_my_skills_from_sidebar()
        self.soft_assert(self.assertEqual, user_profile_page.get_current_url(), UserProfileConstants.MY_SKILLS_URL)
        user_profile_page.click_my_certificates()
        self.soft_assert(self.assertEqual, user_profile_page.get_current_url(),
                         UserProfileConstants.MY_CERTIFICATES_URL)
        user_profile_page.click_member_community_from_sidebar()
        self.soft_assert(self.assertEqual, user_profile_page.get_current_url(),
                         UserProfileConstants.MEMBER_COMMUNITIES_URL)
        user_profile_page.click_projects_and_awards_from_sidebar()
        self.soft_assert(self.assertEqual, user_profile_page.get_current_url(),
                         UserProfileConstants.PROJECTS_AND_AWARDS_URL)
        user_profile_page.click_my_social_media_accounts_from_sidebar()
        self.soft_assert(self.assertEqual, user_profile_page.get_current_url(),
                         UserProfileConstants.MY_SOCIAL_MEDIA_ACCOUNTS_URL)
        user_profile_page.click_my_languages_from_sidebar()
        self.soft_assert(self.assertEqual, user_profile_page.get_current_url(), UserProfileConstants.MY_LANGUAGES_URL)
        user_profile_page.click_settings_from_sidebar()
        self.soft_assert(self.assertEqual, user_profile_page.get_current_url(), UserProfileConstants.SETTINGS_URL)
