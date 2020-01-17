def EditDistance(X, m, Y, n):
    distance = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m + 1):
        distance[i][0] = i

    for i in range(n + 1):
        distance[0][i] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                distance[i][j] = distance[i - 1][j - 1]
            else:
                distance[i][j] = min(distance[i - 1][j], # Delete letter from X
                                     distance[i][j - 1], # Insert letter from Y to X
                                     distance[i - 1][j - 1]) + 1 # Replace letter in X with Y

    return distance[m][n]


X = "sunday"
Y = "saturday"
print(EditDistance(X, len(X), Y, len(Y)))