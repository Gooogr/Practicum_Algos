# https://contest.yandex.ru/contest/23638/problems/D/

from typing import List, Tuple

def find_children_amount(
    greedy_factors: List[int], 
    cookies_sizes: List[int]
) -> int:
    greedy_factors = sorted(greedy_factors, reverse=True)
    cookies_sizes = sorted(cookies_sizes)

    satisfied_childern = 0
    for factor in greedy_factors:
        if cookies_sizes and factor <= cookies_sizes[-1]:
            satisfied_childern += 1
            cookies_sizes.pop()
    return satisfied_childern


def read_input() -> Tuple[List[int], List[int]]:
    _ = input()
    greedy_factors = list(map(int, input().strip().split()))
    _ = input()
    cookies_sizes = list(map(int, input().strip().split()))
    return greedy_factors, cookies_sizes

print(find_children_amount(*read_input()))