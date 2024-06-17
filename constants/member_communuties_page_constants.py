from selenium.webdriver.common.by import By


class MemberCommunutiesPageLocators:
    communutiy_name = (By.NAME, "Name")
    role = (By.NAME, "Title")
    save_button = (By.CSS_SELECTOR, ".m-auto")
    warning = (By.CSS_SELECTOR, ".go3958317564")


class MemberCommunutiesPageConstants:
    ALREADY_ADDED = "Bu isim ve ünvan zaten sistemimizde kayıtlıdır. Lütfen farklı bir isim veya ünvan deneyin."
    VALID = "Kulüp veya topluluk bilgisi başarılı bir şekilde kaydedildi."
    
