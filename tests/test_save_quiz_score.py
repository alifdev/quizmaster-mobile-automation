
import xml.etree.ElementTree as ET

from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy

from pages.home_page import HomePage
from pages.quiz_page import QuizPage
from pages.results_page import ResultsPage
from utils.answer_key import AnswerKey


def test_player_can_save_quiz_score(driver):
    home_page = HomePage(driver)
    quiz_page = QuizPage(driver)
    results_page = ResultsPage(driver)
    answer_key = AnswerKey()

    # Step 1: Start a History quiz.
    home_page.select_category("History")
    home_page.start_quiz()

    # Step 2: Answer all questions correctly.
    for question_number in range(1, 11):
        current_question = quiz_page.get_question_counter()
        question_text = quiz_page.get_question_text()

        correct_option = answer_key.get_correct_option(
            question_text,
            category_id=2
        )

        quiz_page.select_answer_by_letter(correct_option)

        feedback = quiz_page.get_answer_feedback()

        assert feedback == "Correct", (
            f"Question {question_number} was not answered correctly."
        )

        if question_number < 10:
            quiz_page.wait_for_next_question(current_question)

    # Step 3: Validate the final score.
    final_score = results_page.get_final_score()

    assert final_score == "10 / 10", (
        f"Expected 10 / 10, received {final_score}."
    )

    # Step 4: Enter the player's name.
    player_name = "QA Automation"
    actual_name = results_page.enter_player_name(player_name)

    assert actual_name == player_name, (
        f"Expected player name '{player_name}', received '{actual_name}'."
    )

    # Step 5: Save the quiz score.
    results_page.save_score()

    # Step 6: Verify leaderboard navigation.
    leaderboard_title = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            "Leaderboard"
        )
    )

    assert leaderboard_title.is_displayed(), (
        "Leaderboard screen was not displayed after saving the score."
    )

        # Step 7: Verify the saved score on the leaderboard.
    page_source = driver.page_source
    root = ET.fromstring(page_source)

    leaderboard_entries = [
        element.attrib.get("content-desc", "")
        for element in root.iter()
        if element.attrib.get("content-desc")
    ]

    saved_score_found = any(
        "QA Automation" in entry
        and "10 / 10" in entry
        for entry in leaderboard_entries
    )

    assert saved_score_found, (
        "Player 'QA Automation' with score '10 / 10' "
        "was not found on the leaderboard."
    )

    print("\nPlayer score successfully saved and verified.")
    