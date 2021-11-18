'''code challenge 28 '''
def quick_sort(arr,left,right):

    if left<right:
        postion = partition(arr,left,right)
        quick_sort(arr,left,postion-1)
        quick_sort(arr,postion+1,right)

def partition(arr,left,right):
    pivot=arr[right]
    low=left-1
    for i in range(left,right):
            if arr[i] <= pivot:
                low=low+1
                swap(arr,i,low)

    swap(arr, right, low + 1)

    return low + 1


def swap(arr,i,low):
    temp=arr[i]

    arr[i]=arr[low]
    arr[low]=temp

if __name__ == '__main__':
    arr = [ 3,5,1,4]
    print(f'UnSorted array:{arr}')
    quick_sort(arr,0,len(arr)-1)

    print(f'Sorted array: {arr}')
