# https://contest.yandex.ru/contest/23638/problems/B/

results = []
symbols_keys = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

def generate_string(numbers: str, line: str):
    if not numbers:
        results.append(line)
        return
    for letter in symbols_keys[numbers[0]]:
        generate_string(numbers[1:], line + letter)

generate_string(input().strip(), '')
print(*results)


    