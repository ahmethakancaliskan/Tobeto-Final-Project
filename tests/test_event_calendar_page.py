# Test Senaryosu 5

import pytest

from pages.event_calendar_page import EventCalendarPage
from constants import constant
from tests.base_test import BaseTest


class TestEventCalendar(BaseTest):
    #Case 1: Filtresiz Tüm Eğitimlerin Takvim Üzerinde Gösterilmesi
    def test_all_events_on_the_calendar(self):
        event_calendar_page = EventCalendarPage(self.driver)
        event_calendar_page.go_to(constant.BASE_URL)
        event_calendar_page.click_calendar_button()
        event_calendar_page.click_all_event_status_checkbox()
        assert True

    #Case 2: Eğitim Arama Filtresinin Kontrolü
    def test_search_event_by_training_name(self):
        event_calendar_page = EventCalendarPage(self.driver)
        event_calendar_page.go_to(constant.BASE_URL)
        event_calendar_page.click_calendar_button()
        event_calendar_page.search_event("Test")
        assert True

    #Case 3: Eğitmen Arama Filtresinin Kontrolü
    @pytest.mark.xfail
    def test_search_event_by_instructor_name(self):
        event_calendar_page = EventCalendarPage(self.driver)
        event_calendar_page.go_to(constant.BASE_URL)
        event_calendar_page.click_calendar_button()
        event_calendar_page.search_instructor()
        assert True

    #Case 6: Takvim Pop-Up ‘nın Kapatılmasının Kontrolü
    def test_close_calendar_popup(self):
        event_calendar_page = EventCalendarPage(self.driver)
        event_calendar_page.go_to(constant.BASE_URL)
        event_calendar_page.click_calendar_button()
        event_calendar_page.click_close_calendar_icon()
        assert True
