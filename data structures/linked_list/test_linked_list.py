from linked_list import LinkedList

nums = [1, 4, 6, 7, 99, 0, -1]


def test_push():
    test_list = LinkedList()

    for number in nums:
        test_list.push(number)

    assert test_list.length == len(nums)
    assert test_list.head.data == 1
    assert test_list.tail.data == -1


def test_delete():
    test_list = LinkedList()

    for number in nums:
        test_list.push(number)

    test_list.print()

    test_list.delete(0)

    assert test_list.length == len(nums) - 1
    assert test_list.head.data == 4

    test_list.print()
