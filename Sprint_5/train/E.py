# https://contest.yandex.ru/contest/24809/problems/E/

# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, value, left=None, right=None):  
            self.value = value  
            self.right = right  
            self.left = left


def solution(root) -> bool:
    # DFS search
    stack = [root]
    # Track left and right borders for earch node
    llimit = [float('-inf')]
    rlimit = [float('inf')]
    while stack:
        node = stack.pop()
        left = llimit.pop()
        right = rlimit.pop()

        # print(f'Node value: {node.value}, limits: ({left, right})')
        if not left < node.value < right:
            return False

        if node.left is not None:
            stack.append(node.left)
            rlimit.append(node.value)
            llimit.append(left)

        if node.right is not None:
            stack.append(node.right)
            rlimit.append(right)
            llimit.append(node.value)
    return True


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)
    
    assert solution(node5)
    node2.value = 5
    assert not solution(node5)

if __name__ == '__main__':
    test()