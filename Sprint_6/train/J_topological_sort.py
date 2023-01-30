# https://contest.yandex.ru/contest/25069/problems/J/

from typing import List, Dict, Tuple
from itertools import groupby

def read_input() -> Tuple[int, List[Tuple[int, int]]]:
    num_v, num_e = list(map(int, input().split()))
    edges = []
    for _ in range(num_e):
        u, v = list(map(int, input().split()))
        edges.append((u, v))
    return edges, num_v

def create_adj_list(num_v: int, edges: List[Tuple[int, int]]) -> Dict[int,list]:
    adj_list = {}
    # {v1: [u1, u2, ...], ...}
    for vertex, edge_group in groupby(sorted(edges), lambda x: x[0]):
        adj_list[vertex] = [edge[1] for edge in edge_group]
    # add vertexes without edges
    for vertex in range(1, num_v + 1):
        adj_list[vertex] = adj_list.get(vertex, [])
    return adj_list

edges, num_v = read_input()
adj_list = create_adj_list(num_v, edges)

# Colors
# 1 - is white
# 2 - is grey
# 3 - is black
# string values itself leads to TE error
color = [1] * (len(adj_list) + 1)
color[0] = None


# Topological traversal order list
result_order = []

def TopSort(v, adj_list):
    color[v] = 2
    for w in adj_list[v]:
        if color[w] == 1:
            TopSort(w, adj_list)
    color[v] = 3
    result_order.append(v)

def MainTopSort(adj_list):
    for v in adj_list.keys():
        if color[v] == 1:
            TopSort(v, adj_list)

MainTopSort(adj_list)
print(*result_order[::-1])