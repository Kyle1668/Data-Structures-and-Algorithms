"""[summary]
"""


def first_recurring_character(input_string: str) -> str:
    characters = {}

    for character in input_string:
        if (character in characters.keys()):
            return character
        else:
            characters[character] = 1

    return None


print(first_recurring_character("134ajajjjjjk"))
print(first_recurring_character("abcd"))
