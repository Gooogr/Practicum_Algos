# O(N)

from typing import List

def counting_sort(array: List[int], k: int):
    counted_values = [0] * k
    for value in array:
        counted_values[value] += 1
    
    idx = 0
    for value in range(k):
        if counted_values[value] != 0:
            for _ in range(counted_values[value]):
                array[idx] = value
                idx +=1

nums = [5, 7, 1, 0, 1, 5, 11, 1] 
counting_sort(nums, 12)
print(nums)