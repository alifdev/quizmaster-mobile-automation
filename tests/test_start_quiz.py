
from appium.webdriver.webdriver import WebDriver

from pages.home_page import HomePage
from pages.quiz_page import QuizPage


def test_user_can_start_quiz(driver: WebDriver):
    home_page = HomePage(driver)
    quiz_page = QuizPage(driver)

    home_page.select_category("History")
    home_page.start_quiz()

    assert quiz_page.is_quiz_screen_displayed()

    quiz_page.save_screenshot("02-quiz-screen.png")

    assert quiz_page.get_question_counter() == "Question 1 / 10"

    question_text = quiz_page.get_question_text()

    print(f"\nQuestion text: {question_text}")

    assert question_text, "Question text should not be empty."
