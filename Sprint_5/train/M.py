# https://contest.yandex.ru/contest/24809/problems/M/

# Iterative
def sift_up(heap, idx) -> int:
    if idx == 1:
        return idx
    parent_idx = idx // 2
    while heap[parent_idx] < heap[idx] and idx > 1:
        heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
        idx = parent_idx
        parent_idx = idx // 2   
    return idx

# Recursive
def sift_up(heap, idx) -> int:
    if idx == 1:
        return idx
    parent_idx = idx // 2
    if heap[parent_idx] < heap[idx]:
        heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
        return sift_up(heap, parent_idx)  
    return idx
            
def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1, sift_up(sample, 5)

if __name__ == '__main__':
    test()