import pytest


class TestClass:
    var = 10

    def test_one(self):
        x = "this"
        assert "h" in x, "text not found in the given string"

    def test_two(self):
        x = "hello"
        assert hasattr(self, "var"), "not the attribute of the object"

    # pytest -q -m slow .\pytestPackage\pytestZeroToHero\test_class.py
    @pytest.mark.slow
    def test_three(self):
        self.var = 20
        assert self.var == 20

    def test_four(self):
        assert self.var == 20
