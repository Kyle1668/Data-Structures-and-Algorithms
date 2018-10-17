class BinaryTree:
    num_nodes = 0
    root_node = None

    def init_node(self, data):
        return {
            "data": data,
            "left_node": None,
            "right_node": None
        }

    def add_node(self, data):
        if (root_node is None):
            root_node = self.init_node(data)
        else:

    def add_node_helper(self, new_node, parent_node):
        if (parent_node.left_node is None):
            parent_node.left_node = new_node
        elif (parent_node.data < new_node)