
from pages.home_page import HomePage
from pages.quiz_page import QuizPage
from pages.results_page import ResultsPage
from utils.answer_key import AnswerKey


def test_quiz_score_is_calculated_correctly(driver):
    home_page = HomePage(driver)
    quiz_page = QuizPage(driver)
    results_page = ResultsPage(driver)
    answer_key = AnswerKey()

    # Step 1: Start a History quiz.
    home_page.select_category("History")
    home_page.start_quiz()

    correct_answers = 0
    wrong_answers = 0

    # Step 2: Answer 10 questions using a mixed answer strategy.
    for question_number in range(1, 11):

        current_question = quiz_page.get_question_counter()

        expected_counter = f"Question {question_number} / 10"

        assert current_question == expected_counter, (
            f"Expected {expected_counter}, "
            f"but found {current_question}."
        )

        question_text = quiz_page.get_question_text()

        correct_option = answer_key.get_correct_option(
            question_text,
            category_id=2
        )

        # Alternate between correct and incorrect answers.
        if question_number % 2 == 1:
            selected_option = correct_option
            expected_feedback = "Correct"
            correct_answers += 1

        else:
            selected_option = next(
                option for option in "ABCD"
                if option != correct_option
            )
            expected_feedback = "Wrong"
            wrong_answers += 1

        selected_answer = quiz_page.select_answer_by_letter(
            selected_option
        )

        feedback = quiz_page.get_answer_feedback()

        print(f"\nQuestion {question_number}: {question_text}")
        print(f"Expected feedback: {expected_feedback}")
        print(f"Selected answer: {selected_answer}")
        print(f"Actual feedback: {feedback}")

        assert feedback == expected_feedback, (
            f"Question {question_number}: "
            f"Expected {expected_feedback}, "
            f"received {feedback}."
        )

        # Wait for the next question.
        if question_number < 10:

            next_question = quiz_page.wait_for_next_question(
                current_question
            )

            expected_next_counter = (
                f"Question {question_number + 1} / 10"
            )

            assert next_question == expected_next_counter, (
                f"Expected {expected_next_counter}, "
                f"but found {next_question}."
            )

    # Step 3: Validate answer statistics.
    assert correct_answers == 5
    assert wrong_answers == 5

    print(f"\nCorrect answers: {correct_answers}")
    print(f"Wrong answers: {wrong_answers}")

        # Step 4: Validate the Results Screen.
    assert results_page.is_result_screen_displayed(), (
        "Results screen should be displayed after completing the quiz."
    )

    # Step 5: Validate the final score.
    final_score = results_page.get_final_score()

    print(f"\nFinal Score: {final_score}")

    assert final_score == "5 / 10", (
        f"Expected final score 5 / 10, "
        f"but received {final_score}."
    )

    # Temporary debugging: inspect Results Screen elements.
    print("\n--- RESULTS SCREEN ACCESSIBILITY HIERARCHY ---")
    print(driver.page_source)

    print("\nScore calculation validated successfully!")
