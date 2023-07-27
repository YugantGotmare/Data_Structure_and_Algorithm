def Search_2Darray_sorted_martix(matrix, target):
    # Number of Row
    m = len(matrix)
    if m == 0:
        return False
    # Number of Columns
    n = len(matrix[0])

    left, right = 0, m*n-1
    while left <= right:
        mid = left + (right-left)//2
        mid_element = matrix[mid//n][mid%n]
        if target == mid_element:
            return True
        elif target < mid_element:
            right = mid - 1
        else:
            left = mid + 1
    return False

matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,24,60]]

target = 33

output = Search_2Darray_sorted_martix(matrix, target)
print(output)