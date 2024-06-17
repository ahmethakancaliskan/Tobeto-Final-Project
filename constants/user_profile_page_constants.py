from selenium.webdriver.common.by import By


class UserProfilePageLocators:
    side_bar = (By.CLASS_NAME, "sidebar-text")
    personal_info = (By.XPATH, "//span[.='Kişisel Bilgilerim']")
    my_experiences = (By.XPATH, "//span[.='Deneyimlerim']")
    my_education = (By.XPATH, "//span[.='Eğitim Hayatım']")
    my_skills = (By.XPATH, "//span[.='Yetkinliklerim']")
    my_certificates = (By.XPATH, "//span[.='Sertifikalarım']")
    member_communuties = (By.XPATH, "//span[.='Üye Topluluklar']")
    projects_and_awards = (By.XPATH, "//span[.='Projeler ve Ödüller']")
    my_social_media_accounts = (By.XPATH, "//span[.='Medya Hesaplarım']")
    my_languages = (By.XPATH, "//span[.='Yabancı Dillerim']")
    settings = (By.XPATH, "//span[.='Ayarlar']")


class UserProfileConstants:
    expected_sidebar = ["Kişisel Bilgilerim", "Deneyimlerim", "Eğitim Hayatım",
                        "Yetkinliklerim", "Sertifikalarım", "Üye Topluluklar",
                        "Projeler ve Ödüller", "Medya Hesaplarım", "Yabancı Dillerim",
                        "Ayarlar"]

    PERSONAL_INFORMATIONS_URL = "https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim"
    MY_EXPERIENCES_URL = "https://tobeto.com/profilim/profilimi-duzenle/deneyimlerim"
    MY_EDUCATION_URL = "https://tobeto.com/profilim/profilimi-duzenle/egitim-hayatim"
    MY_SKILLS_URL = "https://tobeto.com/profilim/profilimi-duzenle/yetkinliklerim"
    MY_CERTIFICATES_URL = "https://tobeto.com/profilim/profilimi-duzenle/sertifikalarim"
    MEMBER_COMMUNITIES_URL = "https://tobeto.com/profilim/profilimi-duzenle/topluluklar"
    PROJECTS_AND_AWARDS_URL = "https://tobeto.com/profilim/profilimi-duzenle/proje-ve-oduller"
    MY_SOCIAL_MEDIA_ACCOUNTS_URL = "https://tobeto.com/profilim/profilimi-duzenle/medya-hesaplarim"
    MY_LANGUAGES_URL = "https://tobeto.com/profilim/profilimi-duzenle/yabanci-dil"
    SETTINGS_URL = "https://tobeto.com/profilim/profilimi-duzenle/ayarlar"
