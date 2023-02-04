# https://contest.yandex.ru/contest/25596/problems/F/

ladder_size, max_steps = map(int, input().split())

# # DP with recursion. Valid, but leads to stack overflow error
# # Need to rewrite as iterative
# def total_ways(ladder_size: int, max_steps: int, cache:dict={}):
#     # If ladder_size - curret_step < 0
#     if ladder_size < 0:
#         return 0
#     # Base case
#     if ladder_size < 2:
#         return 1

#     # Get pre-calculated value
#     if ladder_size in cache:
#         return cache[ladder_size]

#     # Call recursion for calculation
#     # F[n] = F[n - 1] + ... + F[n - max_steps]
#     count = 0
#     for i in range(1, max_steps + 1):
#         count += total_ways(ladder_size - i, max_steps, cache)
#         count %= (1e9 + 7)
#     cache[ladder_size] = int(count)
 
#     return cache[ladder_size]

# DP with iterative approach
def total_ways(ladder_size: int, max_steps: int):
    # If ladder_size - curret_step < 0
    if ladder_size < 0:
        return 0
    # Base case
    if ladder_size < 2:
        return 1

    dp = [1, 1] # size 0 and 1
    for size in range(2, ladder_size + 1):
        # NB: direct sum() in non-optimal for every iteration
        # but get OK anyway
        dp.append(sum(dp[-max_steps:]) % (1e9 + 7)) 

    return int(dp[-1])

# -1 because every participant start from the first point
print(total_ways(ladder_size - 1, max_steps)) 




