# test_hw5_6.py

from hw5_6 import remove

def test_remove_empty_string():
    assert remove("", "a") == ""

def test_remove_single_character():
    assert remove("a", "a") == ""

def test_remove_character_not_in_string():
    assert remove("hello", "z") == "hello"

def test_remove_character_in_string():
    assert remove("hello", "l") == "heo"

def test_remove_all_occurrences():
    assert remove("banana", "a") == "bnn"

def test_remove_with_spaces():
    assert remove("hello world", "o") == "hell wrld"

def test_remove_numbers():
    assert remove("12345", "3") == "1245"

def test_remove_mixed_characters():
    assert remove("a1b2c3", "1") == "ab2c3"

if __name__ == "__main__":
    test_remove_empty_string()
    test_remove_single_character()
    test_remove_character_not_in_string()
    test_remove_character_in_string()
    test_remove_all_occurrences()
    test_remove_with_spaces()
    test_remove_numbers()
    test_remove_mixed_characters()
    print("All tests passed.")