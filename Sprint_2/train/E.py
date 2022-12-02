# https://contest.yandex.ru/contest/22779/problems/E/

# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class DoubleConnectedNode:  
        def __init__(self, value, next=None, prev=None):  
            self.value = value  
            self.next = next  
            self.prev = prev

def solution(head):
    # Your code
    # Empty or one-cell lists
    if head is None or head.next is None:
        return head

    tmp, curr = None, head
    while curr:
        # save original prev pointer
        tmp = curr.prev 
        # change direction
        curr.prev = curr.next 
        curr.next = tmp  
        # get to the next cell
        curr = curr.prev     
    return tmp.prev

def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    new_head = solution(node0)
    assert new_head is node3, new_head
    assert node3.next is node2, node3.next.value
    assert node2.next is node1, node2.next.value 
    assert node2.prev is node3, node2.prev.value
    assert node1.next is node0, node1.next.value 
    assert node1.prev is node2, node1.prev.value
    assert node0.prev is node1, node0.prev.value

if __name__ == '__main__':
    test()