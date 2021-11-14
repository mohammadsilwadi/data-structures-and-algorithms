# Insertion Sort
## Challenge Summary
Selection Sort is a sorting algorithm that traverses the array multiple times as it slowly builds out the sorting sequence. The traversal keeps track of the minimum value and places it in the front of the array which should be incrementally sorted
## Insertion Sort pseudo code

+ pseudo code for insertion sort:
```
`SelectionSort(int[] arr)`
    DECLARE n <-- arr.Length;
    FOR i = 0; i to n - 1
        DECLARE min <-- i;
        FOR j = i + 1 to n
            if (arr[j] < arr[min])
                min <-- j;

        DECLARE temp <-- arr[min];
        arr[min] <-- arr[i];
        arr[i] <-- temp;
    ```
+ python code for insertion sort:

```
def SelectionSort(array)
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

### visual step


![](shot.png)

### Efficency
Time: O(n^2)
The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times…concluding the algorithm to be n squared.
Space: O(1)
No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).

[Pull Request](https://github.com/mohammadsilwadi/data-structures-and-algorithms/pull/36)



