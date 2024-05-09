def searchMatrix(matrix, target: int) -> bool:
    row = len(matrix)
    col = len(matrix[0])

    row_index = 0
    col_index = col-1

    while(row_index<row and col_index>=0):
        # print(row_index,co)
        element = matrix[row_index][col_index]

        if element == target:
            return True
        if element<target:
            row_index += 1
        else:
            col_index -= 1

    return False


# matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# target = 20

matrix =  [[-5]]
target = -10
print(searchMatrix(matrix=matrix,target=target))