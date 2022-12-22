# https://contest.yandex.ru/contest/23991/problems/F/

from typing import List
from collections import defaultdict

def get_string_code(s: str):
    code_list = [0] * 26 
    for letter in s:
        ord_idx = ord(letter) - ord('a')
        code_list[ord_idx] += 1
    return str(code_list)


def group_anagrams(words: List[str]):
    anagram_dict = defaultdict(list)
    for idx in range(len(words)):
        word_code = get_string_code(words[idx])
        anagram_dict[word_code].append(idx)
    return sorted(anagram_dict.values())

def read_input():
    _ = input()
    words = input().split()
    return words

result = group_anagrams(read_input())
for item in result:
    print(*item, sep=' ')