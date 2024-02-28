import pytest

def pytest_configure():
    pytest.weekdays1 = ["mon", "tue", "wed"]
    pytest.weekdays2 = ["fri", "sat", "sun"]

@pytest.fixture(scope="module")
def setup01():
    wk = pytest.weekdays1.copy()
    wk.append("thur")
    yield wk
    print("\n Fixture setup01 closing \n")

@pytest.fixture(scope="session")
def setup02():
    wk2 = pytest.weekdays2.copy()
    wk2.insert(0, "thur")
    yield wk2
    print("\n Fixture setup02 closing \n")

@pytest.fixture()
def setup04(request):
    mon = getattr(request.module, "months")
    print("\n in Fixture setup04")
    print(f"\n Fixture Scope: {request.scope}")
    print(f"\n Calling function: {request.function.__name__}")
    print(f"\n Calling module: {request.module.__name__}")
    mon.append("April")
    yield mon

@pytest.fixture()
def setup05():
    def get_structure(name):
        if name == "list":
            return [1, 2, 3]
        elif name == "tuple":
            return (1, 2, 3)
    return get_structure
