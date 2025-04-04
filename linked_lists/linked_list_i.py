"""
Write code to demonstrate a singly linked list class with basic functionality
"""

class Node:
    """
    Node class to represent a single node in the linked list.
    """
    def __init__(self, data):
        """
        Initialize a new node with the given data.
        
        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next = None  # Initially, the next pointer is set to None

class LinkedList:
    """
    LinkedList class to represent a singly linked list.
    """
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None  # Initially, the head of the list is set to None

    def add_node(self, data):
        """
        Add a new node with the given data to the end of the linked list.
        
        Args:
            data: The data to be stored in the new node.
        """
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:
            self.head = new_node  # If the list is empty, set the new node as the head
        else:
            current = self.head
            while current.next is not None:
                current = current.next  # Traverse to the last node
            current.next = new_node  # Set the next pointer of the last node to the new node

    def print_list(self):
        """
        Print the data of all nodes in the linked list.
        """
        current = self.head
        while current is not None:
            print(current.data, end=' -> ')  # Print the data of the current node
            current = current.next  # Move to the next node
        print()

# Create a new linked list
ll = LinkedList()

# Add nodes to the linked list
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)

# Print the data of all nodes in the linked list
ll.print_list()
