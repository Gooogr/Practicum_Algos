# https://contest.yandex.ru/contest/25596/problems/G/

from typing import List, Tuple

def get_input():
    target_sum = int(input())
    _ = input()
    coin_nominals = list(map(int, input().split()))
    return target_sum, coin_nominals

def count_ways(target_sum, coin_nominals):

    # number of ways to get sum in range 0...target_sum
    dp = [0] * (target_sum + 1)
    dp[0] = 1

    for i in range(len(coin_nominals)):  # use part of coin list limit by index
        for j in range(coin_nominals[i], len(dp)):
            # dp[j] - ways to get this sum 
            # dp[j - coins[i]] - ways to get previous sum without coins[i]
            dp[j] += dp[j - coin_nominals[i]]
    return dp[-1]

print(count_ways(*get_input()))

