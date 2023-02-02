# https://contest.yandex.ru/contest/25070/problems/B/
# https://contest.yandex.ru/contest/25070/run-report/81740325/
'''
--Описание решения--
Решение основано на поиске циклов в графе с помощью обхода в глубину.
Для оптимизации скорости будем:
* хранить граф в виде списка смежности
* логировать обход графа с помощью массива цветов.

--Доказательство корректности--
По уловоию нам необходимо проверить можно ли добраться из одной вершины в другую
с помощью двух разных типов дорог. Таким образом, если инвертировать один из типов 
ребер, то для такого графа образуется цикл.

--Временная сложность--
Поскольку граф представлен в виде списка смежности, то временная сложность
обхода в глубину оставит O(|E| + |V|),
где |E| — количество рёбер в графе, a |V| — количество вершин.

--Пространственная сложность--
Пространственная сложность составляет O(|E| + |V|)

'''


from typing import List

def read_input() -> List[List[int]]:
    '''
    Convert input in adjacent list. V vertecies correspond to list indices
    R edges are reversed
    '''
    num_v = int(input())
    adj_list = [[] for _ in range(num_v)]
    for v in range(num_v - 1):
        for idx, road_type in enumerate(input().strip()):
            u = v + idx + 1
            if road_type == 'B':
                adj_list[v].append(u)
            else: # reverse direction
                adj_list[u].append(v)
    return adj_list

def _dfs_itertative(start_vertex: int, adj_list: List[List[int]]) -> bool:
    '''
    Helper function to find loops inside one graph component
    '''
    if not adj_list:
        return True
    stack = [start_vertex] 
    while stack:
        v = stack.pop()
        if color[v] == 'white':
            color[v] = 'gray'
            stack.append(v) # to backtrack it later
            for w in adj_list[v]:
                if color[w] == 'white':
                    stack.append(w)
                if color[w] == 'gray': # Loop - gray vertex in forward move
                    return False
        # that means we moving back through visited nodes
        elif color[v] == 'gray':
            color[v] = 'black'      
    return True

def is_cycle_graph(adj_list: List[List[int]]) -> bool:
    '''
    Main function for traversal over graph
    '''
    for v in range(len(adj_list)):
        if color[v] != 'white':
            continue
        if not _dfs_itertative(v, adj_list):
            return False
    return True

adj_list = read_input()
color = ['white'] * (len(adj_list))
result = is_cycle_graph(adj_list)
print('YES' if result else 'NO')




