# test_hw5_5.py

from hw5_5 import reverse

def test_reverse_empty_string():
    assert reverse("") == ""

def test_reverse_single_character():
    assert reverse("a") == "a"

def test_reverse_palindrome():
    assert reverse("madam") == "madam"

def test_reverse_regular_string():
    assert reverse("hello") == "olleh"

def test_reverse_with_spaces():
    assert reverse("hello world") == "dlrow olleh"

def test_reverse_with_numbers():
    assert reverse("12345") == "54321"

def test_reverse_mixed_characters():
    assert reverse("a1b2c3") == "3c2b1a"

if __name__ == "__main__":
    test_reverse_empty_string()
    test_reverse_single_character()
    test_reverse_palindrome()
    test_reverse_regular_string()
    test_reverse_with_spaces()
    test_reverse_with_numbers()
    test_reverse_mixed_characters()
    print("All tests passed.")