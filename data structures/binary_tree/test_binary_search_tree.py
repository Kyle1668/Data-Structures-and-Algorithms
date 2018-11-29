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
    numbers = [2, 1, 3]
    test_tree = BST()

    for num in numbers:
        test_tree.insert(num)

    print("\n")
    test_tree.print_tree_inorder()
    print("")


def test_print_preorder():
    numbers = [2, 1, 3]
    test_tree = BST()

    for num in numbers:
        test_tree.insert(num)

    print("\n")
    test_tree.print_tree_preorder()
    print("")


def test_print_postorder():
    numbers = [2, 1, 3]
    test_tree = BST()

    for num in numbers:
        test_tree.insert(num)

    print("\n")
    test_tree.print_tree_postorder()
    print("")


def test_bst_validation():
    numbers = [9, 5, 7, 8, 3, 4, 88]
    test_tree = BST()

    for num in numbers:
        test_tree.insert(num)

    assert test_tree.is_bst() == True

    test_tree.get_root().left_child.data = 10

    assert test_tree.is_bst() == False
