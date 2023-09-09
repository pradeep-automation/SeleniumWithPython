import pytest


@pytest.mark.high
def test_divisible_by3(input_value):
    assert input_value%3 == 0

@pytest.mark.critical
def test_divisible_by6(input_value):
    assert input_value%13 == 0