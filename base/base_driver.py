import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def scrollWindow(self):
        pageLength = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var pageLength = "
                                                "document.body.scrollHeight;")
        match = False
        while not match:
            lastCount = pageLength
            time.sleep(3)
            pageLength = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var pageLength = "
                                                    "document.body.scrollHeight;")
            if pageLength == lastCount:
                match = True

            time.sleep(3)

    def wait_for_locator(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        wait_for_element_to_locate = wait.until(EC.presence_of_element_located((locator_type, locator)))
        return wait_for_element_to_locate

    def wait_for_locators(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        wait_for_all_elements_to_locate = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return wait_for_all_elements_to_locate
