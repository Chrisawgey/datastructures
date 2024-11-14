import time
import random

def swap(lyst, i, j):
    """Exchanges the items at positions i and j."""
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
    print(f"Swapped {lyst[i]} and {lyst[j]}: {lyst}")
    time.sleep(0.5)  

def quicksort(lyst):
    quicksortHelper(lyst, 0, len(lyst) - 1)

def quicksortHelper(lyst, left, right):
    if left < right:
        pivotLocation = partition(lyst, left, right)
        print(f"Pivot positioned at index {pivotLocation}: {lyst}")
        time.sleep(1)  # Delay to see the pivot placement
        quicksortHelper(lyst, left, pivotLocation - 1)
        quicksortHelper(lyst, pivotLocation + 1, right)

def partition(lyst, left, right):
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    print(f"Moved pivot {pivot} to the end: {lyst}")
    time.sleep(0.5)  # Delay to see the pivot move
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    # Exchange the pivot item and the boundary item
    swap(lyst, right, boundary)
    return boundary

def main(size=20, sort=quicksort):
    lyst = [random.randint(1, size + 1) for _ in range(size)]
    print("Initial list:", lyst)
    time.sleep(1)
    sort(lyst)
    print("Sorted list:", lyst)

if __name__ == "__main__":
    main()

