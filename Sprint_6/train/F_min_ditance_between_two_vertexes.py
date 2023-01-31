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
    start_v, end_v = list(map(int, input().split()))
    return adj_list, start_v, end_v

def bfs(graph, root):
    visited = set()
    queue =  deque([root]) 
    previous = [None] * (len(graph) + 1)
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                previous[neighbour] = vertex
                visited.add(neighbour)
                queue.append(neighbour)
    return previous

# path = Stack()
# current_vertex = v
# while current_vertex != None: # Предшественник вершины s равен None.
#     path.push(current_vertex)
#     current_vertex = previous[current_vertex]
# return path 

def get_shortest_path(end_v, previous):
    path = []
    current_vertex = end_v
    while current_vertex:
        path.append(current_vertex)
        current_vertex = previous[current_vertex]
    return path


adj_list, start_v, end_v = read_input()
previous = bfs(adj_list, start_v)
path = get_shortest_path(end_v, previous)
if path[0] == end_v and path[-1] == start_v:
    print(len(path) - 1)
else:
    print(-1)
