# https://contest.yandex.ru/contest/25596/problems/B/

from typing import List

def read_input() -> List[List[float]]:
    n_rows = int(input())
    rows = []
    for _ in range(n_rows):
        rows.append(list(map(float, input().split())))
    return rows

def get_optimal_schedule(rows: List[List[float]]):
    rows = sorted(rows, key=lambda x: (x[1], x[0]))
    schedule = [rows[0]]
    for start, end in rows[1:]:
        # if last already added lesson end before new candidate
        if schedule[-1][1] <= start:
            schedule.append([start, end])
    return schedule
    
result = get_optimal_schedule(read_input())
print(len(result))
for start, end in result:
    if round(start) == start:
        start = round(start)
    if round(end) == end:
        end = round(end)
    print(start, end)

