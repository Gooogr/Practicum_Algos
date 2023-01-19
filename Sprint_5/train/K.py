# https://contest.yandex.ru/contest/24809/problems/K

# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, left=None, right=None, value=0):  
            self.right = right
            self.left = left
            self.value = value

def print_range(node, r_min, r_max):
    # Base case
    if node is None:
        return
    # Recursive LNR traversal
    if node.value >= r_min: # search smaller numbers
        print_range(node.left, r_min, r_max)
    
    if r_min <= node.value <= r_max:
        print(node.value, end=' ')

    if node.value <= r_max: # search bigger numbers
        print_range(node.right, r_min, r_max)

def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    print_range(node7, 2, 8)
    # expected output: 2 5 8 8

if __name__ == '__main__':
    test()