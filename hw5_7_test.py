# test_hw5_7.py

from hw5_7 import is_palindrome

def test_is_palindrome_radar():
    assert is_palindrome("radar") == True

def test_is_palindrome_madam():
    assert is_palindrome("madam") == True

def test_is_palindrome_racecar():
    assert is_palindrome("racecar") == True

def test_is_palindrome_hello():
    assert is_palindrome("hello") == False

def test_is_palindrome_empty_string():
    assert is_palindrome("") == True

def test_is_palindrome_single_character():
    assert is_palindrome("a") == True

def test_is_palindrome_mixed_case():
    assert is_palindrome("RaceCar".lower()) == True

def test_is_palindrome_with_spaces():
    assert is_palindrome("A man a plan a canal Panama".replace(" ", "").lower()) == True

if __name__ == "__main__":
    test_is_palindrome_radar()
    test_is_palindrome_madam()
    test_is_palindrome_racecar()
    test_is_palindrome_hello()
    test_is_palindrome_empty_string()
    test_is_palindrome_single_character()
    test_is_palindrome_mixed_case()
    test_is_palindrome_with_spaces()
    print("All tests pass")