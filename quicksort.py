def quicksort(lyst):
    quicksortHelper(Lyst, 0, len(lyst) -1)

def quicksortHelper(lyst, left, right):
    if left < right:
        pivotLocation=partition(lyst, left, right)
        quicksortHelper(lyst, pivotLocation + 1, right)

def partition (lyst, left right):
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle]=lyst[right]
    lyst[right]= pivot

    boundy = left

    for index in range(left, right):
        if lyst [index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
            