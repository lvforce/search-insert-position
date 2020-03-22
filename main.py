""" 
Search Insert Position 
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Example:
Input: [1,3,5,6], 5
Output: 2

Input: [1,3,5,6], 2
Output: 1

Input: [1,3,5,6], 7
Output: 4

Input: [1,3,5,6], 0
Output: 0
"""

import random
import time


def binary_search(arr, left, right, value):
	start_time = time.time()
	if right >= left:

		mid = left + (right - left) // 2
		if arr[mid] == value:
			print("Time of execution recursive: %f s" % (time.time() - start_time))
			return mid 
		elif arr[mid] > value:
			return binary_search(arr, left, mid - 1, value)
		else:
			return binary_search(arr, mid + 1, right, value)
	else:
		for i in range(len(arr)):
			if value < arr[i]:
				print("Time of execution recursive:: %f s" % (time.time() - start_time))
				return i
		print("Time of execution recursive:: %f s" % (time.time() - start_time))		
		return len(arr)


def iterative_binary_search(arr, left, right, value):
	start_time = time.time()
	while left <= right:

		mid = left + (right - left) // 2
		if arr[mid] == value:
			print("Time of execution iterative: %f s" % (time.time() - start_time))
			return mid
		elif arr[mid] < value:
			left = mid + 1
		else:
			right = mid - 1 
	else:
		for i in range(len(arr)):
			if value < arr[i]:
				print("Time of execution iterative: %f s" % (time.time() - start_time))
				return i
		print("Time of execution iterative: %f s" % (time.time() - start_time))
		return len(arr)



def for_hundred_thousand_items():
	print("Search for hundred thousand items")
	arr = [random.randint(0,100000) for _ in range(100000)]
	arr.sort()
	test = [1,3,5,6]
	x = iterative_binary_search(arr, 0, len(arr)-1, 20123)
	print("iterative position: ", x)
	print('')
	y = binary_search(arr, 0, len(arr)-1, 20123)
	print("recursive position: ", y)

def for_one_million_items():
	print("Search for one million items")
	arr = [random.randint(0,1000000) for _ in range(1000000)]
	arr.sort()
	x = iterative_binary_search(arr, 0, len(arr)-1, 420123)
	print("iterative position: ", x)
	print('\n')
	y = binary_search(arr, 0, len(arr)-1, 420123)
	print("recursive position: ", y)

for_hundred_thousand_items()
print("=============================")
for_one_million_items()