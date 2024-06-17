from selenium.webdriver.common.by import By


class MyExperiencesPageLocators:
    corporation_name = (By.NAME, "corporationName")
    position = (By.NAME, "position")
    experience_type = (By.ID, "react-select-5-input")
    sector = (By.NAME, "sector")
    city = (By.NAME, "country")
    start_date = (By.CSS_SELECTOR, "input.react-datepicker-ignore-onclickoutside")
    end_date = (By.XPATH, "//div[@class='row mb-2']/div[@class='col-12 d-flex flex-column col-md-6 mb-6']//input[@class='form-control tobeto-input']")
    checkbox = (By.NAME, "checkbox")
    description = (By.XPATH, "//textarea[@name='description']")
    save_button = (By.CSS_SELECTOR, ".btn-primary")
    warning = (By.CLASS_NAME, "toast-body")
    char_Warn = (By.CLASS_NAME, "text-danger")


class MyExperiencesPageConstants:
    ADDED_SUCCESSFULLY = "• Deneyim eklendi."
    AT_LEAST_5_CHAR = "En az 5 karakter girmelisiniz"
    MAX_50_CHAR = "En fazla 50 karakter girebilirsiniz"
    EMPTY_FIELD = "Doldurulması zorunlu alan*"
