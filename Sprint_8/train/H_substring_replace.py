# https://contest.yandex.ru/contest/26131/problems/H/

text = input()
s = input()
t = input()

## Yes, we can use one-liner
# print(text.replace(s, t))

## But probably we were assumed to use something more low-level

def search(p: str, text:str):
    '''
    Reteurn all entering idices of the pattern p in text
    '''
    result = []
    s = p + '#' + text
    pi = [None] * len(p)
    pi[0] = 0
    pi_prev = 0
    for i in range(1, len(s)):
        k = pi_prev
        while k > 0 and s[k] != s[i]:
            k = pi[k - 1]
        if s[k] == s[i]:
            k += 1
        if i < len(p):
            pi[i] = k
        pi_prev = k
        if k == len(p):
            result.append( i - 2 * len(p))
    return result


input_idxs = search(s, text)

## insertion in for loop leads to TL error
# for idx in input_idxs[::-1]:
#     text = text[:idx] + t + text[idx + len(s):]
# print(text)

## print chanks like in task E
prev_idx = 0
for idx in input_idxs:
    print(text[prev_idx: idx], end='')
    print(t, end='')
    prev_idx = idx + len(s)
print(text[prev_idx:], end='')