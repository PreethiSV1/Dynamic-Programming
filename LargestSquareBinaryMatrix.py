# Function to find the size of the largest square(1's) in a binary matrix (m x n)
def LargestSquareBinaryMatrix(X, m, n):
    # squareSize[i][j] => size of maximum square in the matrix with right bottom at i and j
    squareSize = [[0 for _ in range(n)] for _ in range(m)]
    maximumSquareSize = 0
    for i in range(m):
        for j in range(n):
            squareSize[i][j] = X[i][j]

            # if we are not at the first row or first column and
            # current cell has value 1
            if i and j and X[i][j]:
                # largest square matrix ending at X[i][j] is
                # minimum of size of square matrix ending at
                # top, left and top-left <== Important!
                squareSize[i][j] = 1 + min(squareSize[i][j - 1], squareSize[i - 1][j],
                                           squareSize[i - 1][j - 1])

            if maximumSquareSize < squareSize[i][j]:
                maximumSquareSize = squareSize[i][j]

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
