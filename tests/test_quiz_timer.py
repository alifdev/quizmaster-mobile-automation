
from pages.home_page import HomePage
from pages.quiz_page import QuizPage


def test_quiz_timer_counts_down(driver):
    home_page = HomePage(driver)
    quiz_page = QuizPage(driver)

    home_page.select_category("History")
    home_page.start_quiz()

    initial_timer = quiz_page.get_timer_value()

    assert initial_timer > 0, "Timer should start above zero."

    quiz_page.wait_for_timer_to_decrease(initial_timer)
