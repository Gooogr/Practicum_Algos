# https://contest.yandex.ru/contest/24810/problems/A/

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

    def _max_child(self, idx):
        '''
        Find max child index of selected heap node.
        Return:
            If node hasn't any child - None
            If only left child - index of left child
            If both children exist - index of the bigger one 
        '''
        left_idx = idx * 2
        right_idx = idx * 2 +1

        if self.size < left_idx:
            return None 
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
        self.heap.append(x)
        self.size += 1
        self._sift_up(self.size)

    def pop(self) -> int:
        pass
        # if self.size < 2:
        #     raise ValueError("Can't remove element, heap is empty")


min_heap = MaxHeap()
min_heap.insert(10)
min_heap.insert(20)
min_heap.insert(30)
min_heap.insert(-100)

print(min_heap.heap)
