def selectionSort(lyst):
    i = 0
    while i < len(lyst) - 1:
        minIndex = i
        j = i + 1
        while j < len(lyst):
            print(f"List: {lyst}, i: {i}, minIndex: {minIndex}, j: {j}")
            if lyst[j] < lyst[minIndex]:
                minIndex = j 
            j += 1
        if minIndex != i:
            swap(lyst, minIndex, i) 
        i += 1


def swap(lyst, a, b):
    lyst[a], lyst[b] = lyst[b], lyst[a]


lyst = [64, 25, 12, 22, 11]
selectionSort(lyst)
