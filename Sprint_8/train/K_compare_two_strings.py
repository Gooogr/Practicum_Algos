# https://contest.yandex.ru/contest/26131/problems/K/

def is_equal(s1:str, s2:str) -> int:
    s1_clean = ''
    s2_clean = ''
    for item in s1:
        if not ord(item) % 2:
            s1_clean += item
    for item in s2:
        if not ord(item) % 2:
            s2_clean += item

    if s1_clean > s2_clean: return 1
    if s1_clean < s2_clean: return -1
    else: return 0
        
s1 = input().strip()
s2 = input().strip()
print(is_equal(s1, s2))

# Try to solve inplace
# def is_equal(s1: str, s2:str):
#     i, j = 0, 0
#     while i < len(s1) or j < len(s2):
#         # if both symbols have even alphabet positions
#         if not ord(s1[i]) % 2 and not ord(s2[j]) % 2: 
#             if s1[i] < s2[j]:
#                 return -1
#             if s1[i] > s2[j]:
#                 return 1
#             i += 1
#             j += 1
#         else:
#             if i < len(s1) - 1 and ord(s1[i]) % 2:
#                 i += 1
#             if j < len(s2) - 1 and ord(s2[i]) % 2:
#                 j += 1
#     return 0