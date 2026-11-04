
from pages.home_page import HomePage
from pages.quiz_page import QuizPage


def test_quiz_moves_to_next_question_after_answer(driver):
    home_page = HomePage(driver)
    quiz_page = QuizPage(driver)

    home_page.select_category("History")
    home_page.start_quiz()

    initial_question = quiz_page.get_question_counter()

    quiz_page.select_first_available_answer()

    feedback = quiz_page.get_answer_feedback()

    next_question = quiz_page.wait_for_next_question(
        initial_question
    )

    print(f"\nInitial question: {initial_question}")
    print(f"Answer feedback: {feedback}")
    print(f"Next question: {next_question}")

    assert feedback in ["Correct", "Wrong"]
    assert next_question != initial_question
