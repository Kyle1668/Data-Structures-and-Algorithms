from linked_list import LinkedList

nums = [1, 4, 6, 7, 99, 0, -1]


def test_push():
    test_list = LinkedList()

    for number in nums:
        test_list.push(number)

    assert test_list.length == len(nums)

    # Proof by induction!
    assert test_list.head.data == 1
    assert test_list.head.next_node.data == 4
    assert test_list.tail.data == -1


def test_delete():
    test_list = LinkedList()

    for number in nums:
        test_list.push(number)

    print("\n")
    test_list.print()
    print("\n")

    test_list.delete(0)

    assert test_list.length == len(nums) - 1
    assert test_list.head.data == 4

    print("\n")
    test_list.print()
    print("\n")

    test_list.delete(3)

    assert test_list.length == len(nums) - 2
    # assert test_list.head.data == 4

    print("\n")
    test_list.print()
    print("\n")
