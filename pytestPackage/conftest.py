import pytest


@pytest.fixture
def set_up():
    print(f'\n{"Running method level setup": ^100}')
    yield
    print(f'\n{"Running method level teardown": ^100}')


@pytest.fixture(scope="class")
def one_time_setup(request, browser, osType):
    print(f'\n{"Running conftest demo one time setup": ^100}')
    if browser == "firefox":
        value = 40
        print("Running test/s on FF")
    else:
        value = 70
        print("Running test on Chrome")
    if request.cls is not None:
        request.cls.value = value
    yield value
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
