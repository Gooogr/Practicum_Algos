# https://contest.yandex.ru/contest/25069/problems/B/

from typing import List, Tuple

def transform_graph_view(num_v: int, edges: List[Tuple[int, int]]) -> List:
    result = [[0] * num_v for _ in range(num_v)]
    for u, v in edges:
        result[u - 1][v - 1] = 1
    return result

def read_input() -> Tuple[int, List[Tuple[int, int]]]:
    num_v, num_e = list(map(int, input().split()))
    edges = []
    for _ in range(num_e):
        u, v = list(map(int, input().split()))
        edges.append((u, v))
    return num_v, edges

result =  transform_graph_view(*read_input())
for item in result:
    print(*item)  

