from node import BSTNode


class BST:
    def __init__(self):
        self.__root_node = None
        self.__size = 0

    def get_root(self):
        return self.__root_node

    def get_size(self):
        return self.__size

    def insert(self, data):
        new_node = BSTNode(data)

        if (self.__root_node == None):
            self.__root_node = new_node
            self.__size += 1
        else:
            self.insert_recursive(new_node, self.__root_node)

    def insert_recursive(self, new_node, current_node):
        if (current_node == None):
            current_node = new_node
            self.__size += 1
        elif (new_node.data < current_node.data):
            self.insert_recursive(new_node, current_node.left_child)
        else:
            self.insert_recursive(new_node, current_node.right_child)

    def print_tree(self):
        self.print_tree_recursive(self.__root_node)

    def print_tree_recursive(self, current_node):
        if (current_node != None):
            self.print_tree_recursive(current_node.left_child)
            print(current_node.data)
            self.print_tree_recursive(current_node.right_child)
