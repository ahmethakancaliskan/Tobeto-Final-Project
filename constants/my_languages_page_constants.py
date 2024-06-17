from selenium.webdriver.common.by import By


class MyLanguagesPageLocators:
    languages = (By.ID, "react-select-3-input")
    level = (By.ID, "react-select-4-input")
    save_button = (By.CSS_SELECTOR, ".btn-primary")
    warning = (By.CSS_SELECTOR, ".toast-body")

class MyLanguagesPageConstants:
    SUCCESSFULLY_ADDED = "• Yabancı dil bilgisi eklendi."
