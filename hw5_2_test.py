# test_hw5_2.py

from hw5_2 import count

def test_count_a():
    assert count("banana", "a") == 3

def test_count_b():
    assert count("banana", "b") == 1

def test_count_c():
    assert count("banana", "c") == 0

def test_count_n():
    assert count("banana", "n") == 2

def test_count_z():
    assert count("banana", "z") == 0

def test_count_space():
    assert count("banana", " ") == 0

if __name__ == "__main__":
    test_count_a()
    test_count_b()
    test_count_c()
    test_count_n()
    test_count_z()
    test_count_space()
    print("All tests pass")