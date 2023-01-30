# https://contest.yandex.ru/contest/25069/problems/E/

from typing import List, Dict, Tuple
from collections import defaultdict


def read_input() -> Dict[int, List]:
    adj_list = defaultdict(list)
    num_v, num_e = list(map(int, input().split()))
    for _ in range(num_e):
        u, v = list(map(int, input().split()))
        adj_list[u].append(v)
        adj_list[v].append(u)
    for vertex in range(1, num_v + 1):
        adj_list[vertex] = adj_list.get(vertex, [])
    return adj_list

adj_list = read_input()

###------------------------------- Iterative DFS -------------------------------###

def dfs_iterative(adj_list):
    components = [-1] * (len(adj_list) + 1)
    components[0] = None
    component_count = 1

    for vertex in adj_list:
        if components[vertex] != -1:
            continue
        stack = [vertex]
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

# sorted_nodes = sorted(result.values()) #already sorted
sorted_nodes = result.values()

print(len(sorted_nodes))
for item in sorted_nodes:
    print(*item)