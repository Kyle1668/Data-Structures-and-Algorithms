"""[Tests palindrome algorithm]
"""


from .valid_palindrome import is_plaindrome


def test_true():
    """[Tests true cases]
    """

    palindromes = ["Anna", "Civic", "Kayak", "Level"]

    for palindrome in palindromes:
        assert is_plaindrome(palindrome)


def test_false():
    """[Tests false cases]
    """

    wrongs = ["hey", "radd", "earch", "python", "dog"]

    for incorrect in wrongs:
        assert not is_plaindrome(incorrect)
