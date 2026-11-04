
from pages.home_page import HomePage
from pages.quiz_page import QuizPage


def test_quiz_moves_to_next_question_when_timer_expires(driver):
    home_page = HomePage(driver)
    quiz_page = QuizPage(driver)

    home_page.select_category("History")
    home_page.start_quiz()

    initial_question = quiz_page.get_question_counter()
    initial_timer = quiz_page.get_timer_value()

    print(f"\nInitial question: {initial_question}")
    print(f"Initial timer: {initial_timer} seconds")

    # Do not select any answer.
    next_question = quiz_page.wait_for_next_question(
        initial_question
    )

    print(f"Next question after timeout: {next_question}")

    assert next_question != initial_question
