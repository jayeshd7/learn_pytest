import pytest
pytestmark = [pytest.mark.P0, pytest.mark.P1]
@pytest.mark.P0
def test_func1():
    a = 2
    b = 3
    assert a + b == 5


@pytest.mark.P0
def test_func2():
    a = 2
    b = 3
    assert a * b == 6

@pytest.mark.P0
def test_func3():
    a = 2
    b = 3
    assert a - b == -1

@pytest.mark.P1
def test_func4():
   s1 = "python is a programming language"
   assert s1.split() == ['python', 'is', 'a', 'programming', 'language']
