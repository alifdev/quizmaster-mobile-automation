
import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.settings import (
    APPIUM_SERVER_URL,
    PLATFORM_NAME,
    AUTOMATION_NAME,
    DEVICE_NAME,
    UDID,
    APP_PACKAGE,
    APP_ACTIVITY,
    NO_RESET,
    NEW_COMMAND_TIMEOUT,
)


@pytest.fixture
def driver():
    options = UiAutomator2Options()

    options.platform_name = PLATFORM_NAME
    options.automation_name = AUTOMATION_NAME
    options.device_name = DEVICE_NAME
    options.udid = UDID

    options.app_package = APP_PACKAGE
    options.app_activity = APP_ACTIVITY

    options.no_reset = NO_RESET
    options.new_command_timeout = NEW_COMMAND_TIMEOUT

    driver = webdriver.Remote(
        command_executor=APPIUM_SERVER_URL,
        options=options
    )

    try:
        # Restart the app to isolate each test.
        driver.terminate_app(APP_PACKAGE)
        driver.activate_app(APP_PACKAGE)

        # Wait until the Home Screen is available.
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "QuizMaster")
            )
        )

        yield driver

    finally:
        driver.quit()
