from typing import List

def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    start_row = 0
    start_col = 0
    end_row = len(matrix) - 1
    end_col = len(matrix) - 1

    while(start_col<end_col):

        # print(start_row,start_col,end_row,end_col)
        for i in range(end_col-start_col):
            # Save the Top elements
            temp = matrix[start_row][start_col + i]

            # move bottom left into top left
            matrix[start_row][start_col + i] = matrix[end_row-i][start_col]

            # move bottom right into bottom left
            matrix[end_row-i][start_col] = matrix[end_row][end_col-i]

            # move top right into bottom right
            matrix[end_row][end_col-i] = matrix[start_col+i][end_col]

            # move top left into top right
            matrix[start_col+i][end_col] = temp

        start_row += 1
        start_col += 1
        end_row -= 1 
        end_col -= 1


    print()

    return matrix




# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
for row in matrix:
    for col in row:
        print(col,end=" ")
    print()

print("",end="\n\n")

rotated_matrix = rotate(matrix=matrix)
# print(rotated_matrix)
for row in rotated_matrix:
    for col in row:
        print(col,end=" ")
    print()





# # Solution with O(N) space.
# def rotate(matrix: List[List[int]]) -> None:
#     """
#     Do not return anything, modify matrix in-place instead.
#     """
#     n = len(matrix)

#     ans = []

#     for col in range(n):
#         temp = []
#         for row in range(n-1,-1,-1):
#             temp.append(matrix[row][col])
#         ans.append(temp)            

#     return ans
