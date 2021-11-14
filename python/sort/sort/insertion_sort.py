
'''Code challenge 26 '''
def insertion_sort(array):
    n=len(array)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if (array[j] < array[min]):
                min=j
        temp=array[min]
        array[min]=array[i]
        array[i]=temp
    return array
