# https://contest.yandex.ru/contest/25596/problems/L/

from typing import List, Tuple

def get_input() -> Tuple[int, List[int]]:
    _, weight_limit = map(int, input().split())
    items_weights = list(map(int, input().split()))
    return weight_limit, items_weights

def get_max_weight(weight_limit, items_weights):
    dp = [0] * (weight_limit + 1)
    for i in range(len(items_weights)):
        for j in range(weight_limit, items_weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - items_weights[i]] + items_weights[i])

    return(dp[-1])

print(get_max_weight(*get_input()))