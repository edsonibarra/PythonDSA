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
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = current_node

    def fmt_print(self):
        """
        It prints each node.data in a formatted way
        Resulting in somethig like this:
        [1]->[2]->[3]->None
        """
        pass
