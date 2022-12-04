# https://contest.yandex.ru/contest/22779/problems/J/

from typing import List, Tuple

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.queue_size = 0

    def get(self):
        '''
        Print head element and delete it from queue
        '''
        if self.queue_size == 0:
            print('error')
        else:
            x = self.head.value
            print(x)
            
            self.head = self.head.next
            self.queue_size -= 1
            
            if self.head is None:
                self.tail = None

    def put(self, x):
        '''
        Add elemt to tail
        '''
        if self.tail is None:
            self.head = Node(x)
            self.tail = self.head 
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next  
        self.queue_size += 1

    def size(self):
        '''
        Print queue size
        '''
        print(self.queue_size)

def apply_commands(queue: LinkedListQueue, commands: List[str]):
    for step in commands:
        if step == 'get':
            queue.get()
        elif step == 'size':
            queue.size()
        elif 'put' in step:
            value = int(step.split(' ')[1])
            queue.put(value)
        else:
            raise ValueError('Incorrect commands', f'<{step}>')
    return queue

def read_input() -> Tuple[int, List[str]]:
    n = int(input())
    commands = []
    for _ in range(n):
        commands.append(str(input()))
    return commands

queue = LinkedListQueue()
apply_commands(queue, read_input())