class Stack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev_node = None

        def print_node(self):
            print({
                "data": self.data,
                "prev_node": self.prev_node
            })

    def __init__(self):
        self.length = 0
        self.top = None

    def push(self , data):
        new_node = self.Node(data)

        if (self.length == 0):
            self.top = new_node
        else:
            new_node.prev_node = self.top
            self.top = new_node

        self.length += 1

    def pop(self):
        if (self.length != 0):
            if (self.length == 1):
                self.top = None
            else:
                self.top = self.top.prev_node
            self.length -= 1

    def print_stack(self):
        current_node = self.top

        for i in range(0, self.length):
            current_node.print_node()
            current_node = current_node.prev_node

    def get(self, index):
        if (index < self.length):
            current_node = self.top

            for i in range(0, index + 1):
                if (i == index):
                    return current_node
                else:
                    current_node = current_node.prev_node
        else:
            return None

