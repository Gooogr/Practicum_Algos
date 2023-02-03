# https://contest.yandex.ru/contest/25596/problems/D/

# Iterative witch cache
def get_fibo_number(x: int) -> int:
    fibs = [1, 1]
    for _ in range(2, x + 1):
        fibs.append((fibs[-1] + fibs[-2]) % (1e9 + 7))
    return fibs[x]

x = int(input())
print(int(get_fibo_number(x)))