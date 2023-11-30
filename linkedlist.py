from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        pass
    
    def append(self, data):
        """
        Add a new node at the end of the list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
