# https://contest.yandex.ru/contest/24809/problems/L/
# Sift down works fine for final task, output index is shit

def max_child(heap, idx):
        left_idx = idx * 2
        right_idx = idx * 2 +1
        size = len(heap) - 1

        if size < left_idx:
            return None 
        if size >= right_idx and heap[left_idx] < heap[right_idx]:
            return right_idx
        else:
            return left_idx

# Correct sift for heap, but errors in index output
def sift_down(heap, idx: int) -> None:
    result_idx = 1
    while (idx * 2) <= len(heap) - 1:
        idx_largest = max_child(heap, idx)
        if heap[idx] < heap[idx_largest]:
            heap[idx_largest], heap[idx] = heap[idx], heap[idx_largest]
            result_idx = idx_largest # save it for output
        idx = idx_largest
    return result_idx

             
def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5, sift_down(sample, 2)

if __name__ == '__main__':
    test()