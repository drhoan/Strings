from hw5_8 import count_substring

def test_count_substring():
    assert count_substring('love', 'love love love') == 3
    assert count_substring('is', 'This is a test. Is this a test?') == 3
    assert count_substring('are', 'are you sure you are sure?') == 2

if __name__ == "__main__":
    test_count_substring()
    print("All tests pass")
