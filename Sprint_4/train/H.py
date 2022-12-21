# https://contest.yandex.ru/contest/23991/problems/H/

def compare_strings(s1: str, s2:str):
    if len(s1) != len(s2):
        return 'NO'
    # Link s1 with s2 symbols
    string_hash = {}
    for idx in range(len(s1)):
        # if s1-s2 link is already exist
        if s1[idx] in string_hash:
            # and new one is differ from existed
            if string_hash[s1[idx]] != s2[idx]:
                return 'NO'
        else:
            string_hash[s1[idx]] = s2[idx]
    # Handle cases 'aba' ~ 'xxx
    if len(string_hash) == len(set(s2)):
        return 'YES'
    else:
        return 'NO'


def get_input():
    s1 = input().strip()
    s2 = input().strip()
    return s1, s2

print(compare_strings(*get_input()))