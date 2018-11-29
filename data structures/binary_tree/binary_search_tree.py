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
        if (new_node.data < current_node.data):
            if (current_node.left_child == None):
                current_node.left_child = new_node
                self.__size += 1
            else:
                self.insert_recursive(new_node, current_node.left_child)
        else:
            if (current_node.right_child == None):
                current_node.right_child = new_node
                self.__size += 1
            else:
                self.insert_recursive(new_node, current_node.right_child)

    def print_tree_inorder(self):
        self.__print_tree_recursive_inorder(self.__root_node)

    def __print_tree_recursive_inorder(self, current_node):
        if (current_node != None):
            # Left
            # Current
            # Right
            self.__print_tree_recursive_inorder(current_node.left_child)
            print(current_node.data)
            self.__print_tree_recursive_inorder(current_node.right_child)

    def print_tree_preorder(self):
        self.__print_tree_recursive_preorder(self.__root_node)

    def __print_tree_recursive_preorder(self, current_node):
        if (current_node != None):
            # Current
            # Left
            # Right
            print(current_node.data)
            self.__print_tree_recursive_preorder(current_node.left_child)
            self.__print_tree_recursive_preorder(current_node.right_child)

    def print_tree_postorder(self):
        self.__print_tree_recursive_postorder(self.__root_node)

    def __print_tree_recursive_postorder(self, current_node):
        if (current_node != None):
            # Left
            # Right
            # Current
            self.__print_tree_recursive_postorder(current_node.left_child)
            self.__print_tree_recursive_postorder(current_node.right_child)
            print(current_node.data)

    def is_bst(self):


