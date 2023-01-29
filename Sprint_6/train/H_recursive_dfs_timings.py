# https://contest.yandex.ru/contest/25069/problems/H/

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


# Recursive implementation leads to 
# RE error because of stack overflow
def dfs_iterative(start_vertex, adj_list):
    # Create color traking list
    color = ['white'] * (len(adj_list) + 1)
    color[0] = None

    # Time
    time = 0
    entry = [None] * (len(adj_list) + 1)
    leave = [None] * (len(adj_list) + 1)

    stack = [start_vertex]
    while stack:
        v = stack.pop() 
        if color[v] == 'white':
            entry[v] = time
            time += 1
            color[v] = 'gray'
            stack.append(v) # to backtrack it later
            for w in adj_list[v][::-1]: # to keep correct sorted traversal order
                if color[w] == 'white':
                    stack.append(w)
        # that means we moving back through visited nodes
        elif color[v] == 'gray':
            color[v] = 'black'
            leave[v] = time
            time += 1
    return entry, leave

entry, leave = dfs_iterative(1, adj_list)

for enter_time, left_tieme in zip(entry[1:], leave[1:]):
    print(enter_time, left_tieme)
