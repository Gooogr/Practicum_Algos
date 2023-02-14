# https://contest.yandex.ru/contest/26133/problems/B/ 
# 

from typing import List, Tuple

class TrieNode:
    def __init__(self, char: str):
        self.char = char
        self.children = dict() # keys are chars, values are TrieNodes
        self.terminal = False
        self.size = None       # len of word in terminal node

class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word:str):
        node = self.root
        for char in word:
            # if char in children - traverse to child
            if char in node.children:
                node = node.children[char]
            # else - create new child and then traverse
            else:
                node.children[char] = TrieNode(char)
                node = node.children[char]
        node.terminal = True
        node.size = len(word)

def read_input() -> Tuple[str, List[str]]:
    s = input()
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())
    return s, words
    
