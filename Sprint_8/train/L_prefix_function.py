# https://contest.yandex.ru/contest/26131/problems/L/

# Calculate prefix function for string s

# Time complexity O(n^3)
def naive_appoach(s: str):
    N = len(s)
    pi = [0] * N
    for i in range(1, N+1):
        # i - length of substring-prefix
        substring = s[:i]
        # check overlaping
        for k in range(i - 1, -1, -1): 
            prefix = substring[:k]
            suffix = substring[i - k:i]
            if prefix == suffix:
                pi[i - 1] = k
                break # stop, because we move from max to min
    return pi

# Time complexity O(n)
def dp_approach():
    pass


s = input().strip()
print(*naive_appoach(s))