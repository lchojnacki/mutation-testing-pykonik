import pytest

from fizzbuzz.fizzbuzz import fizzbuzz


@pytest.mark.parametrize("number", [3, 6, 9, 18])
def test_fizz(number):
    assert fizzbuzz(number) == "Fizz"


@pytest.mark.parametrize("number", [5, 10, 20, 25])
def test_buzz(number):
    assert fizzbuzz(number) == "Buzz"


@pytest.mark.parametrize("number", [1, 2, 15, 30, 45, 60])
def test_fizzbuzz(number):
    """
    This test is useless on purpose. I put it here to demonstrate what we are
    able to fix with `mutmut` and what a normal test coverage will not catch.
    """
    assert fizzbuzz(number)


@pytest.mark.parametrize("number", [1, 2, 4, 7, 8, 11])
def test_number(number):
    assert fizzbuzz(number) == str(number)
