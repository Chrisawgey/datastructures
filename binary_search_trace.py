
def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    
    while left <= right:
        midpoint = (left + right) // 2
        print(f"left: {left}, right: {right}, midpoint: {midpoint}, midpoint_value: {lst[midpoint]}")
        
        if lst[midpoint] == target:
            return midpoint
        elif lst[midpoint] < target:
            left = midpoint + 1
        else:
            right = midpoint - 1
            
    return -1  # Target not found

lst = [20, 44, 48, 55, 62, 66, 74, 88, 93, 99]

result_90 = binary_search(lst, 90)
print(f"Result for target 90: {result_90}\n")

result_44 = binary_search(lst, 44)
print(f"Result for target 44: {result_44}\n")
