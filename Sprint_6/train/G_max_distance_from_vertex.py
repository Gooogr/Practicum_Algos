# https://contest.yandex.ru/contest/25069/problems/G/
from typing import List, Dict
from collections import defaultdict
from collections import deque


def read_input() -> Dict[int, List]:
    adj_list = defaultdict(list)
    num_v, num_e = list(map(int, input().split()))
    for _ in range(num_e):
        u, v = list(map(int, input().split()))
        adj_list[u].append(v)
        adj_list[v].append(u)
    for vertex in range(1, num_v + 1):
        adj_list[vertex] = adj_list.get(vertex, [])
    start_vertex = int(input())
    return adj_list, start_vertex

def bfs(graph, root):
    visited = set()
    queue =  deque([root]) 
    distance = [float('-inf')] * (len(graph) + 1)
    distance[root] = 0
    visited.add(root)
    
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                distance[neighbour] = distance[vertex] + 1
                visited.add(neighbour)
                queue.append(neighbour)
    return max(distance)

adj_list, start_vertex = read_input()
max_distance_from_vertex = bfs(adj_list, start_vertex)
print(max_distance_from_vertex)