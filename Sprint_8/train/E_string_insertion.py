# https://contest.yandex.ru/contest/26131/problems/E/

from typing import List, Tuple

def get_input():
    source = input().strip()
    n = int(input())
    subs = []
    for _ in range(n):
        substr, idx = input().split()
        subs.append(tuple([substr, int(idx)]))
    return source, subs

# Too slow! Time complexity O(n^2)
# Better way - direct print. Check next function
def insert_subs(source, subs):
    subs = sorted(subs, key=lambda x: x[1], reverse=True)
    result = list(source) 
    for substr, idx in subs:
        result.insert(idx, substr)
    print(''.join(result))
# insert_subs(*get_input())

# Direct print without any insertions - OK
# Time complexity O(n)
def insert_subs(source, subs):
    subs = {idx: substr for substr, idx in subs}
    source = '_' + source # to simplify indexing
    for idx, symbol in enumerate(source):
        if idx == 0 and idx in subs:
            print(subs[0], end='')
        if idx != 0:
            print(symbol, end='')
            print(subs.get(idx, ''), end='')
insert_subs(*get_input())