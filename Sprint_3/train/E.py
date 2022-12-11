# https://contest.yandex.ru/contest/23638/problems/E/

from typing import List, Tuple

def find_max_houses(house_prices: List[int], budget: int) -> int:
    house_prices = sorted(house_prices)
    max_house_amount = 0
    cumsum = 0
    for price in house_prices:
        if budget >= cumsum + price:
            max_house_amount += 1
            cumsum += price
    return max_house_amount

def read_input() -> Tuple[List[int], int]:
    _, budget = list(map(int, input().strip().split()))
    house_prices = list(map(int, input().strip().split()))
    return house_prices, budget

print(find_max_houses(*read_input()))