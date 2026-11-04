
import json
from pathlib import Path


QUESTIONS_FILE = (
    Path(__file__).resolve().parent.parent
    / "test_data"
    / "questions.json"
)


class AnswerKey:

    def __init__(self, questions_file=QUESTIONS_FILE):
        with open(questions_file, encoding="utf-8") as file:
            data = json.load(file)

        self.questions = data["questions"]

    def get_question_data(self, question_text, category_id=2):
        normalized_text = " ".join(question_text.split()).strip()

        matches = [
            question
            for question in self.questions
            if question["category_id"] == category_id
            and " ".join(question["question_text"].split()).strip()
            == normalized_text
        ]

        if len(matches) != 1:
            raise ValueError(
                f"Expected exactly one matching question, "
                f"but found {len(matches)}: {question_text}"
            )

        return matches[0]

    def get_correct_option(self, question_text, category_id=2):
        question = self.get_question_data(
            question_text,
            category_id
        )

        return question["correct_option"]
