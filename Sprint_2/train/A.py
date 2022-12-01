# https://contest.yandex.ru/contest/22779/problems/A/

from typing import List, Tuple

def get_transposed(matrix: List[List[int]], n: int, m: int) -> List[int]:
    # Здесь реализация вашего решения
    result = [[None] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][i] = matrix[i][j]
    return result
        
def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    return matrix, n, m

matrix, n, m = read_input()
matrix_t = get_transposed(matrix, n, m)
for row in matrix_t:
    print(' '.join(str(item) for item in row))
