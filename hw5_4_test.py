# test_hw5_4.py

from hw5_4 import count_digits

def test_count_digits_101():
    assert count_digits(101) == 3

def test_count_digits_2024():
    assert count_digits(2024) == 4

def test_count_digits_102024():
    assert count_digits(102024) == 6

def test_count_digits_0():
    assert count_digits(0) == 1

if __name__ == "__main__":
    test_count_digits_101()
    test_count_digits_2024()
    test_count_digits_102024()
    test_count_digits_0()
    print("All tests pass")