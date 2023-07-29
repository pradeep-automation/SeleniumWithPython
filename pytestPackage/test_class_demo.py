import pytest
from class_to_test import SomeClassToTest


@pytest.mark.usefixtures("one_time_setup", "set_up")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc = SomeClassToTest(10)

    def test_methodA(self):
        result = self.abc.sumNumbers(2,7)
        assert result == 10, f"------Sum {result} is not correct  "
        print("Running Method A")

    def test_methodB(self):
        print("Running Method B")
