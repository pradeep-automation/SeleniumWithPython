import pytest
from softest import TestCase, case

class TestClass(TestCase):

    def test_example(self):
        value = 5
        self.soft_assert(self.assertEqual, value, 5, "Value should be 5")
        self.soft_assert(self.assertTrue, value > 0, "value should be greater than 0")
        self.soft_assert(self.assertTrue, value % 1 == 0, "Value should be odd")
        self.assert_all()
        # assert value == 5, "Value should be 5"
        # assert value < 0, "Value should be greater than 0"
        assert value % 2 == 1, "Value should be odd"

def test_another_example():
    value = 10
    assert value == 10, "Value should be 10"
    assert value > 20, "Value should be less than 20"
    assert value % 2 == 0, "Value should be even"
