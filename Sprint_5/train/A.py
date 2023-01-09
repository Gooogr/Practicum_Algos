# https://contest.yandex.ru/contest/24809/problems/

# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, value, left=None, right=None):  
            self.value = value  
            self.right = right  
            self.left = left

# First solution
def solution(root) -> int:
    '''
    BFS max search
    '''
    queue = [root]
    max_value = float('-inf')

    while queue:
        node = queue.pop(0) #first out
        max_value = max(max_value, node.value)
        
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return max_value

# Second solution
def solution(root) -> int:
    '''
    DFS max search
    '''
    stack = [root]
    max_value = float('-inf')

    while stack:
        node = stack.pop() # last out
        max_value = max(max_value, node.value)

        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    return max_value





def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3

if __name__ == '__main__':
    test()