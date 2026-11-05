
import re

from selenium.webdriver.support.ui import WebDriverWait

from pages.home_page import HomePage
from pages.quiz_page import QuizPage
from pages.results_page import ResultsPage


def test_user_can_complete_quiz_and_view_results(driver):
    home_page = HomePage(driver)
    quiz_page = QuizPage(driver)
    results_page = ResultsPage(driver)

    # Step 1: Open the quiz.
    home_page.select_category("History")
    home_page.start_quiz()

    assert quiz_page.is_quiz_screen_displayed()

    # Step 2: Answer all 10 questions.
    total_questions = 10

    for question_number in range(1, total_questions + 1):
        current_question = quiz_page.get_question_counter()

        expected_question = f"Question {question_number} / 10"

        assert current_question == expected_question

        selected_answer = quiz_page.select_first_available_answer()
        feedback = quiz_page.get_answer_feedback()

        assert feedback in ["Correct", "Wrong"]

        print(
            f"\n{current_question}"
            f"\nSelected answer: {selected_answer}"
            f"\nFeedback: {feedback}"
        )

        # Wait for the next question, except after the final answer.
        if question_number < total_questions:
            next_question = quiz_page.wait_for_next_question(
                current_question
            )

            print(f"Progress: {next_question}")

    # Step 3: Wait for the Results screen.
    assert results_page.is_result_screen_displayed()

    results_page.save_screenshot("03-results-screen.png")

    # Step 4: Validate the final score.
    final_score = results_page.get_final_score()

    assert re.fullmatch(r"\d+ / 10", final_score), (
        f"Unexpected score format: {final_score}"
    )

    # Step 5: Validate the performance summary.
    performance_summary = results_page.get_performance_summary()

    assert re.fullmatch(
        r"\d+% · Time: \d+:\d{2}",
        performance_summary
    ), (
        f"Unexpected performance summary: {performance_summary}"
    )

    # Step 6: Validate the Play Again button.
    assert results_page.is_play_again_button_displayed()

    print(f"\nFinal score: {final_score}")
    print(f"Performance: {performance_summary}")
    print("Results screen successfully displayed.")
