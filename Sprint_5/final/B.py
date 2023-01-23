# https://contest.yandex.ru/contest/24810/problems/B/

# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

from typing import Optional

LOCAL = True
if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value

def find_node_with_parent_by_value(root: Node, val: int):
    '''
    Search node and its parent by node value
    '''
    if not root:
        return None

    # Base case
    left_child = root.left
    right_child = root.right
    if left_child and left_child.value == val:
        return left_child, root
    if right_child and right_child.value == val:
        return right_child, root

    # Recursion case
    if root.value > val:
        return find_node_with_parent_by_value(root.left, val)
    else:
        return find_node_with_parent_by_value(root.right, val)

def get_right_corner_node(root: Node):
    '''
    Return the most right node is selected tree.
    Use iterative BFS with level size tracking
    '''
    # Empty tree
    if not root:
        return None
    # One-node tree
    if not root.right:
        return None

    queue = [root]
    most_right_node = None

    while queue:
        level_size = len(queue)
        right_node = queue[level_size - 1]
        # Get the most right node on the level
        if right_node:
            most_right_node = right_node
        else:
            break
        # Collect next level nodes
        for _ in range(level_size):
            node = queue.pop(0)
            queue.append(node.left)
            queue.append(node.right)
    return most_right_node



def remove(root, key) -> Optional[Node]:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    pass


def test():

    root = Node(value=15)
    root.left = Node(value=10)
    root.right = Node(value=20)
    root.left.left = Node(value=8)
    root.left.right = Node(value=12)
    root.right.left = Node(value=16)
    root.right.right = Node(value=25)

    # print(get_right_corner_node(root).value)

    nodes = find_node_with_parent_by_value(root, 16)
    print(nodes[0].value, nodes[1].value)


    # node1 = Node(None, None, 2)
    # node2 = Node(node1, None, 3)
    # node3 = Node(None, node2, 1)
    # node4 = Node(None, None, 6)
    # node5 = Node(node4, None, 8)
    # node6 = Node(node5, None, 10)
    # node7 = Node(node3, node6, 5)

    # newHead = remove(node7, 10)
    # assert newHead.value == 5
    # assert newHead.right is node5
    # assert newHead.right.value == 8


if __name__ == '__main__':
    test()