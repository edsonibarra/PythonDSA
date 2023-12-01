from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
    
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
        current_node.next = new_node

    def prepend(self, data):
        """
        It adds a new node at the beginning of the list
        """
        pass

    def fmt_print(self):
        """
        It prints each node.data in a formatted way
        Resulting in somethig like this:
        [1]->[2]->[3]->None
        """
        if self.head is None:
            print("None")
            return
        current_node = self.head
        while current_node:
            print(f"[{current_node.data}]",end="->")
            current_node = current_node.next
        print("None")


def main():
    # Create a new linked list
    l = LinkedList()

    # Append new nodes to the list
    for n in  range(1, 5):
        l.append(n)
    
    # Print the list in a formatted way
    l.fmt_print()  # 


if __name__ == "__main__":
    main()
