# https://contest.yandex.ru/contest/24810/problems/A/

class MinHeap():
    def __init__(self):
        self.size = 0
        self.heap = [-1]

    def _sift_up(self, idx: int) -> None:
        if idx > self.size + 1:
            raise IndexError('Sifted index is out of heap range')
        if idx == 1:
            return 
        parent_idx = idx // 2
        if self.heap[parent_idx] < self.heap[idx]:
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            return self._sift_up(parent_idx)  

    def _sift_down(self, idx: int) -> None:
        pass
    
    def insert(self, x: int) -> None:
        pass

    def pop(self) -> int:
        pass

min_heap = MinHeap()
min_heap._sift_up(100)
print(min_heap.heap)