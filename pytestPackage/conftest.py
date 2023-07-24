import pytest


@pytest.fixture
def set_up():
    print(f'\n{"Running method level setup": ^100}')
    yield
    print(f'\n{"Running method level teardown": ^100}')


@pytest.fixture(scope="module")
def one_time_setup():
    print(f'\n{"Running conftest demo one time setup": ^100}')
    yield
    print(f'{"Running conftest demo one time teardown": ^100}')


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of the operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
