class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def insert(self, data, position=None):
        new_node = Node(data)
        
        # If inserting at the beginning
        if position == 0 or not self.head:
            new_node.next = self.head
            self.head = new_node
            return

        # Insert in a specific position or at the end if position is None or greater than list length
        current = self.head
        count = 0
        while current.next and (position is None or count < position - 1):
            current = current.next
            count += 1
        
        new_node.next = current.next
        current.next = new_node

# Example Usage:
# Create linked list
linked_list = LinkedList()

# Insert elements
linked_list.insert(10)       # Insert at end or start if list is empty
linked_list.insert(20)
linked_list.insert(15, 1)    # Insert at position 1 (after the first node)

# Print the list
print("Linked List:")
linked_list.print_list()

# Get and print length
length = linked_list.get_length()
print("\nLength of list:", length)
