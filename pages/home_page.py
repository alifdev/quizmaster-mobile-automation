
from unicodedata import category

from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class HomePage(BasePage):

    APP_TITLE = (
        AppiumBy.ACCESSIBILITY_ID,
        "QuizMaster"
    )

    CATEGORIES = [
    "Geography",
    "History",
    "Movies & TV",
    "Science",
    "Sports",
    ]

    CATEGORY_BUTTON = (
    AppiumBy.XPATH,
    "//android.widget.Button["
    "@content-desc='Choose a topic…' or "
    "@content-desc='Geography' or "
    "@content-desc='History' or "
    "@content-desc='Movies & TV' or "
    "@content-desc='Science' or "
    "@content-desc='Sports'"
    "]"
    )

    START_QUIZ_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Start Quiz"
    )

    def is_home_screen_displayed(self):
        return self.find_element(
            self.APP_TITLE
        ).is_displayed()

    def select_category(self, category):
        if category not in self.CATEGORIES:
            raise ValueError(f"Unsupported category: {category}")

        self.click(self.CATEGORY_BUTTON)

        category_locator = (
            AppiumBy.ACCESSIBILITY_ID,
            category
        )

        self.click(category_locator)

    def get_selected_category(self, category):
        selected_locator = (
            AppiumBy.ACCESSIBILITY_ID,
            category
        )

        return self.find_element(selected_locator)

    
    def start_quiz(self):
        self.click(self.START_QUIZ_BUTTON)

