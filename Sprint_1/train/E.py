def get_longest_word(line: str) -> str:
    # Здесь реализация вашего решения
    max_item = ''
    for item in line.split():
        if len(item) > len(max_item):
            max_item = item
    return max_item

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))