
from utils.answer_key import AnswerKey


def test_answer_key_can_find_correct_option():
    answer_key = AnswerKey()

    question_text = (
        "In which year did World War II end?"
    )

    correct_option = answer_key.get_correct_option(
        question_text,
        category_id=2
    )

    assert correct_option == "B"
