class ListNode:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def init_first(self, data):
        new_node = ListNode(data)
        self.head = new_node
        self.tail = new_node
        self.length += 1

    def push(self, data):
        if (self.length >= 1):
            new_node = ListNode(data)
            self.tail.next_node = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.init_first(data)

    def push_front(self, data):
        if (self.length >= 1):
            new_node = ListNode(data)
            new_node.next_node = self.head
            self.head = new_node
            self.length += 1
        else:
            self.init_first(data)

    def pop(self):
        if (self.length == 0):
            return
        elif (self.length == 1):
            self.head = None
            self.tail = None
            self.length = 0
        else:
            self.tail = None
            self.tail = self.head

            while (self.tail.next_node != None):
                self.tail = self.tail.next_node

    def delete(self, index):
        if (index < self.length):
            self.__delete_node(index)
        else:
            upper = self.length - 1
            raise IndexError(f"Arg ({index}) out of range f[{0}, {upper}]")

    def __delete_node(self, index):
        if (index == 0):
            temp = self.head.next_node
            self.head.next_node = None
            self.head = temp
        else:
            prev_node = None
            delete_node = self.head

            for _ in range(index):
                prev_node = delete_node
                delete_node = delete_node.next_node

            temp = delete_node.next_node
            delete_node = None
            prev_node.next_node = temp

        self.length -= 1

    def print(self):
        iterator_node = self.head

        while (iterator_node):
            print(iterator_node.data, end=" ")
            iterator_node = iterator_node.next_node
