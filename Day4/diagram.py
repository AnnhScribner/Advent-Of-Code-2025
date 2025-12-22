def count_neighbors_paper_roll(matrix, row, col):
    count_neighbors = 0

    for d_row in (1,-1,0):
        for d_col in (1,-1,0):

            # is [row + d_row][col + d_col] valid? is it @?
            r = row + d_row
            c = col + d_col

            if r != -1 and r != len(matrix):
                if c != -1 and c != len(matrix[0]):
                    if matrix[r][c] == "@":
                        count_neighbors += 1
            

    return count_neighbors

    

matrix = []
with open("/Users/Anna/Documents/AdventOfCode2025/Dec4/rollsOfPaper.txt") as file:
    for line in file:
        list_line = list(line.strip())
        matrix.append(list_line)


count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "@":
            if count_neighbors_paper_roll(matrix, i, j) < 5:
                count += 1
            

print(count)

    
 
