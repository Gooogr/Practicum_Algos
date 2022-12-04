# https://contest.yandex.ru/contest/22779/problems/I/

from typing import List, Tuple

class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.queue_size = 0
    
    def pop(self):
        '''
        Delete head element and print it
        '''
        if self.queue_size == 0:
            print('None')
        else:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_n
            self.queue_size -= 1
            print(x)

    def peek(self):
        '''
        Print head element
        '''
        if self.queue_size == 0:
            print('None')
        else:
            print(self.queue[self.head])

    def size(self):
        '''
        Print size of queue
        '''
        print(self.queue_size)

    def push(self, x):
        '''
        Add new element to tail
        '''
        if self.queue_size < self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.queue_size += 1
        else:
            print('error')

def apply_commands(queue: MyQueueSized, commands: List[str]):
    for step in commands:
        if step == 'pop':
            queue.pop()
        elif step == 'peek':
            queue.peek()
        elif step == 'size':
            queue.size()
        elif step == 'push':
            value = int(step.split(' ')[1])
            queue.push(value)
        else:
            raise ValueError('Incorrect command')
    return queue

def read_input() -> Tuple[int, List[str]]:
    n = int(input())
    max_size = int(input())

    commands = []
    for _ in range(n):
        commands.append(str(input()))
    return max_size, commands

max_size, commands = read_input()
queue = MyQueueSized(max_size)
queue = apply_commands(queue, commands)