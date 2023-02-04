# https://contest.yandex.ru/contest/25596/problems/F/

ladder_size, max_steps = map(int, input().split())


def total_ways(ladder_size, max_steps):
    # If ladder_size - curret_step < 0
    if ladder_size < 0:
        return 0
    # Base case
    if ladder_size < 2:
        return 1
 
    count = 0
    for i in range(1, max_steps + 1):
        count += total_ways(ladder_size - i, max_steps)
 
    return count

print(total_ways(ladder_size - 1, max_steps)) #-1 because every start from the first point




