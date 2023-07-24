def LinearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i 
    return -1

arr = [1,2,3,4,5,6,7,8,9,10]
x = 10

output = LinearSearch(arr,x)
print("The Number you are looking for in at index: ", output)



##### Worst case complexity is O(n)
##### Best case complexity is O(n)
##### Space case complexity is O(1)