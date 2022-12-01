# https://contest.yandex.ru/contest/22450/problems/A/
# https://contest.yandex.ru/contest/22450/run-report/77560006/

from typing import List

def find_distance(values: List[int]) -> List[int]:
    min_dist_left = []
    min_dist_right = []
    current_max_dist_l = len(values)
    current_max_dist_r = len(values)
    l, r = 0, len(values) - 1

    # iterate over list -> and <-
    while l <= len(values) - 1:
        if values[l] == 0:
            current_max_dist_l = 0
        if values[r] == 0:
            current_max_dist_r = 0
        min_dist_left.append(current_max_dist_l)  
        min_dist_right.append(current_max_dist_r) 
        current_max_dist_l += 1
        current_max_dist_r += 1
        l += 1
        r -= 1
        
    # select minimal distance for every pair
    result = [min(l, r) for l, r in zip(min_dist_left, min_dist_right[::-1])]
    return result
    
def read_input() -> List[int]:
    _ = int(input())
    values = list(map(int, input().strip().split()))
    return values

print(" ".join(map(str, find_distance(read_input()))))