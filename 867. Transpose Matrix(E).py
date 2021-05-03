matrix = [[1,2,3],[4,5,6]]

newmat = [[] for _ in range(len(matrix[0]))]
for c in range(len(matrix[0])):
    for r in range(len(matrix)):
        newmat[c].append(matrix[r][c])
        
print(newmat)
