# https://contest.yandex.ru/contest/25596/problems/J/
# https://habr.com/en/post/343210/
# https://neerc.ifmo.ru/wiki/index.php?title=%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0_%D0%BE_%D0%BD%D0%B0%D0%B8%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B5%D0%B9_%D0%B2%D0%BE%D0%B7%D1%80%D0%B0%D1%81%D1%82%D0%B0%D1%8E%D1%89%D0%B5%D0%B9_%D0%BF%D0%BE%D0%B4%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8

from typing import List
from copy import copy

def get_input():
    _ = input()
    nums = list(map(int, input().split()))
    return nums

# Get size of longest subsequence without path
def get_longest_subsq(nums: List[int]):
    # store size of subsq for every element
    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        # i always before j
        for j in range(i):
            # if nums[i] is part of subsq of nums[j]
            # and counter is less then current max len of subseq
            if nums[i] > nums[j] and dp[i] <= dp[j]: 
                dp[i] = dp[j] + 1
    print(dp)
    return max(dp)

# with saved path (values)
# def get_longest_subsq(nums: List[int]):
#     pass

longest_subsq = get_longest_subsq(get_input())
# print(len(longest_subsq))
print(*longest_subsq)
