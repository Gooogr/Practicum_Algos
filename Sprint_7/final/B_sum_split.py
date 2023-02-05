# https://contest.yandex.ru/contest/25597/problems/B/
# https://contest.yandex.ru/contest/25597/run-report/81883782/

'''
--Описание решения--


--Доказательство корректности--


--Временная сложность--


--Пространственная сложность--

'''

from typing import List
from copy import copy

def read_input() -> List[int]:
    _ = input()
    nums = list(map(int, input().split()))
    return nums

###------------------ DP with set approach ------------------###

# Works correct, but leads to ML error becasue of Set() usage
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

###----------------- DP with array approach -----------------###

# Accepted solution
def is_equal_split(nums: List[int]) -> bool:
    # trivial case - even sum
    num_sum = sum(nums)
    if num_sum % 2: 
        return False
    # All possible sum cache in range 0 .. sum(nums)//2
    target = num_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for i in range(1, len(nums) + 1):
        for j in range(target, -1, -1):
            if j - nums[i - 1] >= 0:
                dp[j] = dp[j - nums[i - 1]] or dp[j]
    return dp[target]
    
print(is_equal_split(read_input()))

