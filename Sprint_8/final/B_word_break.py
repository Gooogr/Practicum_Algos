# https://contest.yandex.ru/contest/26133/problems/B/ 
# https://contest.yandex.ru/contest/26133/run-report/82354911/

from typing import List, Tuple

class TrieNode:
    def __init__(self, char: str):
        self.char = char
        self.children = dict() # keys are chars, values are TrieNodes
        self.terminal = False


def read_input() -> Tuple[str, List[str]]:
    s = input()
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())
    return s, words


def create_trie(words: List[str]):
    root = TrieNode("")
    for word in words:
        node = root            # every new word starts from root
        for char in word:
            # traverse trough existed chars
            if char in node.children:
                node = node.children[char]
            # add new nodes and traverse trough new path
            else:
                node.children[char] = TrieNode(char)
                node = node.children[char]
            # add terminal node info
        node.terminal = True
    return root


def can_split(s: str, trie: TrieNode) -> bool:
    dp = [False] * (len(s) + 1)
    # Base case. Empty string
    dp[0] = True
    for i in range(len(s)):
        node = trie
        # if we could get to this substring point
        if dp[i]:                  
            # collect info about other point where we can get from this one
            for j in range(i, len(s) + 1):
                if node.terminal:
                    dp[j] = True
                # return to root of trie if we met end of branch
                if j == len(s) or s[j] not in node.children:
                    break
                node = node.children[s[j]]
    return dp[-1]


s, words = read_input()
trie = create_trie(words)
print('YES' if can_split(s, trie) else 'NO')

    
