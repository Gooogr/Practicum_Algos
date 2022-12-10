# https://contest.yandex.ru/contest/23638/problems/C/

from typing import Tuple

def compare_strings(substring: str, full_string: str)-> bool:
    position_idx = -1
    for symbol in substring:
        position_idx = full_string.find(symbol, position_idx + 1)
        if position_idx == -1:
            return False
    else:
        return True

def read_input() -> Tuple[str]:
    substring = input().strip()
    full_string = input().strip()
    return substring, full_string

print(compare_strings(*read_input()))