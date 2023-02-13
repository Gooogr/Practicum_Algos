# https://contest.yandex.ru/contest/26133/problems/A/

from typing import List

def decode_string(s: str) -> str:
    stack = []
    for char in s:
        if char != ']':
            stack.append(char)
        else:
            substr = ''
            while stack and stack[-1] != '[':
                substr = stack.pop() + substr # invert order from stack
            stack.pop()                       # remove '['

            coef = ''
            while stack and stack[-1].isnumeric():
                coef = stack.pop() + coef
            stack.append(int(coef) * substr)
    return "".join(stack)

def read_input() -> List[str]:
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input().strip())
    return strings

def get_biggest_prefix(strings: List[str]):
    strings = [decode_string(string) for string in strings]
    strings = sorted(strings, key = lambda x: len(x)) # to get prefix string
    prefix = strings[0]
    for string in strings[1:]:
        # truncate prefix until match
        while prefix and string[:len(prefix)] != prefix:
            prefix = prefix[:-1] 
    return prefix
    
print(get_biggest_prefix(read_input()))





        

