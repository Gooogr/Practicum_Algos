# https://contest.yandex.ru/contest/25596/problems/E/

from typing import List, Tuple

# Time O(target_sum * len(nominals))
# Space O(target_sum)
def read_input() -> Tuple[int, List[int]]:
    target_sum = int(input())
    _ =  input()
    nominals = list(map(int, input().split()))
    return target_sum, nominals

def get_min_count(target_sum: int, nominals: List[int]):
    # count minimal coins amount for money in range 0...target_sum
    dp = [1e9] * (target_sum + 1) 
    dp[0] = 0
    for sum in range(1, target_sum + 1):
        for coin in nominals:
            if sum - coin >= 0:
                # dp[i] = 1 + dp[i - coin] but min track count history!
                dp[sum] = min(dp[sum], 1 + dp[sum - coin])
    return dp[target_sum] if dp[target_sum] < 1e9 else -1

target_sum, nominals = read_input()
print(get_min_count(target_sum, nominals))


            
        