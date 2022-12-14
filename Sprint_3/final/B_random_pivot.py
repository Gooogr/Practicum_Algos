# https://contest.yandex.ru/contest/23815/problems/B/
# https://contest.yandex.ru/contest/23815/run-report/79450507/
'''
--Описание решения--
Решение основано на быстрой сортировке Хоара без использования дополнительной памяти
Для корректной сортировки триплетов данных баллы участников инвертированы

--Доказательство корректности--
В качестве опорного элемента выбирается случайный. Логика in-place замены 
элементов массива взята из описания задачи

--Временная сложность--
Благодаря случайному выбору опорного элемента средняя 
временная сложность гарнатированна равна O(n*Log(n))

--Пространственная сложность--
Алгоритм требует O(1) дополнительной памяти 
'''
from typing import List, Tuple
from random import randint

# TODO: add first <-> pivot ligic

def quicksort(arr: List, left:int, right:int):
    if left >= right:
        return 
    # select pivot index
    # based on https://www.geeksforgeeks.org/quicksort-using-random-pivoting/
    # Implementation using Hoare’s Partitioning
    pivot = randint(left, right)
    arr[pivot], arr[left] = arr[left], arr[pivot]
    pivot = left
    # in-place swap
    l_idx, r_idx = left, right
    while l_idx <= r_idx:
        while arr[l_idx] < arr[pivot]:
            l_idx += 1
        while arr[r_idx] > arr[pivot]:
            r_idx -= 1
        if l_idx <= r_idx: #if while condition is still valid
            arr[l_idx], arr[r_idx] = arr[r_idx], arr[l_idx]
            l_idx += 1
            r_idx -= 1
    quicksort(arr, left, r_idx)
    quicksort(arr, l_idx, right)
    
def read_input() -> List[Tuple[int, int, str]]:
    '''
    Read and prepare data triplets
    '''
    n = int(input())
    data = []
    for _ in range(n):
        name, n_task, penalty = input().strip().split()
        n_task = -1 * int(n_task) #to keep sorting order
        penalty = int(penalty) 
        data.append((n_task, penalty, name))
    return data

data = read_input()
quicksort(data, 0, len(data) - 1)
for item in data:
    print(item[2])
