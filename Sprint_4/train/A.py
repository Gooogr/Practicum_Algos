# https://contest.yandex.ru/contest/23991/problems/A/

## Naive implementation
# def get_hash(a:int, m:int, s:str):
#     hash = 0
#     for idx, symbol in enumerate(s):
#         hash += ord(symbol)*(a**(len(s) - idx - 1))
#     return hash % m

# Horner’s Method
def get_hash(a:int, m:int, s:str):
    if not s:
        return 0
    string_hash = ord(s[0])
    for idx in range(1, len(s)):
        string_hash = string_hash*a + ord(s[idx])
        string_hash = string_hash % m
    return string_hash
    
def read_input():
    a = int(input())
    m = int(input())
    s = input().strip()
    return a, m, s

print(get_hash(*read_input()))