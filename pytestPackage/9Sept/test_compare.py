import pytest


# pytestmark = pytest.mark.random_order(disabled=True)

# @pytestmark
@pytest.mark.xfail
@pytest.mark.great
def test_greater():
    num = 100
    assert num > 100

# @pytestmark
@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100


# @pytestmark
# @pytest.mark.skip
@pytest.mark.others
def test_less():
    num = 100
    assert num < 200
