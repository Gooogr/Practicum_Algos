# https://contest.yandex.ru/contest/23638/problems/F/

from typing import List

def is_triangle(a_max:int, b:int, c:int):
    if a_max < b + c:
        return True
    else:
        return False

def find_max_perimeter(sizes: List[int]):
    sizes = sorted(sizes, reverse=True)
    for idx in range(0, len(sizes) - 2):
        a, b, c = sizes[idx], sizes[idx + 1], sizes[idx + 2] 
        if is_triangle(a, b, c):
            return sum([a, b, c])

def read_input() -> List[int]:
    _ = input()
    sizes = list(map(int, input().strip().split()))
    return sizes

print(find_max_perimeter(read_input()))