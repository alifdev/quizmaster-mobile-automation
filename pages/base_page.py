
import time

from pathlib import Path

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

    def save_screenshot(self, filename):
        screenshot_dir = (
            Path(__file__).resolve().parent.parent
            / "screenshots"
        )

        screenshot_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        screenshot_path = screenshot_dir / filename

        self.driver.save_screenshot(
            str(screenshot_path)
        )

        print(f"\nScreenshot saved: {screenshot_path}")

        return screenshot_path
