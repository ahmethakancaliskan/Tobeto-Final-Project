import time
import pytest
from constants.event_calendar_page_constants import EventCalendarPageLocators
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class EventCalendarPage(BasePage):

    def click_calendar_button(self):
        self.wait_until_element_visible(EventCalendarPageLocators.calendar_button)
        self.find_element(EventCalendarPageLocators.calendar_button).click()

    def search_event(self, eventName):
        self.wait_until_element_visible(EventCalendarPageLocators.search_event)
        self.find_element(EventCalendarPageLocators.search_event).send_keys(eventName)
        self.save_screenshot("../Screenshots/training_calendar_page/AllRelatedEvents.png")
        # screenshot alır => Screenshots

    @pytest.mark.xfail
    def search_instructor(self):
        self.wait_until_element_visible(EventCalendarPageLocators.search_instructor)
        self.find_element(EventCalendarPageLocators.search_instructor).send_keys("Engin")
        time.sleep(2)
        self.find_element(By.CSS_SELECTOR, "react-select-2-option-0").click()
        self.save_screenshot("../Screenshots/training_calendar_page/AllEventsOfInstructor.png")
        # screenshot alır => Screenshots

    def click_all_event_status_checkbox(self):
        self.wait_until_element_visible(EventCalendarPageLocators.event_ended)
        self.find_element(EventCalendarPageLocators.event_ended).click()
        self.wait_until_element_visible(EventCalendarPageLocators.event_continue)
        self.find_element(EventCalendarPageLocators.event_continue).click()
        self.wait_until_element_visible(EventCalendarPageLocators.event_buyed)
        self.find_element(EventCalendarPageLocators.event_buyed).click()
        self.wait_until_element_visible(EventCalendarPageLocators.event_not_started)
        self.find_element(EventCalendarPageLocators.event_not_started).click()
        self.save_screenshot("../Screenshots/training_calendar_page/AllEventsOnTheCalendar.png")
        # screenshot alır => Screenshots

    def click_close_calendar_icon(self):
        self.wait_until_element_visible(EventCalendarPageLocators.close_calendar_button)
        self.find_element(EventCalendarPageLocators.close_calendar_button).click()
        self.save_screenshot("../Screenshots/training_calendar_page/CloseCalendar.png")
