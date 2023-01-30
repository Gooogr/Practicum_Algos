# https://contest.yandex.ru/contest/25069/problems/E/

from typing import List, Dict, Tuple
from itertools import groupby
from collections import defaultdict


def read_input() -> Tuple[int, List[Tuple[int, int]]]:
    num_v, num_e = list(map(int, input().split()))
    edges = []
    for _ in range(num_e):
        u, v = list(map(int, input().split()))
        edges.append((u, v))
        edges.append((v, u))
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


###------------------------------- Iterative DFS -------------------------------###

def dfs_iterative(adj_list):
    components = [-1] * (len(adj_list) + 1)
    components[0] = None
    component_count = 1

    while -1 in set(components):
        start_vertex = components.index(-1)
        stack = [start_vertex]
        while stack:
            v = stack.pop() 
            if components[v] == -1:
                components[v] = component_count
                stack.append(v) # to backtrack it later
                for w in adj_list[v]:
                    if components[w] == -1:
                        stack.append(w)
        component_count += 1
        
    return components
components = dfs_iterative(adj_list)

###-----------------------------------------------------------------------------###


###------------------------------- Recursive DFS -------------------------------###

# # TL and RE for recursive approach
# # Components initialization
# components = [-1] * (len(adj_list) + 1)
# components[0] = None
# component_count = 1

# def dfs_traversal(v, adj_list):
#     components[v] = component_count
#     for w in adj_list[v]:
#         if components[w] == -1:
#             dfs_traversal(w, adj_list)

# def main_components(adj_list):
#     global component_count
#     for v in adj_list.keys():
#         if components[v] == -1:
#             dfs_traversal(v, adj_list)
#         component_count += 1

# main_components(adj_list)

###-----------------------------------------------------------------------------###

result = defaultdict(list)
for idx, value in enumerate(components[1:]):
    result[value].append(idx + 1)

# sorted_nodes = sorted(result.values())
sorted_nodes = result.values()

print(len(sorted_nodes))
for item in sorted_nodes:
    print(*item)