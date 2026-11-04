
from pages.home_page import HomePage
from pages.quiz_page import QuizPage
from pages.results_page import ResultsPage


def test_user_can_start_new_quiz_after_play_again(driver):
    home_page = HomePage(driver)
    quiz_page = QuizPage(driver)
    results_page = ResultsPage(driver)

    # Step 1: Complete the first quiz.
    home_page.select_category("History")
    home_page.start_quiz()

    for question_number in range(1, 11):
        current_question = quiz_page.get_question_counter()

        assert current_question == f"Question {question_number} / 10"

        quiz_page.select_first_available_answer()
        quiz_page.get_answer_feedback()

        if question_number < 10:
            quiz_page.wait_for_next_question(current_question)

    # Step 2: Verify the first quiz has finished.
    assert results_page.is_result_screen_displayed()

    first_score = results_page.get_final_score()

    print(f"\nFirst quiz score: {first_score}")

    # Step 3: Click Play Again.
    results_page.play_again()

    # Step 4: Verify the app returns to Home Screen.
    assert home_page.is_home_screen_displayed(), (
        "Home Screen did not appear after clicking Play Again."
    )

    print("Home Screen displayed after clicking Play Again.")

    # Step 5: Start another quiz.
    home_page.start_quiz()

    # Step 6: Verify a new quiz session has started.
    assert quiz_page.is_quiz_screen_displayed()

    new_question = quiz_page.get_question_counter()
    new_timer = quiz_page.get_timer_value()

    print(f"New quiz question: {new_question}")
    print(f"New quiz timer: {new_timer}")

    assert new_question == "Question 1 / 10", (
        f"Expected Question 1 / 10, but found {new_question}."
    )

    assert new_timer > 0, (
        "The timer should start with a positive value."
    )

    # Step 7: Verify the new quiz accepts an answer.
    selected_answer = quiz_page.select_first_available_answer()
    feedback = quiz_page.get_answer_feedback()

    print(f"Selected answer in new quiz: {selected_answer}")
    print(f"New quiz feedback: {feedback}")

    assert feedback in ["Correct", "Wrong"]
