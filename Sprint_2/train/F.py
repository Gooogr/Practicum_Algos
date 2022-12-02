# https://contest.yandex.ru/contest/22779/problems/F/

from typing import List

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        '''
        Add value to stack
        '''
        self.items.append(value)

    def pop(self):
        '''
        Delete value from the top of stack
        '''
        if self.items:
            self.items.pop()
        else:
            print('error')

    def get_max(self):
        '''
        Print max value in stack
        '''
        if self.items:
            print(max(self.items))
        else:
            print('None')

def apply_commands(stack: Stack, commands: List[str]):
    for step in commands:
        if step == 'get_max':
            stack.get_max()
        elif step == 'pop':
            stack.pop()
        else:
            value = int(step.split(' ')[1])
            stack.push(value)
    return stack


def read_input() -> List[str]:
    n = int(input())
    commands = []
    for _ in range(n):
        commands.append(str(input()))
    return commands

stack = Stack()
stack = apply_commands(stack, read_input())