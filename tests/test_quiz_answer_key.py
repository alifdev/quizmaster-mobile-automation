from pages.home_page import HomePage
from pages.quiz_page import QuizPage
from utils.answer_key import AnswerKey


def test_quiz_selects_correct_answer_using_answer_key(driver):
    home_page = HomePage(driver)
    quiz_page = QuizPage(driver)
    answer_key = AnswerKey()

    # Step 1: Start a History quiz.
    home_page.select_category("History")
    home_page.start_quiz()

    # Step 2: Read the displayed question.
    question_text = quiz_page.get_question_text()

    # Step 3: Find the correct answer from JSON.
    correct_option = answer_key.get_correct_option(
        question_text,
        category_id=2
    )

    # Step 4: Select the correct answer.
    selected_answer = quiz_page.select_answer_by_letter(
        correct_option
    )

    # Step 5: Validate the selected answer.
    assert selected_answer.startswith(
        f"{correct_option}\n"
    )

    # Step 6: Validate answer feedback.
    feedback = quiz_page.get_answer_feedback()

    print(f"\nQuestion: {question_text}")
    print(f"Expected answer: {correct_option}")
    print(f"Selected answer: {selected_answer}")
    print(f"Feedback: {feedback}")

    assert feedback == "Correct", (
        f"Expected Correct feedback, but received: {feedback}"
    )