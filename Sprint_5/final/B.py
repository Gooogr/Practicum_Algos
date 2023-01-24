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

def get_tree_max(root: Optional[Node]):
	if not root:
		return None
	while root.right:
		root = root.right
	return root

def printBinaryTree(root, space, height):
	# https://www.techiedelight.com/print-two-dimensional-view-binary-tree/
    # Base case
    if root is None:
        return
    # Increase distance between levels
    space += height
    # Print right child first
    printBinaryTree(root.right, space, height)
    print()
    # Print the current node after padding with spaces
    for i in range(height, space):
        print(' ', end='')
    print(root.value, end='')
    # Print left child
    print()
    printBinaryTree(root.left, space, height)

# Iterative approach
def remove(root: Optional[Node], key: int) -> Optional[Node]:
	if not root:
		return None

	# Stage1: track D node and its parent by key
	pd_node = None
	d_node = root

	# Iterate over tree
	while d_node and d_node.value != key:
		pd_node = d_node
		if d_node.value > key:
			d_node = d_node.left
		else:
			d_node = d_node.right
	
	# If we failed to find target node - return root
	if not d_node:
		return root

	# Stage 2: replace D node 
	# Simple case - D node is leaf or one-node tree
	if d_node.left is None and d_node.right is None:
		# Leaf case - delete link with parent
		if d_node != root:
			if pd_node.left == d_node:
				pd_node.left = None
			else:
				pd_node.right = None
		# One-node tree - now it's empty
		else:
			root = None
	# Two children case - find P node and replace D node
	elif d_node.left and d_node.right:
		p_node = get_tree_max(d_node.left)
		p_node_value = p_node.value
		remove(root, p_node.value)
		d_node.value = p_node_value
	# One child case
	else:
		if d_node.left is None:
			p_node = d_node.right
		else:
			p_node = d_node.left

		# If D node isn't root - update D parent link
		if d_node != root:
			if pd_node.left == d_node:
				pd_node.left = p_node
			else:
				pd_node.right = p_node
		# If D node is root - replace node by child
		else:
			root = p_node
	return root

def test():
	# Build in test
	node1 = Node(None, None, 2)
	node2 = Node(node1, None, 3)
	node3 = Node(None, node2, 1)
	node4 = Node(None, None, 6)
	node5 = Node(node4, None, 8)
	node6 = Node(node5, None, 10)
	node7 = Node(node3, node6, 5)
	print('Original')
	printBinaryTree(node7, 0, 5)
	newHead = remove(node7, 10)
	print('Altered')
	printBinaryTree(newHead, 0, 5)
	assert newHead.value == 5, newHead.value
	assert newHead.right is node5
	assert newHead.right.value == 8
	print('----------------------')

	# Additional test
	node7 = Node(None, None, 7)
	node6 = Node(None, None, 5)
	node5 = Node(None, None, 3) 
	node4 = Node(None, None, 1)
	node3 = Node(node6, node7, 6)  
	node2 = Node(node4, node5, 2)
	node1 = Node(node2, node3, 4)
	print('Original')
	printBinaryTree(node1, 0, 5)
	new_head = remove(node1, 4)
	print('Altered')
	printBinaryTree(new_head, 0, 5)
	assert new_head.value == 3, new_head.value
	print('----------------------')

	node10 = Node(None, None, 99)
	node9 = Node(None, None, 72)
	node8 = Node(node9, node10, 91)
	node7 = Node(None, None, 50)
	node6 = Node(None, None, 32)
	node5 = Node(None, node6, 29)
	node4 = Node(None, None, 11)
	node3 = Node(node7, node8, 65)
	node2 = Node(node4, node5, 20)
	node1 = Node(node2, node3, 41)
	print('Original')
	printBinaryTree(node1, 0, 5)
	new_head = remove(node1, 41)
	print('Altered')
	printBinaryTree(new_head, 0, 5)

if __name__ == '__main__':
    test()