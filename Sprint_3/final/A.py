# https://contest.yandex.ru/contest/23815/problems/A/
# https://contest.yandex.ru/contest/23815/run-report/79303702/

'''
--Описание решения--
Решение основано на алгоритме бинарного поиска и разбито на 2 шага:
* Поиск индекса максимального элемента в исходном массиве данных. 
* Поиск индекса целевого элемента в нужном сегменте исходного массива данных

--Доказательство корректности--
Максимальный элемент в остортированном и сдвинутом массиве будет определять 
расстояние сдвига. Зная его, мы можем выбрать нужный нам сегмент и запустить 
бинарный поиск только внутри него, сведя задачу к обычному поиску.

--Временная сложность--
Временная сложность каждого шага - O(log(n)). Таким образом общая временная
сложность алгоритма так же O(log(n))

--Пространственная сложность--
Алгоритм требует O(1) дополнительной памяти 
'''

from typing import List, Union

#------------------------------- Helper functions ----------------------------#
def find_pivot_index(
    nums: List[int], 
    left: int=0, 
    right: Union[None, int]=None
) -> int:
    '''
    Find pivot point (index of max value) in the sorted and rotated array
    '''
    if right is None:
        right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        # Target case - value drop means pivot point
        if nums[middle] > nums[middle + 1]:
            return middle
        # If middle in the bigger part - go right
        elif nums[middle] > nums[-1]:
            return find_pivot_index(nums, middle + 1, right)
        # Else - go left
        else:
            return find_pivot_index(nums, left, middle - 1)

def binary_search(
    nums: List[int], 
    target: int, 
    left: int=0, 
    right: Union[None, int]=None
) -> int:
    '''
    Binary search in the sorted array
    '''
    if right is None:
        right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            return binary_search(nums, target, left, middle - 1)
        else:
            return binary_search(nums, target, middle + 1, right)
    return -1

#-------------------------------- Main functions -----------------------------#

def broken_search(nums: List[int], target: int) -> int:
    # Edge cases
    if len(nums) == 1:
        return 0 if nums[0] == target else -1

    # Find pivot index
    pivot_idx = find_pivot_index(nums)

    # Find target index
    # No rotation case
    if pivot_idx is None:
        return binary_search(nums, target)
    # Lucky case
    elif nums[pivot_idx] == target:
        return pivot_idx
    # Target in the bigger part
    elif nums[pivot_idx] > target and nums[0] <= target:
        return binary_search(nums, target, 0, pivot_idx)
    # Target in the smaller part
    else:
        return binary_search(nums, target, pivot_idx + 1, len(nums) - 1)

def test():
    # Usual case
    arr_1 = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr_1, 5) == 6
    # n-1 rotation
    arr_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
    assert broken_search(arr_2, 1) == 0
    # No rotation
    arr_3 = [0, 2, 6, 7, 8, 9, 10]
    assert broken_search(arr_3, 5) == -1
    # One value
    arr_4 = [1]
    assert broken_search(arr_4, 1) == 0

# TURN OFF BEFORE SUBMIT 
# test()

