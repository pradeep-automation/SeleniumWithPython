"""
File name should start with test
test method name should start with test

# >>>py.test test_mod.py # run tests in the module
# >>>py.test somepath #Run all tests below somepath
# >>>py.test test_module.py::test_method   # only run test_method in test_module

-s to print statements
-v Verbose
"""


import pytest


def test_methodA(one_time_setup, set_up):
    print("-----Running DEMO3 method A")


def test_methodB(one_time_setup, set_up):
    print("-----Running DEMO3 method B")