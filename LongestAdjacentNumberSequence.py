# Function to find the longest sequence of consecutive numbers in any (<-, ->, ^, v️) direction
# in a matrix (n x n) with no duplicates
def LongestAdjacentNumberSequence(X, n, i, j, dp):
    if i > n or i < 0 or j > n or j < 0:  # exit conditions
        return ''

    if dp[i][j] == 0:  # if lookup not found
        path = ''  # Initially no adjacent values found => ''

        # no duplicates in the matrix => only one of the four adjacent values
        # can be consecutive of the current number.

        if i - 1 >= 0 and X[i - 1][j] - X[i][j] == 1:  # Number Above
            path = LongestAdjacentNumberSequence(X, n, i - 1, j, dp)

        if i + 1 < n and X[i + 1][j] - X[i][j] == 1:  # Number Below
            path = LongestAdjacentNumberSequence(X, n, i + 1, j, dp)

        if j - 1 >= 0 and X[i][j - 1] - X[i][j] == 1:  # Number to the Left
            path = LongestAdjacentNumberSequence(X, n, i, j - 1, dp)

        if j + 1 < n and X[i][j + 1] - X[i][j] == 1:  # Number to the Right
            path = LongestAdjacentNumberSequence(X, n, i, j + 1, dp)

        if path != '':  # Add path if found
            dp[i][j] = str(X[i][j]) + ' - ' + path

        else:  # else add the current number alone
            dp[i][j] = str(X[i][j])

    return dp[i][j]


X = [
    [10, 13, 14, 21, 23],
    [11, 9, 22, 2, 3],
    [12, 8, 1, 5, 4],
    [15, 24, 7, 6, 20],
    [16, 17, 18, 19, 25]
]
n = len(X)
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
resultSize = 0
result = ''
for i in range(n):
    for j in range(n):
        path = LongestAdjacentNumberSequence(X, n, i, j, dp)
        pathLen = len(path.split('-'))
        if pathLen > resultSize:
            result = path
            resultSize = pathLen
print(result)
print(resultSize)
