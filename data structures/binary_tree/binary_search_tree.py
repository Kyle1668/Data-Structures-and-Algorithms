class BSTNode:
    def __init__(self, data):
        self.data = data
        self.count = 1
        self.left_child = None
        self.right_child = None


class BST:
    def __init__(self):
        self.root_node = None
        self.size = 0

    def insert(self, data):
        if (self.root_node == None):
            self.root_node = BSTNode(data)
        else:
            self.insert_helper(data, self.root_node)

    def insert_helper(self, data, current_node):
        if (current_node == None):
            current_node = BSTNode(data)
        elif (data < current_node.data):
            self.insert_helper(data, current_node.left_child)
        else:
            print(data)
            self.insert_helper(data, current_node.right_child)

    def print_tree(self, current_node):
        if (current_node != None):
            self.print_tree(current_node.left_child)
            print(current_node.data)
            self.print_tree(current_node.right_node)
