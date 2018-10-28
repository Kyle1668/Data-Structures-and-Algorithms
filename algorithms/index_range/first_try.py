"""Write a function that returns the range of occurences of a given value
"""


def iterative_search(target: int, num_set: list) -> list:
    """Functions returns the range of occurences of a given value

    Args:
        target (int): Value to be searched for.
        num_set (list): The list to be searched through

    Returns:
        list: [description]
    """

    lower_bound = None
    upper_bound = None

    for (index, element) in enumerate(num_set):
        if element == target:
            if lower_bound == None:
                lower_bound = index
            upper_bound = index
        elif upper_bound != None:
            break

    return [lower_bound, upper_bound]
