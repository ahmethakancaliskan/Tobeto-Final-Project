#Test Senaryosu 17
import time

import pytest

from pages.my_certificates_page import MyCertificatesPage
from tests.base_test import BaseTest


class TestMyCertificatesPage(BaseTest):
    #Case 1: Başarılı Sertifika Ekleme Kontrolü
    def test_add_certificate_succesfully(self):
        my_certificates_page = MyCertificatesPage(self.driver)
        my_certificates_page.precondition()
        my_certificates_page.enter_certificate_name("Herkes İçin Kodlama")
        my_certificates_page.enter_certificate_date("2024")
        my_certificates_page.click_upload_certificate()
        my_certificates_page.click_save_button()
        assert True
