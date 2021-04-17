numRows = 5


n = [[1]]
i = 0
while i <= 5:
    n.append([a+b for a,b in zip(n[-1]+[0], [0]+n[-1])])
    i += 1

print(n)

