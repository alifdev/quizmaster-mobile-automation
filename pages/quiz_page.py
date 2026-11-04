
import re

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class QuizPage(BasePage):

    QUESTION_COUNTER = (
        AppiumBy.XPATH,
        "//android.view.View[starts-with(@content-desc, 'Question ') "
        "and contains(@content-desc, ' / 10')]"
    )

    QUESTION_TEXT = (
        AppiumBy.XPATH,
        "//android.view.View[contains(@content-desc, '?')]"
    )

    TIMER = (
        AppiumBy.XPATH,
        "//android.view.View[number(@content-desc) >= 0 "
        "and number(@content-desc) <= 15]"
    )

    ANSWER_OPTIONS = (
        AppiumBy.XPATH,
        "//android.view.View[@clickable='true']"
    )

    ANSWER_FEEDBACK = (
    AppiumBy.XPATH,
    "//android.view.View["
    "starts-with(@content-desc, 'Correct') "
    "or starts-with(@content-desc, 'Wrong')"
    "]"
)

    def is_quiz_screen_displayed(self):
        return self.find_element(
            self.QUESTION_COUNTER
        ).is_displayed()

    def get_question_counter(self):
        return self.find_element(
            self.QUESTION_COUNTER
        ).get_attribute("content-desc")

    def get_question_text(self):
        return self.find_element(
            self.QUESTION_TEXT
        ).get_attribute("content-desc")

    def get_timer_value(self):
        timer = self.find_element(self.TIMER)
        return int(timer.get_attribute("content-desc"))

    def wait_for_timer_to_decrease(self, initial_value):
        return WebDriverWait(
            self.driver,
            5,
            poll_frequency=0.2
        ).until(
            lambda driver: self.get_timer_value() < initial_value
        )

    
    def get_answer_options(self):
        elements = self.driver.find_elements(
            *self.ANSWER_OPTIONS
        )

        return [
            element
            for element in elements
            if re.match(
                r"^[A-D]\n",
                element.get_attribute("content-desc") or ""
            )
        ]

    
    def select_answer_by_letter(self, letter):
        if letter not in ["A", "B", "C", "D"]:
            raise ValueError(
                f"Invalid answer letter: {letter}"
            )

        selected_answer = WebDriverWait(
            self.driver,
            5,
            poll_frequency=0.2
        ).until(
            lambda driver: next(
                (
                    option
                    for option in self.get_answer_options()
                    if option.get_attribute("content-desc").startswith(
                        f"{letter}\n"
                    )
                ),
                False
            )
        )

        answer_description = selected_answer.get_attribute(
            "content-desc"
        )

        selected_answer.click()

        return answer_description


    def select_first_available_answer(self):
        options = WebDriverWait(
            self.driver,
            5,
            poll_frequency=0.2
        ).until(
            lambda driver: self.get_answer_options()
        )

        selected_answer = options[0]

        answer_description = selected_answer.get_attribute(
            "content-desc"
        )

        selected_answer.click()

        return answer_description

    def get_answer_feedback(self):
        feedback = WebDriverWait(
            self.driver,
            5,
            poll_frequency=0.2
        ).until(
            lambda driver: driver.find_element(
                *self.ANSWER_FEEDBACK
            )
        )

        feedback_text = feedback.get_attribute("content-desc")

        if feedback_text.startswith("Correct"):
            return "Correct"

        if feedback_text.startswith("Wrong"):
            return "Wrong"

        raise AssertionError(
            f"Unexpected answer feedback: {feedback_text}"
        )

    
    def wait_for_next_question(self, current_question):
        def question_has_changed(driver):
            elements = driver.find_elements(
                *self.QUESTION_COUNTER
            )

            if not elements:
                return False

            displayed_question = elements[0].get_attribute(
                "content-desc"
            )

            if displayed_question != current_question:
                return displayed_question

            return False

        return WebDriverWait(
            self.driver,
            15,
            poll_frequency=0.2
        ).until(question_has_changed)
