# Insertion Sort 
# Time Complexity 
# Best Case: O(n), when the array is ascending order. 
# Worst case: O(n^2), when the array is descending order 
# space complexity O(1)


def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key 
    return arr

arr = [9,5,1,4,3]
output = InsertionSort(arr)
print(output)