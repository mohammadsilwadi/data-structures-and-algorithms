'''code challenge 27 '''
def mergesort(arr):
    n=len(arr)
    if n>1:
        mid=n//2
        left=arr[:mid]
        right=arr[mid:]
        mergesort(left)
        mergesort(right)
        return merge(left,right,arr)
def merge(left,right,arr):
    i=0
    j=0
    k=0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1

        k = k + 1
    if i == len(left):
     arr[k:]=right[j:]
    else:
     arr[k:]=left[i:]



    return arr

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")

    print(arr)
    print("Sorted array is: ", end="\n")
    print(mergesort(arr))
