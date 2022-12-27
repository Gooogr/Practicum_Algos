# https://contest.yandex.ru/contest/24414/problems/B/

'''
--Описание решения--
https://all-num.com/ru/prime/0-999999/100000-104999.html
--Доказательство корректности--
--Временная сложность--
--Пространственная сложность--
'''
from typing import List, Tuple, Union

TABLE_CAPACITY = 100003 # The samllest prime number > 1e5

class Node:
    def __init__(self, key: int, value: int, next=None) -> None:
        self.key = key
        self.value = value
        self.next = next

class Hash_table:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity

    def __hash__(self, key: int) -> int:
        '''
        Compute hash for int values
        '''
        return key % self.capacity
    
    def put(self, key, value):
        pass

    def get(self, key):
        pass

    def delete(self, key):
        pass


###----------------------------- Helper functions --------------------------###
def read_input() -> List[str]:
    n = int(input())
    commands = []
    for _ in range(n):
        commands.append(str(input()))
    return commands

def apply_commands(hash_table: Hash_table, commands: List[str]):
    for step in commands:
        *step,  = step.split() # flexible unpacking
        if step[0] == 'get':
            hash_table.get(step[1])
        elif step[0] == 'put':
            hash_table.put(step[1], step[2])
        elif step[0] == 'delete':
            hash_table.delete(step[1])
        else:
            raise ValueError('Incorrect command')

###--------------------------------- Main run ------------------------------###

hash_table = Hash_table(TABLE_CAPACITY)
commands = read_input()
apply_commands(hash_table, commands)
