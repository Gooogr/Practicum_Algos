# https://contest.yandex.ru/contest/25069/problems/A/

from typing import List, Tuple

def transform_graph_view(num_v: int, edges: List[Tuple[int, int]]):
    result = [None] + [0] * num_v # dummy [None] to start edges indexing from 1
    for u, v in edges:
        if result[u] == 0:
            result[u] = [1, v]
        else:
            result[u][0] += 1
            result[u].append(v)
    return result

def read_input() -> Tuple[int, List[Tuple[int, int]]]:
    num_v, num_e = list(map(int, input().split()))
    edges = []
    for _ in range(num_e):
        u, v = list(map(int, input().split()))
        edges.append((u, v))
    return num_v, edges

result = transform_graph_view(*read_input())
for item in result[1:]:
    if item != 0:
        print(*item, sep=' ')
    else:
        print(item)

        