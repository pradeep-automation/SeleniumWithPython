import pytest
from class_to_test import SomeClassToTest


@pytest.mark.usefixtures("one_time_setup", "set_up")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self, one_time_setup):
        self.abc = SomeClassToTest(self.value)

    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 75, f"------Sum {result} is not correct  "
        print("Running Method A")

    def test_methodB(self):
        print("Running Method B")
