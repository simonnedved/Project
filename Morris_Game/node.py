class Node:
    def __init__(self, value=None, child=None):
        self.value = value
        self.child = child

    def print_node(self):
        print('Value:', self.value)
        print('Children:', self.child)


