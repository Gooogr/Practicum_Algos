from typing import List, Tuple

def quicksort(arr: List, left:int, right:int):
    if left >= right:
        return 
    # select pivot index
    pivot = left
    # in-place swap
    l_idx, r_idx = left, right
    while l_idx <= r_idx:
        while arr[l_idx] < arr[pivot]:
            l_idx += 1
        while arr[r_idx] > arr[pivot]:
            r_idx -= 1
        if l_idx <= r_idx: #if while condition is still valid
            arr[l_idx], arr[r_idx] = arr[r_idx], arr[l_idx]
            l_idx += 1
            r_idx -= 1
    quicksort(arr, left, r_idx)
    quicksort(arr, l_idx, right)

arr = list(map(int, input().strip().split()))
quicksort(arr, 0, len(arr) - 1)
print(arr)