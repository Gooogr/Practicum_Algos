# https://contest.yandex.ru/contest/23638/problems/H/

def comparator(number_1:str, number_2:str) -> bool:
    if len(number_1) == len(number_2):
        return number_1 > number_2
    else:
        var1 = number_1 + number_2
        var2 = number_2 + number_1
        return var1 > var2

def max_number_summator(numbers_arr, comparator):
    for i in range(1, len(numbers_arr)):
        item_to_insert = numbers_arr[i]
        j = i
        while j > 0 and comparator(item_to_insert, numbers_arr[j-1]):
            numbers_arr[j] = numbers_arr[j-1]
            j-= 1
            numbers_arr[j] = item_to_insert
    return numbers_arr

num = input()
numbers_arr = input().strip().split()
print("".join(max_number_summator(numbers_arr, comparator)))