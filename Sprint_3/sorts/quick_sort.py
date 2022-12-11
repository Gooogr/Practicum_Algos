# O(n*log(n))
# Need additional memory to store left, right, center arrays

from typing import List, Tuple

def partition(
    array: List[int], 
    pivot:int
) -> Tuple[List[int], List[int], List[int]]:
    left = [x for x in array if x < pivot]
    center = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return left, center, right

def quicksort(array: List[int]) -> List[int]:
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        left, center, right = partition(array, pivot)
        return quicksort(left) + center + quicksort(right)

arr = list(map(int, input().strip().split()))
result = quicksort(arr)
print('Input:', arr)
print('Result:', result)
