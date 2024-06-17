from selenium.webdriver.common.by import By


class MyEducationLifeLocators:
    education_status = (By.CSS_SELECTOR, ".select__input")
    university = (By.NAME, "University")
    department = (By.NAME, "Department")
    start_Date = (By.XPATH, "//input[@placeholder='Başlangıç Yılınızı Seçiniz']")
    end_Date = (By.XPATH, "//input[@placeholder='Mezuniyet Yılınızı Seçiniz']")
    save_button = (By.CSS_SELECTOR, ".btn-primary")
    bachelor_degree = (By.ID, "react-select-2-option-2")
    warnings = (By.CLASS_NAME, "toast-body")
    remove_yes = (By.CSS_SELECTOR, ".btn-yes")
    remove_no = (By.CSS_SELECTOR, ".btn-no")
    remove_added_education = (By.CSS_SELECTOR, ".fa-solid")


class MyEducationLifeConstants:
    WARNING_REMOVE_EDUCATION = "• Eğitim kaldırıldı."
    WARNING_ADD_EDUCATION = "• Eğitim bilgisi eklendi."
