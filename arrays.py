class Array:

    def __init__(self, capacity, fillValue=None):
        self.items = list()
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self.items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self.items)

    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self.items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        return self.items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        self.items[index] = newItem

    def size(self):
        """Returns the current size of the array (number of items)."""
        return len(self.items)

    def grow(self, new_capacity, fillValue=None):
        """Grows the array to a new capacity."""
        if new_capacity > len(self.items):
            for count in range(new_capacity - len(self.items)):
                self.items.append(fillValue)
        else:
            print("New capacity must be larger than the current size.")

    def insert(self, index, newItem):
        """Inserts an item at a specific index, shifting other elements."""
        if index >= len(self.items):
            print("Index out of bounds.")
        else:
            self.items.insert(index, newItem)


# Test the new methods
a = Array(5)  # Create an array with 5 positions
print("Array length:", len(a))  # Show the number of positions

print("Initial array contents:", a)

for i in range(len(a)):
    a[i] = i + 1

print("All items in the array after assignment:")
for item in a:
    print(item)

# Test size method
print("Current size of the array:", a.size())

# Test grow method
a.grow(8)
print("Array after growing to size 8:", a)

# Test insert method
a.insert(2, 100)
print("Array after inserting 100 at index 2:", a)
