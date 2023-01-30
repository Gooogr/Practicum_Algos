# https://contest.yandex.ru/contest/25069/problems/D/

from typing import List, Dict, Tuple
from itertools import groupby
from collections import deque

def read_input() -> Tuple[int, List[Tuple[int, int]]]:
    num_v, num_e = list(map(int, input().split()))
    edges = []
    for _ in range(num_e):
        u, v = list(map(int, input().split()))
        edges.append((u, v))
        edges.append((v, u))
    start_vertex = int(input())
    return edges, start_vertex, num_v

def create_adj_list(num_v: int, edges: List[Tuple[int, int]]) -> Dict[int,list]:
    adj_list = {}
    # {v1: [u1, u2, ...], ...}
    for vertex, edge_group in groupby(sorted(edges), lambda x: x[0]):
        adj_list[vertex] = [edge[1] for edge in edge_group]
    # add vertexes without edges
    for vertex in range(1, num_v + 1):
        adj_list[vertex] = adj_list.get(vertex, [])
    return adj_list

edges, start_vertex, num_v = read_input()
adj_list = create_adj_list(num_v, edges)


def bfs(graph, root):
    visited = set()
    queue =  deque([root]) #because list() as queue is too slow
    traversal_result = []
    visited.add(root)

    while queue:
        vertex = queue.popleft()
        # print(str(vertex) + " ", end="")
        traversal_result.append(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return traversal_result

result = bfs(adj_list, start_vertex)
print(*result)