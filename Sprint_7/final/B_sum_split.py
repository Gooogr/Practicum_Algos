# https://contest.yandex.ru/contest/25597/problems/B/

from typing import List
from copy import copy

def read_input() -> List[int]:
    _ = input()
    # to fit in 8Mb memory limit 
    nums = list(map(int, input().split()))
    return nums

def is_equal_split(nums: List[int]) -> bool:
    # trivial case - even sum
    if sum(nums) % 2: 
        return False
    
    target = sum(nums) / 2
    dp = set()
    dp.add(0)

    for val in nums:
        next_dp_part = copy(dp)
        for prev_val in dp:
            next_dp_part.add(prev_val + val)
        dp = next_dp_part
        if target in  dp:
            return True
    return False

print(is_equal_split(read_input()))

