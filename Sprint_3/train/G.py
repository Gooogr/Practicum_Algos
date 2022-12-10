# https://contest.yandex.ru/contest/23638/problems/G/

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
_ = input()
nums = list(map(int, input().strip().split()))
counting_sort(nums, 3)
print(*nums)