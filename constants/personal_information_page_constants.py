from selenium.webdriver.common.by import By


class PersonalInformationPageLocators:
    name = (By.NAME, "name")
    surname = (By.NAME, "surname")
    phone = (By.ID, "phoneNumber")
    birth_date = (By.NAME, "birthday")
    email = (By.NAME, "email")
    national_identity = (By.NAME, "identifier")
    gender = (By.ID, "react-select-2-input")
    military_status = (By.ID, "react-select-3-input")
    disability = (By.ID, "react-select-4-input")
    github_adress = (By.NAME, "githubAddress")
    country = (By.NAME, "country")
    city = (By.NAME, "city")  #select nesnesi ile
    district = (By.NAME, "district")  #select nesnesi ile
    address = (By.NAME, "address")  # mahalle / sokak
    about_me = (By.XPATH, "//textarea[@name='description']")
    save_button = (By.CSS_SELECTOR, ".btn-primary")
    upload_picture_button = (By.CSS_SELECTOR, ".photo-edit-btn")
    upload_picture = (By.CSS_SELECTOR, ".uppy-c-btn")
    warning = (By.CSS_SELECTOR, ".toast-body")


class PersonalInformationPageConstants:
    UPDATED_SUCCESSFULLY = "• Bilgileriniz başarıyla güncellendi."
