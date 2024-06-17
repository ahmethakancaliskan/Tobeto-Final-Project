from constants import constant
from constants.login_page_constants import LoginPageConstants
from pages.base_page import BasePage
from constants.member_communuties_page_constants import MemberCommunutiesPageLocators
from pages.homepage import HomePage
from pages.login_page import LoginPage
from pages.user_profile_page import UserProfilePage


class MemberCommunitiesPage(BasePage):
    def precondition(self):
        login_page = LoginPage(self.driver)
        login_page.go_to(constant.LOGIN_PAGE_URL)
        login_page.enter_email(LoginPageConstants.VALID_EMAIL)
        login_page.enter_password(LoginPageConstants.VALID_PASSWORD)
        login_page.click_login_button()
        homepage = HomePage(self.driver)
        homepage.click_create_your_profile_start_button()
        user_profile_page = UserProfilePage(self.driver)
        user_profile_page.click_member_community_from_sidebar()

    def enter_communutiy_name(self, name):
        self.wait_until_element_visible(MemberCommunutiesPageLocators.communutiy_name)
        self.find_element(MemberCommunutiesPageLocators.communutiy_name).send_keys(name)

    def enter_role(self, role):
        self.wait_until_element_visible(MemberCommunutiesPageLocators.role)
        self.find_element(MemberCommunutiesPageLocators.role).send_keys(role)

    def click_save_button(self):
        self.wait_until_element_visible(MemberCommunutiesPageLocators.save_button)
        self.find_element(MemberCommunutiesPageLocators.save_button).click()

    def get_warning_massage(self):
        self.wait_until_element_visible(MemberCommunutiesPageLocators.warning)
        massage = self.find_element(MemberCommunutiesPageLocators.warning)
        return massage.text
