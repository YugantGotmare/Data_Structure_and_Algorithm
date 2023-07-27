# Bubble sort 
# Time Complexity O(n^2)
# space complexity O(1)



def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr = [70,20,50,30,90,5,1,15]
output = BubbleSort(arr)
print(output)