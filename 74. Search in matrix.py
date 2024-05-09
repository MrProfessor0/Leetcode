def search_in_matrix(matrix,target):
    row = len(matrix)
    col = len(matrix[0])

    start = 0
    end = row*col-1

    while(start<=end):
        # mid = (start+end)//2
        mid = start + (end-start)//2
        element = matrix[mid//col][mid%col]

        if element == target:
            return True
        if target < element:
            end = mid - 1
        if target > element:
            start = mid + 1
        
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 33

print(search_in_matrix(matrix=matrix, target=target))