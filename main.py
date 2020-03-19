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

def binary_search(arr, left, right, value):
	if right >= left:

		mid = left + (right - left) // 2
		if arr[mid] == value:
			return mid
		elif arr[mid] > value:
			return binary_search(arr, left, mid - 1, value)
		else:
			return binary_search(arr, mid + 1, right, value)
	else:
		for i in range(len(arr)):
			if value < arr[i]:
				return i
		return len(arr)		
	




arr = [1,3,5,6]
x = binary_search(arr, 0, len(arr)-1, 7)
print(x)