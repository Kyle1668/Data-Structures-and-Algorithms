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
        if (self.root_node is None):
            self.root_node = self.init_node(data)
        else:
            new_node = self.init_node(data)
            self.add_node_helper(new_node, self.root_node)

    def add_node_helper(self, new_node, parent_node):
        if (parent_node is None):
            parent_node = new_node
        elif (parent_node["data"] > new_node["data"]):
            self.add_node_helper(new_node, parent_node["left_node"])
        else:
            self.add_node_helper(new_node, parent_node["right_node"])


x = BinaryTree()

x.add_node(40)
x.add_node(19)
x.add_node(50)
x.add_node(7)
x.add_node(30)
x.add_node(28)
x.add_node(60)

