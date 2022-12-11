# https://contest.yandex.ru/contest/23638/problems/I/
# O(n) in best, O(n*logn) in worst solution with additional memory

from typing import List, Tuple

def top_k_freq_ids(ids: List[int], k:int):
    count_dict = {}
    freq_arr = [[] for _ in range(len(ids) + 1)]
    # Count all frequencies
    for item in ids:
        count_dict[item] = count_dict.get(item, 0) + 1
    # Store them in array, where freq is index
    for id, freq in count_dict.items():
        freq_arr[freq].append(id)

    # Collect top K elements with additional sort
    result = []
    for i in range(len(freq_arr) - 1, 0, -1):
        sublist = sorted(freq_arr[i])
        for id in sublist:
            result.append(id)
            if len(result) == k:
                return result

def read_input() -> Tuple[List[int], int]:
    _ = input()
    ids = list(map(int, input().strip().split()))
    k = int(input())
    return ids, k

print(*top_k_freq_ids(*read_input()))