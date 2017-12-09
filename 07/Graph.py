class Graph:
    nodes = []

    def append(self, node):
        self.nodes.append(node)

    def get_by_name(self, node_name):
        return list(filter(lambda node: node.name == node_name, self.nodes))[0]

    def get_parent_node(self, node_name):
        ret = list(filter(lambda node: node_name in node.children, self.nodes))
        return ret if len(ret) > 0 else None

    def __repr__(self):
        """ Debug purposes """
        return "\n".join([repr(node) for node in self.nodes])
