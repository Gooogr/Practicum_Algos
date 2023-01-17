# https://contest.yandex.ru/contest/24809/problems/B/
# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

from typing import Optional

LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, value, left=None, right=None):  
            self.value = value  
            self.right = right  
            self.left = left


def solution(root: Optional[Node]) -> bool:
    is_balanced = True

    def dfs(node: Optional[Node]):
        if not node: 
            return 0

        height_left, height_right = dfs(node.left), dfs(node.right)

        nonlocal is_balanced
        if abs(height_left - height_right) > 1:
            is_balanced = False

        return 1 + max(height_left, height_right)
    
    dfs(root)
    return is_balanced

def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == '__main__':
    test()