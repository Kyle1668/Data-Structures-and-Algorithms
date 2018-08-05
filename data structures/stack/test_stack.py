from .stack import Stack


def test_push():
    test_stack = Stack()
    test_stack.push(1668)

    assert test_stack.top.data == 1668
    assert test_stack.length == 1


def test_pop():
    test_stack = Stack()
    test_stack.push(1668)
    test_stack.pop()

    assert test_stack.length == 0
    assert test_stack.top == None


def test_get():
    test_stack = Stack()
    test_stack.push(1668)
    test_stack.push(3000)
    test_stack.push(5432)

    assert test_stack.get(1).data == 3000
    assert test_stack.get(5) == None
