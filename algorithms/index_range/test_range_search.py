from iterative_search import iterative_search


def test_iterative_search():
    set_1 = [1, 2, 4, 4, 4, 5, 6, 7]
    set_2 = [1, 1, 3, 6, 88, 99]

    assert(iterative_search(4, set_1) == [2, 4])
    assert(iterative_search(6, set_2) == [3, 3])
