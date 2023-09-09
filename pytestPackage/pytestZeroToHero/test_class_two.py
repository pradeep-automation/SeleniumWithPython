"""It is to validate the following flag"""
# pytest -k "MyClass and not method"

class TestMyClass:

    def test_something(self):
        print("I am somthing")
        assert 0

    def test_method_something(self):
        print("I am method something")
        assert 0
