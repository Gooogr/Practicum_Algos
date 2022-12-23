# https://contest.yandex.ru/contest/23991/problems/B/

import random
import string
random.seed(42)

base = 1000
tablesize = 123987123


def get_hash(a:int, m:int, s:str):
    string_hash = ord(s[0])
    for idx in range(1, len(s)):
        string_hash = string_hash*a + ord(s[idx])
    return string_hash % m

letters = string.ascii_lowercase
map = {}

hash_counter = 0 # just for cuiriosity
while True:
    str = ''.join(random.choice(letters) for i in range(20))
    hash = get_hash(base, tablesize, str)
    if hash in map:
        print('Hash:', hash)
        print('First string:', str)
        print('Second string:', map[hash])
        print('Total hashes generated:', hash_counter + 1)
        break
    else:
        map[hash] = str
        hash_counter += 1