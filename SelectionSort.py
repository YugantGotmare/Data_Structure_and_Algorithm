# Selection sort 
# Time Complexity O(n^2)

def SelectionSort(arr):
    for i in range(len(arr)):
        min_idx = i 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j 
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [50,1,38,45,79,19,27,29]
output = SelectionSort(arr)
print(output)