# https://contest.yandex.ru/contest/25069/problems/L/
# https://en.wikipedia.org/wiki/Complete_graph

n_vertex, n_edges = list(map(int, input().split()))
unique_edges = set()
for _ in range(n_edges):
    u, v = list(map(int, input().split())) 
    if u != v:
        edge = str(f'{u} {v}') if u > v else str(f'{v} {u}')
        unique_edges.add(edge)

if n_vertex * (n_vertex - 1) / 2 == len(unique_edges):
    print('YES')
else:
    print('NO')