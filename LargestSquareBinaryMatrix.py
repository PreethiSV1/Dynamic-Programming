# Function to find the size of the largest square(1's) in a binary matrix (m x n)
def LargestSquareBinaryMatrix(X, m, n):
    # squareSizeDp[i][j] => size of maximum square in the matrix with right bottom at i and j
    squareSizeDp = [[0 for _ in range(n)] for _ in range(m)]
    maximumSquareSize = 0
    for i in range(m):
        for j in range(n):
            squareSizeDp[i][j] = X[i][j]

            # if we are not at the first row or first column and
            # current cell has value 1
            if i and j and X[i][j]:
                # largest square matrix ending at X[i][j] is
                # minimum of size of square matrix ending at
                # top, left and top-left <== Important!
                squareSizeDp[i][j] = 1 + min(squareSizeDp[i][j - 1], squareSizeDp[i - 1][j],
                                             squareSizeDp[i - 1][j - 1])

            if maximumSquareSize < squareSizeDp[i][j]:
                maximumSquareSize = squareSizeDp[i][j]

    return maximumSquareSize


X = [[0, 0, 1, 0, 1, 1],
     [0, 1, 1, 1, 0, 0],
     [0, 0, 1, 1, 1, 1],
     [1, 1, 0, 1, 1, 1],
     [1, 1, 1, 1, 1, 1],
     [1, 1, 0, 1, 1, 1],
     [1, 0, 1, 1, 1, 1],
     [1, 1, 1, 0, 1, 1]]
# X = [[0, 1]]
m = len(X)
n = len(X[0])
print(LargestSquareBinaryMatrix(X, m, n))
