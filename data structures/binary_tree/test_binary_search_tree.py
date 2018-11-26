from binary_search_tree import BSTNode, BST


def test_insert():
    numbers = [9, 5, 7, 8, 3, 4, 88]
    test_tree = BST()

    for num in numbers:
        test_tree.insert(num)

    assert test_tree.get_size() == len(numbers)
    assert test_tree.get_root().data == 9
    assert test_tree.get_root().left_child.data == 5
    assert test_tree.get_root().right_child.data == 88


def test_print_inorder():
    numbers = [9, 5, 7, 8, 3, 3, 4, 88, 3]
    test_tree = BST()

    for num in numbers:
        test_tree.insert(num)

    print("")
    test_tree.print_tree_inorder()


def test_print_inorder():
    numbers = [9, 5, 7, 8, 3, 3, 4, 88, 3]
    test_tree = BST()

    for num in numbers:
        test_tree.insert(num)

    print("")
    test_tree.print_tree_inorder()
