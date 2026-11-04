
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.settings import (
    DEMO_MODE,
    DEMO_ACTION_DELAY,
    EXPLICIT_WAIT,
)


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)

    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        self.demo_pause()

    def demo_pause(self):
        if DEMO_MODE:
            time.sleep(DEMO_ACTION_DELAY)
