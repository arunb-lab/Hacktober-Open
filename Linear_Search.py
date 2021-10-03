# Searching an element in a list/array in python

# Example:
# if x in arr:
# print arr.index(x)

# Linearly search x in arr[]
# If x is present then return its location
# else return -1



def search(arr, x):

	for i in range(len(arr)):

		if arr[i] == x:
			return i

	return -1
