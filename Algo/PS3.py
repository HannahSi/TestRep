v = [[0, 0, 0], [45, 20, 50], [70, 45, 50], [90, 75, 80], [105, 110, 100], [120, 150, 130]]
M = [[0] * 6, [0] * 6, [0] * 6]

for n in range(0, 6):
    M[0][n] = v[n][0]

for j in range(1, 3):
    for n in range(0, 6):
        M[j][n] = 0
        for i in range(0, n+1):
            M[j][n] = max(M[j][n], v[i][j] + M[j-1][n-i])

print(M[0])
print(M[1])
print(M[2])

def findSolution(j, n):
    if j == 0:
        assignments = n
    else:
        assignments = 0
        max_life = M[j][0]
        for i in range(1, n+1):
            if (max_life < v[i][j] + M[j-1][n-i]):
                max_life = v[i][j] + M[j-1][n-i]
                assignments = i
        findSolution(j-1, n-assignments)
    print(j, assignments)

findSolution(2, 5)
