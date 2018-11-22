from binary_search_tree import BSTNode, BST


def test_insert():
    numbers = [9, 5, 7, 8, 3, 4, 88]
    test_tree = BST()

    for num in numbers:
        test_tree.insert(num)

    test_tree.print_tree()

    assert test_tree.size + 1 == len(numbers)
    assert test_tree.root_node.data == 9
    assert test_tree.root_node.left_child.data == 5
    assert test_tree.root_node.right_child.data == 88


def test_print():
    numbers = [9, 5, 7, 8, 3, 3, 4, 88, 3]
    test_tree = BST()

    for num in numbers:
        test_tree.insert(num)

    test_tree.print_tree()