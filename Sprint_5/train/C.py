# https://contest.yandex.ru/contest/24809/problems/C/
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

def check_symmetry(left_node: Optional[Node], right_node: Optional[Node]):
    if (left_node is None) and (right_node is None):
        return True

    if (left_node is None) and (right_node is not None):
        return False

    if (left_node is not None) and (right_node is None):
        return False

    return (left_node.value == right_node.value and 
            check_symmetry(left_node.left, right_node.right) and
            check_symmetry(left_node.right, right_node.left)) 
    

def solution(root: Optional[Node]) -> bool:
    return check_symmetry(root.left, root.right)

 
def test():
    node1 = Node(3,  None,  None)
    node2 = Node(4,  None,  None)
    node3 = Node(4,  None,  None)
    node4 = Node(3,  None,  None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert solution(node7)

if __name__ == '__main__':
    test()