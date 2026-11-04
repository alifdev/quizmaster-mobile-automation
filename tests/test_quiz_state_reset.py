
import re

from pages.home_page import HomePage
from pages.quiz_page import QuizPage
from pages.results_page import ResultsPage


def complete_quiz(quiz_page, results_page):
    """Answer all questions and return the final score."""

    for question_number in range(1, 11):
        current_question = quiz_page.get_question_counter()

        expected_question = f"Question {question_number} / 10"

        assert current_question == expected_question

        quiz_page.select_first_available_answer()
        feedback = quiz_page.get_answer_feedback()

        assert feedback in ["Correct", "Wrong"]

        if question_number < 10:
            quiz_page.wait_for_next_question(current_question)

    assert results_page.is_result_screen_displayed()

    return results_page.get_final_score()


def test_quiz_score_is_reset_after_starting_new_session(driver):
    home_page = HomePage(driver)
    quiz_page = QuizPage(driver)
    results_page = ResultsPage(driver)

    # Step 1: Start the first quiz session.
    home_page.select_category("History")
    home_page.start_quiz()

    # Step 2: Complete the first quiz.
    first_score = complete_quiz(quiz_page, results_page)

    print(f"\nFirst quiz score: {first_score}")

    # Step 3: Validate the first quiz score.
    assert re.fullmatch(r"\d+ / 10", first_score)

    first_score_value = int(first_score.split(" / ")[0])

    assert 0 <= first_score_value <= 10

    # Step 4: Return to Home Screen.
    results_page.play_again()

    assert home_page.is_home_screen_displayed()

    # Step 5: Start a new quiz session.
    home_page.start_quiz()

    assert quiz_page.is_quiz_screen_displayed()

    new_question = quiz_page.get_question_counter()

    assert new_question == "Question 1 / 10"

    # Step 6: Complete the second quiz.
    second_score = complete_quiz(quiz_page, results_page)

    print(f"Second quiz score: {second_score}")

    # Step 7: Validate the second quiz score.
    assert re.fullmatch(r"\d+ / 10", second_score), (
        f"Unexpected second quiz score: {second_score}"
    )

    second_score_value = int(second_score.split(" / ")[0])

    assert 0 <= second_score_value <= 10, (
        "Second quiz score must remain within the range of 0–10."
    )

    print("\nQuiz state reset validation completed.")
