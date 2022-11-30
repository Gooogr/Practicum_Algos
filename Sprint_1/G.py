def to_binary(number: int) -> str:
    # Здесь реализация вашего решения
    if number==0: return ''
    else:
        return to_binary(number//2) + str(number%2)

def read_input() -> int:
    return int(input().strip())

result = to_binary(read_input()) 
if not result: #edge case with empty output
    result = '0'
print(result)