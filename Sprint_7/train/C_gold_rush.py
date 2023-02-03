# https://contest.yandex.ru/contest/25596/problems/C/

from typing import List, Tuple

def read_input() -> Tuple[int, List[Tuple[int, int]]]:
    bag_size = int(input())
    n = int(input())
    piles = []
    for _ in range(n):
        piles.append(tuple(map(int, input().split())))
    return bag_size, piles

def get_max_profit(bag_size: int, piles: List[Tuple[int, int]]) -> int:
    piles = sorted(piles, key=lambda x: x[0], reverse=True)
    profit = 0
    mass = 0
    for pile in piles:
        pile_price, pile_mass = pile
        if mass + pile_mass <= bag_size:
            profit += pile_price * pile_mass
            mass += pile_mass
        else:
            free_space = bag_size - mass
            profit += pile_price * free_space
            break
    return profit

bag_size, piles = read_input()
print(get_max_profit(bag_size, piles))


