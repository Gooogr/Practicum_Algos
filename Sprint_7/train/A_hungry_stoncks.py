# https://contest.yandex.ru/contest/25596/problems/A/

from typing import List

def read_input():
    _ = input()
    arr = list(map(int, input().split()))
    return arr

def get_max_profit(arr: List[int]):
    profit = 0
    idx = 0
    purchase_phase = True 
    while idx < len(arr) - 1:
        # Meet local min - buy
        if purchase_phase and arr[idx] < arr[idx + 1]: 
            profit -= arr[idx]
            purchase_phase = False
        # Meet local max - sell
        elif not purchase_phase and arr[idx] > arr[idx + 1]: 
            profit += arr[idx]
            purchase_phase = True

        # Have stonk and didn't find final local max - sell by final max price
        if (not purchase_phase) and idx == len(arr) - 2: 
            profit += arr[idx + 1]
        idx += 1
    return profit

print(get_max_profit(read_input()))



