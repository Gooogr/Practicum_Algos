# https://contest.yandex.ru/contest/22779/problems/H/

def is_correct_bracket_seq(line: str):
    bracket_hash = {')':'(', ']':'[', '}':'{'}
    bracket_stack = []
    for item in line:
        if bracket_stack and item in bracket_hash:
            if bracket_hash[item] == bracket_stack[-1]:
                bracket_stack.pop()
            else:
                return False
        else:
            bracket_stack.append(item)
    return bracket_stack == []

print(is_correct_bracket_seq(input().strip()))