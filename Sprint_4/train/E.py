# https://contest.yandex.ru/contest/23991/problems/E/

# Naive solution with list->set transformation, which is O(n)
def measure_max_unique_substring_length(s: str):
    substring = []
    max_size = 0
    for symbol in s:
        substring.append(symbol)
        while len(substring) != len(set(substring)):
            substring = substring[1:]
        max_size = max(max_size, len(substring))
    return max_size

# Better approach without transformation overhead
def measure_max_unique_substring_length(s: str):
    l = 0
    max_size = 0
    substring_hash = set()
    for r in range(len(s)):
        # truncate string from left until in became unique again
        while s[r] in substring_hash:
            substring_hash.remove(s[l])
            l += 1
        # add new unique symbol from right to hash
        substring_hash.add(s[r])
        max_size = max(max_size, len(substring_hash))
    return max_size

print(measure_max_unique_substring_length(input().strip()))




