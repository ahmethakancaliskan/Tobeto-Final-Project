from pages.base_page import BasePage
from constants.user_profile_page_constants import UserProfilePageLocators


class UserProfilePage(BasePage):

    def get_all_sidebar_menu(self):
        self.wait_until_element_visible(UserProfilePageLocators.side_bar)
        sidebar = self.find_elements(UserProfilePageLocators.side_bar)
        sidebar_list = []
        for i in sidebar:
            sidebar_list.append(i.text)
        return sidebar_list

    def click_personal_informations_from_sidebar(self):
        self.wait_until_element_visible(UserProfilePageLocators.personal_info)
        self.find_element(UserProfilePageLocators.personal_info).click()

    def click_my_experiences_from_sidebar(self):
        self.wait_until_element_visible(UserProfilePageLocators.my_experiences)
        self.find_element(UserProfilePageLocators.my_experiences).click()

    def click_my_education_from_sidebar(self):
        self.wait_until_element_visible(UserProfilePageLocators.my_education)
        self.find_element(UserProfilePageLocators.my_education).click()

    def click_my_skills_from_sidebar(self):
        self.wait_until_element_visible(UserProfilePageLocators.my_skills)
        self.find_element(UserProfilePageLocators.my_skills).click()

    def click_member_community_from_sidebar(self):
        self.wait_until_element_visible(UserProfilePageLocators.member_communuties)
        self.find_element(UserProfilePageLocators.member_communuties).click()

    def click_projects_and_awards_from_sidebar(self):
        self.wait_until_element_visible(UserProfilePageLocators.projects_and_awards)
        self.find_element(UserProfilePageLocators.projects_and_awards).click()

    def click_my_certificates(self):
        self.wait_until_element_visible(UserProfilePageLocators.my_certificates)
        self.find_element(UserProfilePageLocators.my_certificates).click()

    def click_my_social_media_accounts_from_sidebar(self):
        self.wait_until_element_visible(UserProfilePageLocators.my_social_media_accounts)
        self.find_element(UserProfilePageLocators.my_social_media_accounts).click()

    def click_my_languages_from_sidebar(self):
        self.wait_until_element_visible(UserProfilePageLocators.my_languages)
        self.find_element(UserProfilePageLocators.my_languages).click()

    def click_settings_from_sidebar(self):
        self.scroll_page_down(250)
        self.wait_until_element_visible(UserProfilePageLocators.settings)
        self.find_element(UserProfilePageLocators.settings).click()

