# https://contest.yandex.ru/contest/24810/problems/A/

from typing import List, Tuple, Hashable
from dataclasses import dataclass    

class MaxHeap():
    def __init__(self):
        self.size = 0
        self.heap = [-1]

    def _sift_up(self, idx: int) -> None:
        '''
        Sift up selected heap index
        '''
        if idx > self.size + 1:
            raise IndexError('Sifted index is out of heap range')
        if idx == 1:
            return 
        parent_idx = idx // 2
        if self.heap[parent_idx] < self.heap[idx]:
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            return self._sift_up(parent_idx)  

    def _max_child(self, idx: int):
        '''
        Find max child index of the selected heap node.
        Return:
            If node hasn't any child - None
            If only left child - index of left child
            If both children exist - index of the bigger one 
        '''
        left_idx = idx * 2
        right_idx = idx * 2 +1

        # No childrens case
        if self.size < left_idx:
            return None 
        # Where self.size >= right_idx for making sure that both children exist
        if self.size >= right_idx and self.heap[left_idx] < self.heap[right_idx]:
            return right_idx
        else:
            return left_idx


    def _sift_down(self, idx: int) -> None:
        '''
        Sift down selected heap element
        '''
        while (idx * 2) <= self.size:
            idx_largest = self._max_child(idx)
            if self.heap[idx] < self.heap[idx_largest]:
                self.heap[idx_largest], self.heap[idx] = self.heap[idx], self.heap[idx_largest]
            idx = idx_largest
    
    def insert(self, x: int) -> None:
        '''
        Add new value to the heap
        '''
        self.heap.append(x)
        self.size += 1
        self._sift_up(self.size)

    def pop(self) -> Hashable:
        '''
        Remove root value from the heap and update tree
        '''
        if self.size < 1:
            raise ValueError("Can't remove element, heap is empty")
        max_value = self.heap[1]
        # Replace root by last added value and sift it down
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self._sift_down(1)
        return max_value
   
def read_input() -> List[Tuple[str, int, int]]:
    n = int(input())
    input_list = []
    for _ in range(n):
        login, number, penalty = list(input().strip().split())
        input_list.append((-int(number), int(penalty), login))
    return input_list

def heap_sort(x: List) -> List:
    heap = MaxHeap()
    sorted_result = []
    for item in x:
        heap.insert(item)
    while heap.size > 0:
        sorted_result.append(heap.pop())
    return sorted_result

result = heap_sort(read_input())
for competitor in result[::-1]:
    print(competitor[2])

