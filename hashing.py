def KeyToIndex(item, n, hashFunc):
    return hashFunc(item) % n

def stringHash(item):
    if len(item) > 4 and (item[0].islower() or item[0].isupper()):
        item = item[1:]  # Drop first letter
    total = 0
    for ch in item:
        total += ord(ch)
    if len(item) > 2:
        total -= 2 * ord(item[-1])  
    return total


def createArray(size):
    return ["empty"] * size  # Each slot is initially marked as empty


def loadTable(aList, n, hashFunc=lambda key: key):
    table = createArray(n)  # Initialize the table
    print("n =", n, "table =", table)
    
    for item in aList:
        index = KeyToIndex(item, n, hashFunc)  # Calculate the index for the item
        print(f"Storing item '{item}' at index {index}")

        while table[index] != "empty":  # Check for collision
            print(f"Collision at index {index}, trying next slot...")
            index = (index + 1) % n  # Linear probing to the next slot

        table[index] = item  # Store the item at the resolved index
        print(f"Item '{item}' stored at index {index}")

    return table



def printTable(table):
    print("\nHash Table:")
    for i, slot in enumerate(table):
        print(f"Index {i}: {slot}")


def main():
    # Define the list of months
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    
    # Load the hash table with months
    hashTable = loadTable(months, 12, stringHash)
    print("Final Table:", hashTable)
    
    # Define the list of book numbers
    bookNumbers = [20, 30, 40, 50, 60, 70]
    
    # Load the hash table with book numbers
    hashTable = loadTable(bookNumbers, 8)
    print("Final Table:", hashTable)

if __name__ == "__main__":
    main()

