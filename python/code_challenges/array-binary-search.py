def findValue(list, num):
	low = 0
	high = len(list)-1

	while low <= high:
		middle = low + (high - low) // 2

		if list[middle] == num:
			return middle
		elif list[middle] < num:
			low = middle + 1
		else:
			high = middle - 1
	return -1
list=[1,2,3,4,5,6,7,8,9]

print(findValue(list,9))

