# O(n**2)
# Stable sort

from typing import List

def insertion_sort(array: List[int]):
    for i in range(1, len(array)):
        # save our insertable element
        item_to_insert = array[i]
        j = i
        # shift elements to the left step-by-step until until the element to 
        # the right of the free space is strictly larger than our variable
        while j > 0 and item_to_insert < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        # insert saved element
        array[j] = item_to_insert
        print(f'step {i}, sorted {i+1} elements: {array}') 
    return array

result = insertion_sort([11, 2, 9, 7, 1])
print('Final result:', result)

# Input:                     [11, 2, 9, 7, 1] 
# step 1, sorted 2 elements: [2, 11, 9, 7, 1]
# step 2, sorted 3 elements: [2, 9, 11, 7, 1]
# step 3, sorted 4 elements: [2, 7, 9, 11, 1]
# step 4, sorted 5 elements: [1, 2, 7, 9, 11]
# Final result:              [1, 2, 7, 9, 11]