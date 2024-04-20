import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class launchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    SEARCH = "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']"
    FILTER1 = "//p[text()='1']//parent::label"
    FILTER2 = "//p[text()='2']//parent::label"
    SELECT_DATE = "BE_flight_origin_date"
    DATE = "//td[@class!='inActiveTD' and @class!='inActiveTD weekend']"

    def launch(self, selectedDate):
        self.driver.find_element(By.ID, self.SELECT_DATE).click()
        self.wait_for_locators(By.XPATH, self.DATE)
        all_dates = self.driver.find_elements(By.XPATH, self.DATE)
        print("number of dates", len(all_dates))
        for date in all_dates:
            if date.get_attribute("data-date") == selectedDate:
                date.click()
                break
        self.wait_for_locator(By.XPATH, self.SEARCH)
        self.driver.find_element(By.XPATH, self.SEARCH).click()

    def filter(self):
        self.wait_for_locator(By.XPATH, self.FILTER2)
        self.driver.find_element(By.XPATH, self.FILTER2).click()
