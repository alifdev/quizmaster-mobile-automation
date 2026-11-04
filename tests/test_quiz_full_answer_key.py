
from pages.home_page import HomePage
from pages.quiz_page import QuizPage
from pages.results_page import ResultsPage
from utils.answer_key import AnswerKey


def test_all_history_questions_can_be_answered_correctly(driver):
    home_page = HomePage(driver)
    quiz_page = QuizPage(driver)
    answer_key = AnswerKey()

    # Step 1: Start a History quiz.
    home_page.select_category("History")
    home_page.start_quiz()

    validated_questions = []

    # Step 2: Answer all 10 questions.
    for question_number in range(1, 11):

        # Capture the current question counter BEFORE answering.
        current_question = quiz_page.get_question_counter()

        expected_counter = f"Question {question_number} / 10"

        assert current_question == expected_counter, (
            f"Unexpected question counter. "
            f"Expected {expected_counter}, "
            f"but found {current_question}."
        )

        # Read the displayed question.
        question_text = quiz_page.get_question_text()

        # Find the correct answer from JSON.
        correct_option = answer_key.get_correct_option(
            question_text,
            category_id=2
        )

        # Select the correct answer.
        selected_answer = quiz_page.select_answer_by_letter(
            correct_option
        )

        # Validate answer feedback.
        feedback = quiz_page.get_answer_feedback()

        print(f"\nQuestion {question_number}: {question_text}")
        print(f"Expected answer: {correct_option}")
        print(f"Selected answer: {selected_answer}")
        print(f"Feedback: {feedback}")

        assert feedback == "Correct", (
            f"Question {question_number} failed. "
            f"Expected Correct, received {feedback}. "
            f"Question: {question_text}"
        )

        validated_questions.append(question_text)

        # Wait for the next question.
        if question_number < 10:

            next_question = quiz_page.wait_for_next_question(
                current_question
            )

            expected_next_counter = (
                f"Question {question_number + 1} / 10"
            )

            print(f"Progressed to: {next_question}")

            assert next_question == expected_next_counter, (
                f"Question progression error. "
                f"Expected {expected_next_counter}, "
                f"but found {next_question}."
            )

    # Step 3: Validate all 10 questions.
    assert len(validated_questions) == 10

    assert len(set(validated_questions)) == 10, (
        "Duplicate questions were detected."
    )

    print("\nSuccessfully answered all 10 History questions!")

    # Step 4: Validate the final results.
    results_page = ResultsPage(driver)

    assert results_page.is_result_screen_displayed(), (
        "Results screen should be displayed after completing the quiz."
    )

    final_score = results_page.get_final_score()

    print(f"\nFinal Score: {final_score}")

    assert final_score == "10 / 10", (
        f"Expected final score 10 / 10, "
        f"but received {final_score}."
    )

    assert results_page.is_play_again_button_displayed(), (
        "Play Again button should be displayed."
    )

    print("\nPerfect score achieved: 10 / 10!")
    