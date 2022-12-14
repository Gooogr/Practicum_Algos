# https://contest.yandex.ru/contest/23991/problems/D/

def print_unique()-> None:
    n = int(input())
    unique_hobbies = set()
    for _ in range(n):
        hobbie = input().strip()
        if hobbie not in unique_hobbies:
            print(hobbie)
        unique_hobbies.add(hobbie)

print_unique()
