import pytest

from presidio_anonymizer.operators.initial import Initial


def test_correct_name():
    assert Initial().operator_name() == "initial"


@pytest.mark.parametrize(
    "input_text, initials",
    [
        ("John Smith", "J. S."),
        ("     Eastern    Michigan   University ", "E. M. U."),
    ],
)
def test_given_value_for_initial(input_text, initials):
    text = Initial().operate(input_text)
    assert text == initials
    
    @pytest.mark.parametrize(
    "input_text, expected",
    [
        ("@abc", "@A."),
        ("@843A", "@8."),
        ("--**abc", "--**A."),
    ],
)
    def test_leading_non_alphanumeric_is_preserved(input_text, expected):
        text = Initial().operate(input_text)
        assert text == expected
