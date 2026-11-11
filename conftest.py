
import pytest

from pathlib import Path
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
        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located(
                    (AppiumBy.ACCESSIBILITY_ID, "QuizMaster")
                )
            )

        except Exception:
            # Capture diagnostic evidence when Home Screen is not found.
            reports_dir = Path(__file__).resolve().parent / "reports"
            reports_dir.mkdir(parents=True, exist_ok=True)

            print("\n=== CI DIAGNOSTIC INFORMATION ===")

            try:
                current_activity = driver.current_activity
                print(f"Current activity: {current_activity}")
                (reports_dir / "ci-current-activity.txt").write_text(
                    str(current_activity),
                    encoding="utf-8"
                )
            except Exception as diagnostic_error:
                print(f"Could not get current activity: {diagnostic_error}")

            try:
                screenshot_path = reports_dir / "ci-home-screen.png"
                driver.save_screenshot(str(screenshot_path))
                print(f"Screenshot saved: {screenshot_path}")
            except Exception as diagnostic_error:
                print(f"Could not capture screenshot: {diagnostic_error}")

            try:
                page_source = driver.page_source
                source_path = reports_dir / "ci-page-source.xml"
                source_path.write_text(page_source, encoding="utf-8")
                print(f"Page source saved: {source_path}")
            except Exception as diagnostic_error:
                print(f"Could not capture page source: {diagnostic_error}")

            raise

        yield driver

    finally:
        driver.quit()
