# https://contest.yandex.ru/contest/22450/problems/B/
# https://contest.yandex.ru/contest/22450/run-report/78629798/

from typing import List, Tuple

MATRIX_SIZE = 4

def get_max_possible_points(k:int, matrix: List[List[str]]):
    count_dict = {}
    # count amount of each number in matrix
    for row in matrix:
        for item in row:
            if item != '.':
                count_dict[item] = count_dict.get(item, 0) + 1
    # find all symbols that player can handle
    max_points = 0
    for demand_amount in count_dict.values():
        if k * 2 >= demand_amount:
            max_points += 1
    return max_points

def read_input() -> Tuple[int, List[List[str]]]:
    k = int(input())
    matrix = []
    for _ in range(MATRIX_SIZE):
        matrix.append(input().strip())
    return k, matrix

k, matrix = read_input()
print(get_max_possible_points(k, matrix))
