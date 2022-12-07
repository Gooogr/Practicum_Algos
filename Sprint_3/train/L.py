# https://contest.yandex.ru/contest/23638/problems/L

from typing import List, Tuple

def find_number(x: List[int], target: int, left:int, right:int) -> int:
    if right <= left and left != 0:
        return -1
    mid = (left + right) // 2
    if (x[mid] >= target) and (x[mid -1] < target or mid == 0):
        return mid + 1
    elif target <= x[mid]: # <= not just < because of double return condition
        return find_number(x, target, left, mid)
    else:
        return find_number(x, target, mid + 1, right)

def read_input() -> Tuple[List[int], int]:
    _ = input()
    values = list(map(int, input().strip().split()))
    price = int(input())
    return values, price

values, price = read_input()
print(find_number(values, price, 0, len(values)), end=' ')
print(find_number(values, price * 2, 0, len(values)))