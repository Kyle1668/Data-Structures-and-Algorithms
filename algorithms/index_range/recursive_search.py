"""Write a function that returns the range of occurences of a given value
"""


def recursive_search(target: int, num_set: list) -> list:
    return recursive_search_helper(target, num_set, [0, len(num_set) - 1])


def recursive_search_helper(target: int, num_set: list, range: list) -> list:
    length = len(num_set)

    if (length != 0):
        mid_index = int(length / 2)
        middle_element = num_set[mid_index]

        if (middle_element > target):
            return recursive_search_helper(target, num_set[:mid_index], [0, mid_index])
        elif (middle_element < target):
            return recursive_search_helper(target, num_set[mid_index:], [mid_index, length])

        if (length == 1):
            return []

    else:
        return False


example = [1, 4, 5, 5, 5, 8, 9, 9]

print(recursive_search(5, example))
