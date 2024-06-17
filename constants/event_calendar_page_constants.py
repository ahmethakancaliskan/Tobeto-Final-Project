from selenium.webdriver.common.by import By


class EventCalendarPageLocators:
    calendar_button = (By.CSS_SELECTOR, ".calendar-btn")
    search_event = (By.ID, "search-event")
    search_instructor = (By.CSS_SELECTOR, ".css-19bb58m")
    event_ended = (By.NAME, "eventEnded")
    event_continue = (By.NAME, "eventContinue")
    event_buyed = (By.NAME, "eventBuyed")
    event_not_started = (By.NAME, "eventNotStarted")
    instructor = (By.CSS_SELECTOR, "react-select-2-option-10")
    close_calendar_button = (By.CSS_SELECTOR, ".btn-close-white")
