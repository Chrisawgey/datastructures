def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):  # Outer loop: runs n-1 times
        for j in range(n-i-1):  # Inner loop: checks each pair of adjacent elements
            if arr[j] > arr[j+1]:  # Swap if elements are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(f"Step {i+1}.{j+1}: {arr}")  # Trace the list after each comparison
    return arr


arr = [5, 4, 2, 1, 3]
bubble_sort(arr)
