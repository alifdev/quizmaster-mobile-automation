
from pages.home_page import HomePage


def test_home_screen_is_displayed(driver):
    home_page = HomePage(driver)

    assert home_page.is_home_screen_displayed()

    home_page.save_screenshot("01-home-screen.png")
