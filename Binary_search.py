######### Binary Search ##############

# 1) Sorted Array 
# 2) mid = i + (j-i)//2 (i=starting index, j = end index)
# 3) i) arr[mid] = x return mid      O(1)
#    ii) arr[mid] < x   recursion    BinarySearch(arr,mid+1,j,x)    
#    iii) arr[mid] > x   recursion    BinarySearch(arr,i,mid-1,x) 
# 4) Time Complexity: O(logn)






# Binary Search using Recursion
# def BinarySearch(arr,i,j,x):
#     while i <= j:
#         mid = i + (j-i)//2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x:
#             return BinarySearch(arr,mid+1,j,x)
#         else:
#             return BinarySearch(arr,i,mid-1,x)
#     return -1

# arr = [2,4,6,8,10,12,14,16,18,20]
# i = 0
# j = len(arr) - 1
# x = 2

# output = BinarySearch(arr,i,j,x)
# print("The Number you are looking for is at index: ", output)




# Binary Search without Recursion
def BinarySearch(arr,i,j,x):
    while i <= j:
        mid = i + (j-i)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            i = mid + 1
        else:
            j = mid - 1
    return -1

arr = [2,4,6,8,10,12,14,16,18,20]
i = 0
j = len(arr) - 1
x = 20

output = BinarySearch(arr,i,j,x)
print("The Number you are looking for is at index: ", output)