# https://contest.yandex.ru/contest/24414/problems/B/

'''
--Описание решения--
https://all-num.com/ru/prime/0-999999/100000-104999.html
--Доказательство корректности--
--Временная сложность--
--Пространственная сложность--
'''
from typing import List, Optional

TABLE_CAPACITY = 999983 

class Node:
    def __init__(self, key: int, value: int, next=None) -> None:
        self.key = key
        self.value = value
        self.next = next

class Hash_table:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.size = 0  # track it it to simplify debug
        self.buckets = [None] * self.capacity

    def _get_bucket(self, key: int) -> int:
        '''
        Compute hash backet for int value
        '''
        return key % self.capacity
    
    def put(self, key: int, value: int) -> None:
        '''
        Add or update key-value pair
        '''
        bucket_idx = self._get_bucket(key)
        node = self.buckets[bucket_idx]
        # If bucket is empty - just add new node
        if node is None:
            self.buckets[bucket_idx] = Node(key, value)
            self.size += 1
            return None
        else:
            # Check if we already have this key and update value
            while node is not None:
                node_key = node.key
                if node_key == key:
                    node.value = value
                    return None
            # Add new key-value pair to the head
            new_head =  Node(key, value)
            new_head.next = self.buckets[bucket_idx]
            self.buckets[bucket_idx] = new_head
            self.size += 1
            
    def get(self, key: int) -> Optional[int]:
        '''
        Find value by key
        '''
        bucket_idx = self._get_bucket(key)
        node = self.buckets[bucket_idx]
        # If hash table doesn't have target key
        if node is None:
            return None
        # Track and return target key value
        while node is not None:
            node_key = node.key
            if node_key == key:
                return node.value
        # If target key not in linked list
        return None
                
    def delete(self, key: int) -> Optional[int]:
        '''
        Remove key-value pair
        '''
        bucket_idx = self._get_bucket(key)
        node = self.buckets[bucket_idx]
        # If hash table doesn't have target key
        if node is None:
            return None
        # If target key in head of list
        if node is not None and node.key == key:
            old_value = node.value
            new_head = node.next
            self.buckets[bucket_idx] = new_head
            self.size -= 1
            return old_value
        # Try to find target key in list beyond head
        temp_node = self.buckets[bucket_idx]
        while temp_node is not None:
            if temp_node.key == key:
                break
            prev_node = temp_node
            temp_node = temp_node.next
        # If we find tartget key - delete node
        if temp_node is not None:
            old_value = temp_node.value
            prev_node.next = temp_node.next
            self.size -= 1
            return old_value
        # If target key not in linked list
        return None
        

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
        if step[0] == 'put':
            hash_table.put(int(step[1]), int(step[2]))
        elif step[0] == 'get':
            result = hash_table.get(int(step[1]))
            if result is None:
                print(None)
            else:
                print(result)
        elif step[0] == 'delete':
            result = hash_table.delete(int(step[1]))
            if result is None:
                print(None)
            else:
                print(result)
        else:
            raise ValueError('Incorrect command')

###--------------------------------- Main run ------------------------------###

hash_table = Hash_table(TABLE_CAPACITY)
commands = read_input()
apply_commands(hash_table, commands)

## COMMENT BEFORE SUBMIT
# print('Final hash table size:', hash_table.size)
