# https://contest.yandex.ru/contest/26131/problems/B/

def can_cross_border(s1: str, s2: str) -> bool:
    # Equal strings case
    if s1 == s2:
        return True
    # Too different strings case
    if abs(len(s1) - len(s2)) > 1:
        return False
    i, j = 0, 0
    counter = 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            counter += 1
            if counter > 1:
                return False
            if len(s1) > len(s2): # 'abc' vs 'bc' -> jump to next symbol in 'abc'
                i += 1
            elif len(s1) < len(s2):
                j += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1
    return True

s1 = input().strip()
s2 = input().strip()

print("OK" if can_cross_border(s1, s2) else "FAIL")
