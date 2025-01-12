import pytest


def expensive_computation():
    print("This is an expensive computation")
    return 23


@pytest.fixture()
def my_data(pytestconfig):
    val = pytestconfig.cache.get("example/value", None)
    if val is None:
        val = expensive_computation()
        pytestconfig.cache.set("example/value", val)
    return val


def test_function1(my_data):
    assert my_data == 23
   