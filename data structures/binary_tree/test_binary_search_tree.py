from binary_search_tree import BSTNode, BST


def test_insert():
    nums = [9, 5, 7, 8, 3, 3, 4, 88, 3]
    test_tree = BST()

    for num in nums:
        test_tree.insert(num)

    # test_tree.print_tree()
    assert test_tree.root_node.data == 9
    assert test_tree.root_node.left_child.data == 5
    assert test_tree.root_node.right_child.data == 88
