
from unicodedata import name

from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class ResultsPage(BasePage):

    RESULT_TITLE = (
        AppiumBy.ACCESSIBILITY_ID,
        "Results"
    )

    FINAL_SCORE = (
        AppiumBy.XPATH,
        "//android.view.View["
        "contains(@content-desc, ' / 10') "
        "and not(starts-with(@content-desc, 'Question'))"
        "]"
    )

    PERFORMANCE_SUMMARY = (
        AppiumBy.XPATH,
        "//android.view.View[contains(@content-desc, '% · Time:')]"
    )

    SAVE_SCORE_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Save Score"
    )

    PLAY_AGAIN_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Play Again"
    )

    PLAYER_NAME_INPUT = (
        AppiumBy.XPATH,
        "//android.widget.EditText[@hint='Your name']"
    )

    def is_result_screen_displayed(self):
        return self.find_element(
            self.RESULT_TITLE
        ).is_displayed()

    def get_final_score(self):
        return self.find_element(
            self.FINAL_SCORE
        ).get_attribute("content-desc")

    def get_performance_summary(self):
        return self.find_element(
            self.PERFORMANCE_SUMMARY
        ).get_attribute("content-desc")

    def is_play_again_button_displayed(self):
        return self.find_element(
            self.PLAY_AGAIN_BUTTON
        ).is_displayed()

    def play_again(self):
        self.click(self.PLAY_AGAIN_BUTTON)


    def enter_player_name(self, name):
        name_field = self.find_element(self.PLAYER_NAME_INPUT)

        name_field.click()
        name_field.clear()
        name_field.send_keys(name)

        actual_name = name_field.get_attribute("text")

        print(f"\nName entered: {actual_name}")

        return actual_name

    def get_player_name(self):
        return self.find_element(
            self.PLAYER_NAME_INPUT
        ).get_attribute("text")

    def save_score(self):
        self.click(self.SAVE_SCORE_BUTTON)
