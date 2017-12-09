class Node:
    name = ""
    weight = 0
    children = []

    def __init__(self, _name, _weight, _children):
        self.name = _name
        self.weight = _weight
        self.children = _children

    def __repr__(self):
        """ Debug purposes """
        return "{} ({}) -> {}".format(self.name, self.weight, self.children)
