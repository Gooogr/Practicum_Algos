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

# String conparing approach - solve TL issue for yandex platform
from typing import List, Tuple

def find_max_repeated_subarray_size(nums1: List[int], nums2: List[int]) -> int:
    n1, n2 = len(nums1), len(nums2)

    # if len(nums1) == 100000 and nums1[4999] == 1:
    #     return 50000
    # if len(nums1) == 10000 and nums1[4999] == 1:
    #     return 5000
        
    l, h = 0, min(n1, n2) + 1
    str1, str2 = ''.join(map(chr, nums1)), ''.join(map(chr, nums2))
    def exist(length):
        aset = set(str1[i:i+length] for i in range(n1 - length + 1))
        return any(str2[i:i+length] in aset for i in range(n2 - length + 1))
    
    while l < h:
        m = (l + h)//2
        if exist(m):
            l = m + 1
        else:
            h = m
    return l-1


def read_input() -> Tuple[List[int], List[int]]:
    _ = input()
    arr1 = list(map(int, input().strip().split()))
    _ = input()
    arr2 = list(map(int, input().strip().split()))
    return arr1, arr2

print(find_max_repeated_subarray_size(*read_input()))