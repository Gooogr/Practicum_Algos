# O(n*log(n))
# Stable

from typing import List

def mergesort(arr):
	if len(arr) < 2:
		return arr
	else:
		n = len(arr)//2
		left_arr = mergesort(arr[:n])
		right_arr = mergesort(arr[n:])
		return merge(left_arr, right_arr)

def merge(left_arr, right_arr):
	result = []
	i,j = 0, 0
	while i < len(left_arr) and j < len(right_arr):
		if left_arr[i] <= right_arr[j]:
			result.append(left_arr[i])
			i += 1
		else:
			result.append(right_arr[j])
			j += 1
	# Add the rest of arrays
	result += left_arr[i:]
	result += right_arr[j:]
	return result

A = [1, 2, 4, 3, 7, 3, 9, 0, 0]
print(mergesort(A))