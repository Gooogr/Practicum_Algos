# https://contest.yandex.ru/contest/22779/problems/K/

def find_fibo(n: int):
    if n <= 1:
        return 1
    else: 
        return find_fibo(n - 1) + find_fibo(n - 2)

print(find_fibo(int(input())))
