def spiral_order(matrix):
    ans = []

    rows = len(matrix)
    cols = len(matrix[0])

    start_row = 0
    start_col = 0
    ending_row = rows
    ending_col = cols

    total = rows*cols
    count = 0

    while(count<total):

        # First Row
        for i in range(start_row,ending_col):
            if count>=total:
                break
            ans.append(matrix[start_row][i])
            count += 1
        start_row  += 1
        print(ans)

        # Ending Col
        for i in range(start_row,ending_row):
            if count>=total:
                break
            ans.append(matrix[i][ending_col-1])
            count+=1
        ending_col -= 1
        print(ans)


        # Print Ending Row
        for i in range(ending_col-1,start_col-1,-1):
            if count>=total:
                break
            ans.append(matrix[ending_row-1][i])
            count += 1
        ending_row -= 1
        print(ans)
        
        # Print Starting Row
        for i in range(ending_row-1,start_row-1,-1):
            if count>=total:
                break
            ans.append(matrix[i][start_col])
            count+=1
        start_col += 1
        print(ans)
        print()



    return ans

# T = [[1,2,3],[4,5,6],[7,8,9]]
T = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for i in T:
    for j in i:
        print(j,end=" ")
    print()
print()
# print(T)
print(spiral_order(T))