from selenium.webdriver.common.by import By


class RegisterPageLocators:
    sign_up = (By.CSS_SELECTOR, ".signup")
    name_input = (By.NAME, "firstName")
    last_name_input = (By.NAME, "lastName")
    mail_input = (By.NAME, "email")
    password_input = (By.NAME, "password")
    password2_input = (By.NAME, "passwordAgain")
    sign_up_button = (By.CSS_SELECTOR, ".mt-4")
    acik_riza_metni = (By.XPATH, "//input[@name='contact']")
    membership_contrat = (By.XPATH, "//input[@name='membershipContrat']")
    email_confirmation = (By.XPATH, "//input[@name='emailConfirmation']")
    phone_confirmation = (By.XPATH, "//input[@name='phoneConfirmation']")
    continue_button = (By.CSS_SELECTOR, ".btn-yes")
    phone_number_button = (By.ID, "phoneNumber")
    alert_massage = (By.CSS_SELECTOR, ".alert-message")
    phone_number_character_warning = (By.CSS_SELECTOR, ".text-muted.w-90 > p")
    invalid_email = (By.CSS_SELECTOR, "form > p")
    email_input_must_fill = (
        By.XPATH, "//p[contains(text(),'Doldurulması zorunlu alan*')]")  # Email inputu boş bırakılınca verilen uyarı
    get_right_corner_warning_massage = (By.CSS_SELECTOR, ".toast-body")


class RegisterPageConstants:
    ALERT_POPUP_TITLE_TEXT = "Kayıt oluşturmak için gerekli sözleşmeler"
    WARNING_AT_LEAST_10_CHARACTER = "En az 10 karakter girmelisiniz."
    WARNING_INVALID_EMAIL = "Geçersiz e-posta adresi*"
    WARNING_EMPTY_EMAIL_INPUT_MUST_FILL = "Doldurulması zorunlu alan*"
    WARNING_MAIL_ALREADY_EXIST = "• Girdiğiniz e-posta adresi ile kayıtlı üyelik bulunmaktadır."
    WARNING_PASSWORD_CHARACTER_QUANTITY = "• Şifreniz en az 6 karakterden oluşmalıdır."
    WARNING_PASSWORDS_DO_NOT_MATCH = "• Şifreler eşleşmedi"
    WARNING_TWO_ERROR = "• 2 errors occured"
