# https://contest.yandex.ru/contest/25069/problems/C/

from typing import List, Dict, Tuple
from itertools import groupby

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

# Recursive implementation leads to 
# RE error because of stack overflow
def dfs_iterative(start_vertex, adj_list):
    # Create color traking list
    color = ['white'] * (len(adj_list) + 1)
    color[0] = None

    stack = [start_vertex]
    traversal_result = []
    while stack:
        v = stack.pop() 
        if color[v] == 'white':
            traversal_result.append(v)
            color[v] = 'gray'
            stack.append(v) # to backtrack it later
            for w in adj_list[v][::-1]: # to keep correct sorted traversal order
                if color[w] == 'white':
                    stack.append(w)
        # that means we moving back through visited nodes
        elif color[v] == 'gray':
            color[v] = 'black'
    return traversal_result

edges, start_vertex, num_v = read_input()
adj_list = create_adj_list(num_v, edges)
result = dfs_iterative(start_vertex, adj_list)
print(*result)