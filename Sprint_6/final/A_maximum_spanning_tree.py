# https://contest.yandex.ru/contest/25070/problems/A/
# https://contest.yandex.ru/contest/25070/run-report/81700101/

'''
--Описание решения--
Решение основано на алгоритме поиска минимального остовного дерева (алгоритме Прима).
Для ускорения реализаован подход с приоритетной очередью.
Поскольку по условия задачи необходимо найти максимальное остовное дерево, то
исходные веса инвертированы, а итоговое значение выведено по модулю.

--Доказательство корректности--
Как мне подсказывает википедия, коррекотность алгоритма Прима доказывается 
через лемму о безоапсном ребре. Алгоритм MST добавляющий добавляющий безопасные 
ребра, причём делающий это ровно |V|−1  раз, корректен.
Детали: 
https://neerc.ifmo.ru/wiki/index.php?title=%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%9F%D1%80%D0%B8%D0%BC%D0%B0

--Временная сложность--
Поскольку это алгоритм Прима на основе приоритетной очереди (двоичной кучи), 
то временная сложность составляет O(|E|⋅log|V|), 
где |E| — количество рёбер в графе, a |V| — количество вершин.

--Пространственная сложность--
Пространственная сложность составляет O(|E| + |V|)

'''

from typing import List, Tuple, Set
import heapq

def read_input() -> List[List[Tuple[int, int]]]:
    n_vertex, n_edges = list(map(int, input().split()))
    adj_list = [[] for _ in range(n_vertex + 1)]
    for _ in range(n_edges):
        u, v, weight = list(map(int, input().split()))
        adj_list[u].append((v, -weight)) #negative weight for result invertion
        adj_list[v].append((u, -weight))
    return adj_list

def _add_vertex(
    v: int, 
    adj_list: List[List[Tuple[int, int]]], 
    added: Set[int], 
    edges: List[Tuple[int, int]]
) -> Tuple[Set[int], List[Tuple[int, int]]]:
    '''
    Helper function. Add all the edges (vertices and corresponded edges weights) that are 
    incidental to v, but their end is not yet in the spanning tree.
    '''
    added.add(v)
    for u, weight in adj_list[v]:
        if u not in added:
            heapq.heappush(edges, (weight, u))
    return added, edges

def find_MST(adj_list: List[List[Tuple[int, int]]]) -> int:
    '''
    Main function. Find vertices of minimal spanning tree with
    its total size. Based on the Prim's algorithm.
    '''
    added = set()          # container for all spaning tree nodes         
    edges = []             # queue for processed vertices
    spaning_tree_sum = 0   # total size of spaning tree 

    # graph can't be empty based on task description
    # so it's safe to inialize process it by 1 
    added, edges = _add_vertex(1, adj_list, added, edges) 

    # while we have accesible vertices to visit
    while len(added) < len(adj_list) and edges:
        min_weight, min_vertex = heapq.heappop(edges)
        if min_vertex not in added:
            spaning_tree_sum += min_weight
            added, edges = _add_vertex(min_vertex, adj_list, added, edges)
    return spaning_tree_sum, added

adj_list = read_input()
spaning_tree_sum, spaning_tree_edges = find_MST(adj_list)

if len(spaning_tree_edges) == len(adj_list) - 1:
    print(abs(spaning_tree_sum))
else:
    print('Oops! I did it again')



        







