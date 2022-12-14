# https://contest.yandex.ru/contest/23815/problems/A/
# https://contest.yandex.ru/contest/23815/run-report/79448530/

'''
--Описание решения--
Решение основано на алгоритме бинарного поиска.
На каждом рекурсивном шаге мы определяем:
* Является ли часть массива по левую\правую сторону от точки разбиения отсортированной
* Попадает ли наш таргет в эту отсортированную часть. 
Если да - ищем его через обычную логику бинарного поиска. Если нет - разбиваем массив на части еще раз.

--Доказательство корректности--
Алгоритм сходится, так как по сути является обычным алгоритмом бинарного поиска, но с дополнительным
условием на проверку нарушения сортировки внтури частей подмассива.

--Временная сложность--
Общая временная сложность алгоритма O(log(n))

--Пространственная сложность--
Алгоритм требует O(1) дополнительной памяти 
'''

from typing import List, Union

def broken_search(
    nums: List[int], 
    target: int, 
    left:int = 0, 
    right: Union[None, int]=None
) -> int:
    '''
    Binary search in sorted and rotated array
    '''
    if right is None:
        right = len(nums) - 1
    # If we didn't find target
    if left > right:
        return -1

    middle = (left + right) // 2
    if nums[middle] == target:
        return middle
    
    # If the left part is sorted
    if nums[left] <= nums[middle]:
        # If target somewhere in the sorted part - find it with usual binary search
        if target >= nums[left] and target <= nums[middle]:
            return broken_search(nums, target, left, middle - 1)
        # If target not in sorted part - dig deeper
        else:
            return broken_search(nums, target, middle + 1, right)
    # If the left part is not sorted - the right part have to be sorted
    else:
        # Again, check if target in this sorted part
        if target >= nums[middle] and target <= nums[right]:
            return broken_search(nums, target, middle + 1, right)
        # If not - again, dig deeper
        else:
            return broken_search(nums, target, left, middle - 1)
    

def test():
    # Usual case
    arr_1 = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr_1, 5) == 6, broken_search(arr_1, 5)
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