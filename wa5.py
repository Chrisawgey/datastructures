class Array:
    def __init__(self, capacity, fillValue=None):
        self.capacity = capacity
        self.fillValue = fillValue
        self.items = [fillValue] * capacity
        self.size = 0  # Track actual number of elements

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Array index out of bounds")
        return self.items[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.capacity:
            raise IndexError("Array index out of bounds")
        self.items[index] = value
        # Increment size if we are adding new items within capacity bounds
        if index >= self.size:
            self.size = index + 1

    def shrink(self):
        """Decreases the physical size of the array if necessary."""
        newSize = max(self.capacity, len(self.items) // 2)
        for _ in range(len(self.items) - newSize):
            self.items.pop()

    def pop(self, index):
        """Removes an item at a specific index and shrinks the array if needed."""
        if index < 0 or index >= self.size:
            raise IndexError("Array index out of bounds")
        
        # Store the value to return later
        removed_item = self.items[index]
        
        # Shift elements left to fill the gap
        for i in range(index, self.size - 1):
            self.items[i] = self.items[i + 1]
        
        # Fill the last element with fillValue and adjust size
        self.items[self.size - 1] = self.fillValue
        self.size -= 1
        
        # Shrink if the size condition is met
        if self.size <= len(self.items) // 4 and len(self.items) > self.capacity:
            self.shrink()
        
        return removed_item

# Testing code to add the removal of an element using the pop method
def main():
    array = Array(10)
    for i in range(5):  # Add initial values
        array.__setitem__(i, i + 1)  # Use __setitem__ explicitly or use a custom insert method
    
    print("Array before popping:", array.items[:array.size])
    
    # Remove an element and print the array again
    array.pop(2)
    print("Array after popping index 2:", array.items[:array.size])

if __name__ == "__main__":
    main()
