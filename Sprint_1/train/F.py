def is_palindrome(line: str) -> bool:
    # Здесь реализация вашего решения
    l, r = 0, len(line) - 1
    while l < r:
        if not line[l].isalnum():
            l += 1
        elif not line[r].isalnum():
            r -= 1
        elif line[l].lower() != line[r].lower():
            return False
        else:
            l += 1
            r -= 1
    return True


print(is_palindrome(input().strip()))