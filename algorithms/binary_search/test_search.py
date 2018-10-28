"""[Unit Tests For Finary Search]
"""

from .search import binary_search


def test_search():
    """[Unit test for binary search]

    Args:
        arr (list): [list to be searched through]
        target (any): [target value to be searched for]
    """

    lists = [[1, 5, 7, 8, 9], [10, 15, 17, 89, 1778]]
    targets = [[1, 77, 5, 3, 2, 9, 0], [1, 77, 17, 3, 2, 10, 0]]

    for target in targets[0]:
        if (target in lists[0]):
            assert binary_search(lists[0], target)
        else:
            assert not binary_search(lists[0], target)
