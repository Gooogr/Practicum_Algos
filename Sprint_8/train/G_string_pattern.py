# https://contest.yandex.ru/contest/26131/problems/G/

from typing import Tuple, List

def read_input() -> Tuple[List[int], List[int]]:
    _ = input()
    nums = list(map(int, input().split()))
    _ = input()
    pattern = list(map(int, input().split()))
    return nums, pattern

def _is_pattern(sub_nums: List[int], min_pattern: List[int]):
    assert len(sub_nums) == len(min_pattern)
    # Exlude constant from pattern [1, 3, 5] -> [0 ,2, 4]
    sub_nums_min = min(sub_nums)
    sub_nums = [val - sub_nums_min for val in sub_nums]
    return sub_nums == min_pattern

def get_start_idx(nums: List[int], pattern: List[int]):
    min_pattern_value = min(pattern)
    pattern_min = [val - min_pattern_value for val in pattern]

    result_idxs = []
    for idx in range(len(nums) - len(pattern_min) + 1):
        sub_nums = nums[idx:idx + len(pattern_min)]
        if _is_pattern(sub_nums, pattern_min):
            result_idxs.append(idx + 1) # count from 1 by task description
    return result_idxs
        
nums, pattern = read_input()
print(*get_start_idx(nums, pattern))

