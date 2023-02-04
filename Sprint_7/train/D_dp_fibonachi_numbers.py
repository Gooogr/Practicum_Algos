# https://contest.yandex.ru/contest/25596/problems/D/
# Methods comparing
# Simple recursion: 
# O(2^n) time, O(n) space. The size of space controls
# by call stack max size, it can't be more than N in any case.
# DP: 
# O(n) time, O(n) space

from typing import Dict


# Iterative witch cache
def get_fibo_number(x: int) -> int:
    fibs = [1, 1]
    for _ in range(2, x + 1):
        fibs.append((fibs[-1] + fibs[-2]) % (1e9 + 7))
    return fibs[x]

# Recursive with cache. It's also DP!
def get_fibo_number(x: int, cache: Dict[int,int] = {}) -> int:
    if x < 2:
        return 1
    if x in cache:
        return cache[x]
    cache[x] = (get_fibo_number(x - 1, cache) + get_fibo_number(x - 2, cache)) % (1e9 + 7)
    return  cache[x]

x = int(input())
print(int(get_fibo_number(x)))