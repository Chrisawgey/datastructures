class Array:
    def __init__(self, capacity, fillValue=None):
        self.items = [fillValue] * capacity
        self.capacity = capacity
        self.logicalSize = 0

    def __len__(self):
        return self.logicalSize

    def __getitem__(self, index):
        # Raise an exception if the index is out of bounds
        if index < 0 or index >= self.logicalSize:
            raise IndexError("Array index out of bounds")
        return self.items[index]

    def __setitem__(self, index, newItem):
        # Raise an exception if the index is out of bounds
        if index < 0 or index >= self.logicalSize:
            raise IndexError("Array index out of bounds")
        self.items[index] = newItem

    def shrink(self):
        """Decreases the physical size of the array if necessary."""
        newSize = max(self.capacity, len(self) // 2)
        for _ in range(len(self) - newSize):
            self.items.pop()

    def pop(self, index):
        """Removes and returns the item at the given index."""
        # Check if the index is out of bounds
        if index < 0 or index >= self.logicalSize:
            raise IndexError("Array index out of bounds")
        
        # Store the item to be removed in a temporary area
        removed_item = self.items[index]

        # Shift the elements to the left
        for i in range(index, self.logicalSize - 1):
            self.items[i] = self.items[i + 1]

        # Set the last element to the fill value (assuming None here)
        self.items[self.logicalSize - 1] = None

        # Decrease the logical size by one
        self.logicalSize -= 1

        # Call shrink method if needed
        if self.logicalSize <= len(self) // 4 and len(self) > self.capacity:
            self.shrink()

        # Return the removed item
        return removed_item

# Testing the Array class and the pop method
def main():
    # Create an array with a capacity of 10
    myArray = Array(10)
    
    # Fill the array with values
    for i in range(6):
        myArray[i] = i + 1
        myArray.logicalSize += 1  # Manually adjust logical size

    print("Original Array:", myArray.items)

    # Remove an element using pop
    removed_value = myArray.pop(3)
    print(f"Removed value: {removed_value}")
    print("Array after pop:", myArray.items)

if __name__ == "__main__":
    main()
