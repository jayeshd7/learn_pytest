import pytest
def test_cases01():
    with pytest.raises(AssertionError):
        assert 1 == 2

def test_cases02():
    with pytest.raises(ZeroDivisionError):
        assert 1/0


def test_cases03():
    with pytest.raises(Exception) as excinfo:
        assert (12, 13) == (12, 14)
    print(str(excinfo.value))


def test_cases04():
    raise Exception("This is an exception")

def test_cases05():
    with pytest.raises(Exception) as excinfo:
        test_cases04()
    print(str(excinfo.value))
    assert "exception" in str(excinfo.value)