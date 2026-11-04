
from pages.home_page import HomePage


def test_user_can_select_history_category(driver):
    home_page = HomePage(driver)

    home_page.select_category("History")

    selected_category = home_page.get_selected_category("History")

    assert selected_category.is_displayed()
