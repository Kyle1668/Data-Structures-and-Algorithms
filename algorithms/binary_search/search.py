"""[summary]
"""

def binary_search(arr: list, target: any):
    """[Searches through a list in log(n) time for a value]

    Args:
        arr (list): [list to be searched through]
        target (any): [target value to be searched for]

    Returns:
        [bool]: [True if target found. False if not. ]
    """

    length = len(arr)
    mid = int(length / 2)
    current_element = arr[mid]

    print(current_element)
    print(target)

    if current_element == target:
        return True
    elif length == 1:
        return False
    elif current_element > target:
        return binary_search(arr[:mid], target)
    else:
        return binary_search(arr[mid:], target)
