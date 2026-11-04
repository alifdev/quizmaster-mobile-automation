
from pages.home_page import HomePage
from pages.quiz_page import QuizPage


def test_user_can_select_answer(driver):
    home_page = HomePage(driver)
    quiz_page = QuizPage(driver)

    home_page.select_category("History")
    home_page.start_quiz()

    selected_answer = quiz_page.select_first_available_answer()
    feedback = quiz_page.get_answer_feedback()

    print(f"\nSelected answer: {selected_answer}")
    print(f"Answer feedback: {feedback}")

    assert feedback in ["Correct", "Wrong"], (
        f"Unexpected answer feedback: {feedback}"
    )
