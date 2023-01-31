# https://contest.yandex.ru/contest/25069/problems/K/
# https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/

from typing import List

def read_input() -> List[List[int]]:
    num_v, num_e = list(map(int, input().split()))
    result = [[0] * num_v for _ in range(num_v)]
    for _ in range(num_e):
        u, v, weight = list(map(int, input().split()))
        if result[u - 1][v - 1] == 0:
            result[u - 1][v - 1] = weight
        else: # repeated edges with different weight. We need smaller
            result[u - 1][v - 1] = min(weight, result[u - 1][v - 1])
        
        if result[v - 1][u - 1] == 0:
            result[v - 1][u - 1] = weight
        else:
            result[v - 1][u - 1] = min(weight, result[v - 1][u - 1])
    return result

adj_matrix = read_input()
vertex_amount = len(adj_matrix)
# print(adj_matrix)

def minDistance(dist, sptSet):

    # Initialize minimum distance for next node
    min = 1e7

    # Search not nearest vertex not in the
    # shortest path tree
    for v in range(vertex_amount):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v

    return min_index

def dijkstra(src):
 
        dist = [1e7] * vertex_amount
        dist[src] = 0
        sptSet = [False] * vertex_amount
 
        for _ in range(vertex_amount):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            try:
                u = minDistance(dist, sptSet)
            except:
                continue
 
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(vertex_amount):
                if (adj_matrix[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + adj_matrix[u][v]):
                    dist[v] = dist[u] + adj_matrix[u][v]
 
        return dist
result = []
for v in range(vertex_amount):
    row = dijkstra(v)
    row = [item if not isinstance(item, float) else -1 for item in row]
    result.append(row)

for row in result:
    print(*row)
