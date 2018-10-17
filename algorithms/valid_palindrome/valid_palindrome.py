"""[summary]
"""


def is_plaindrome(text: str):
    """[Checks if an argued string is a palindrome.]

    Args:
        text (str): [String to be checked]

    Returns:
        [bool]: [If the string is a palindrome or not]
    """

    parsed = list(text.lower())
    lower_index = 0
    upper_index = len(parsed) - 1

    if len(parsed) is 0:
        return False
    else:
        while (upper_index - lower_index > 1):
            if parsed[lower_index] is not parsed[upper_index]:
                return False

            lower_index += 1
            upper_index -= 1

        return True
