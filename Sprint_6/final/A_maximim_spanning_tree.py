# https://contest.yandex.ru/contest/25070/problems/A/

from typing import List, Tuple
import heapq

def read_input() -> List[List[Tuple[int, int]]]:
    n_vertex, n_edges = list(map(int, input().split()))
    adj_list = [[] for _ in range(n_vertex + 1)]
    for _ in range(n_edges):
        u, v, weight = list(map(int, input().split()))
        adj_list[u].append((v, weight))
        adj_list[v].append((u, weight))
    return adj_list


added = set()         
edges = []      
  

def _add_vertex(v: int, adj_list):
    added.add(v)
    for u, weight in adj_list[v]:
        if u not in added:
            heapq.heappush(edges, (-weight, u))

def find_MST(adj_list: List[List[Tuple[int, int]]]) -> int:
    spaning_tree_sum = 0  
    _add_vertex(1, adj_list) # graph can't be empty based on task description
    while len(added) < len(adj_list) and edges:
        min_weight, min_vertex = heapq.heappop(edges)
        if min_vertex not in added:
            spaning_tree_sum += min_weight
            _add_vertex(min_vertex, adj_list)
    return spaning_tree_sum

adj_list = read_input()
spaning_tree_sum = find_MST(adj_list)
print(added)
print(spaning_tree_sum)



        







