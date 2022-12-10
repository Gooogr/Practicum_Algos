# https://contest.yandex.ru/contest/23638/problems/N/

from typing import List

def find_thresholds(data: List[List[int]]):
    data = sorted(data)

    # initialize result pairs by first minimal value
    result = [[data[0][0], data[0][1]]]

    for item in data[1:]:
        curr_min = item[0]
        curr_max = item[1]
        # rages intersect with last result from right side
        if curr_min <= result[-1][1]:
            # Update right side max value
            result[-1][1] = max(curr_max, result[-1][1])
        else:
            result.append([curr_min, curr_max])
    return result

def read_input():
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))
    return data

result = find_thresholds(read_input())
for item in result:
    print(f'{item[0]} {item[1]}')