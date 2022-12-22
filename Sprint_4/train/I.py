# https://contest.yandex.ru/contest/23991/problems/I/

from typing import List, Tuple

# Matrix approach without rolling hash. O(m*n) but too slow anyway
def find_max_repeated_subarray_size(arr1: List[int], arr2: List[int]) -> int:
    C = len(arr1) # columns amount
    R = len(arr2) # rows amount
    result = [[0] * C] * R
    max_size = 0
    for i in range(R):
        for j in range(C):
            if arr2[i] == arr1[j]:
                if i > 0 and j > 0 and arr2[i - 1] == arr1[j - 1]:
                    result[i][j] = result[i - 1][j - 1] + 1
                else:
                    result[i][j] = 1
                max_size = max(max_size, result[i][j])
    return max_size

# Rollong hash approach


def read_input() -> Tuple[List[int], List[int]]:
    _ = input()
    arr1 = list(map(int, input().strip().split()))
    _ = input()
    arr2 = list(map(int, input().strip().split()))
    return arr1, arr2

print(find_max_repeated_subarray_size(*read_input()))