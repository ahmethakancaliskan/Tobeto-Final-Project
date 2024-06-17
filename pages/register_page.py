from pages.base_page import BasePage
from constants.register_page_constants import RegisterPageLocators


class RegisterPage(BasePage):

    def click_sign_up(self):
        self.wait_until_element_visible(RegisterPageLocators.sign_up)
        self.find_element(RegisterPageLocators.sign_up).click()

    def enter_name(self, name):
        self.wait_until_element_visible(RegisterPageLocators.name_input)
        self.find_element(RegisterPageLocators.name_input).send_keys(name)

    def enter_last_name(self, last_name):
        self.wait_until_element_visible(RegisterPageLocators.last_name_input)
        self.find_element(RegisterPageLocators.last_name_input).send_keys(last_name)
        self.scroll_page_down(450)

    def enter_mail(self, mail):
        self.wait_until_element_visible(RegisterPageLocators.mail_input)
        self.find_element(RegisterPageLocators.mail_input).send_keys(mail)

    def enter_password(self, password):
        self.wait_until_element_visible(RegisterPageLocators.password_input)
        self.find_element(RegisterPageLocators.password_input).send_keys(password)

    def enter_password_again(self, password2):
        self.wait_until_element_visible(RegisterPageLocators.password2_input)
        self.find_element(RegisterPageLocators.password2_input).send_keys(password2)

    def click_sign_up_button(self):
        self.wait_until_element_visible(RegisterPageLocators.sign_up_button)
        self.find_element(RegisterPageLocators.sign_up_button).click()

    def click_acik_riza_metni(self):
        self.wait_until_element_visible(RegisterPageLocators.acik_riza_metni)
        self.find_element(RegisterPageLocators.acik_riza_metni).click()

    def click_membership_contrat(self):
        self.wait_until_element_visible(RegisterPageLocators.membership_contrat)
        self.find_element(RegisterPageLocators.membership_contrat).click()

    def click_email_confirmation(self):
        self.wait_until_element_visible(RegisterPageLocators.email_confirmation)
        self.find_element(RegisterPageLocators.email_confirmation).click()
        self.scroll_page_down(250)

    def click_phone_confirmation(self):
        self.wait_until_element_visible(RegisterPageLocators.phone_confirmation)
        self.find_element(RegisterPageLocators.phone_confirmation).click()

    def click_continue_button(self):
        self.scroll_page_down(250)
        self.wait_until_element_visible(RegisterPageLocators.continue_button)
        self.find_element(RegisterPageLocators.continue_button).click()

    def click_phone_number_button(self, phone_number):
        self.wait_until_element_visible(RegisterPageLocators.phone_number_button)
        self.find_element(RegisterPageLocators.phone_number_button).send_keys(phone_number)
        self.scroll_page_down(50)

    def get_alert_massage(self):
        self.wait_until_element_visible(RegisterPageLocators.alert_massage)
        massage = self.find_element(RegisterPageLocators.alert_massage)
        return massage.text

    def get_phone_number_character_warning(self):
        self.wait_until_element_visible(RegisterPageLocators.phone_number_character_warning)
        massage = self.find_element(RegisterPageLocators.phone_number_character_warning)
        return massage.text

    def get_invalid_email(self):
        self.wait_until_element_visible(RegisterPageLocators.invalid_email)
        massage = self.find_element(RegisterPageLocators.invalid_email)
        return massage.text

    def get_email_input_must_fill(self):  # Email inputu boş bırakılınca verilen uyarıyı döndürür
        self.wait_until_element_visible(RegisterPageLocators.email_input_must_fill)
        massage = self.find_element(RegisterPageLocators.email_input_must_fill)
        return massage.text

    def get_right_corner_warning_massage(self):
        self.wait_until_element_visible(RegisterPageLocators.get_right_corner_warning_massage)
        massage = self.find_element(RegisterPageLocators.get_right_corner_warning_massage)
        return massage.text
