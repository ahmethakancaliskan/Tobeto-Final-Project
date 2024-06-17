from selenium.webdriver.common.by import By


class MySkillsPageLocators:
    skills = (By.ID, "react-select-5-input")
    warning = (By.CSS_SELECTOR, ".toast-body")
    remove_button = (By.CSS_SELECTOR, " grade-delete g-del button-transparent")
    remove_confirm = (By.CSS_SELECTOR, ".btn-yes")
    save_button = (By.CSS_SELECTOR, ".btn-primary")


class MySkillsPageConstants:
    expected_success_warning_massage = "• Yetenek eklendi."
    expected_empty_warning_massage = "• Herhangi bir yetenek seçmediniz!"
    expected_remove_warning_massage = "• Yetenek kaldırıldı."
