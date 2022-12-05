# https://contest.yandex.ru/contest/22781/problems/A/

from typing import List, Tuple

class DeckSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.queue_size = 0
    
    def push_back(self, x):
        '''
        Add new element to the tail of deck
        '''
        if self.queue_size < self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.queue_size += 1
        else:
            print('error')

    def push_front(self, x):
        pass

    def pop_front(self):
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

    def pop_back(self):
        '''
        Delete tail element and print it
        '''

###----------------------------- Helper functions --------------------------###
def read_input() -> Tuple[int, List[str]]:
    n = int(input())
    max_size = int(input())

    commands = []
    for _ in range(n):
        commands.append(str(input()))
    return max_size, commands

def apply_commands(deck: DeckSized, commands: List[str]):
    for step in commands:
        *step,  = step.split() # flexible unpacking
        if step[0] == 'push_back':
            deck.push_back(step[1])
        elif step[0] == 'push_front':
            deck.push_front(step[1])
        elif step[0] == 'pop_front':
            deck.pop_front()
        elif step[0] == 'pop_back':
            deck.pop_back()
        else:
            raise ValueError('Incorrect command')
        # TURN OFF PRINTS BEFORE SUBMIT
        print()
        print('-----------------')
        print('Get command:', step)
        print('Current deck state:', deck.queue)
        print('-----------------')
    return deck

###------------------------------- Run steps -------------------------------###
max_size, commands = read_input()
deck = DeckSized(max_size)
apply_commands(deck, commands)