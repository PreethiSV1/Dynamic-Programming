# Function to find the most efficient way to multiply given sequence of matrices
import sys


def MatrixChainOrderingCost(value):
    n = len(value)

    dp = [[0 for _ in range(n)] for _ in range(n)]
    # dp[i,j] = minimum number of scalar multiplications (i.e., cost)
    # needed to compute the matrix M[i]M[i+1]...M[j] = M[i..j]
    # The cost is zero when multiplying one matrix <====

    # for each kind of possible split, we calculate cost and find the minimum
    for length in range(2, n):
        for start in range(1, n - length + 1):
            end = start + length - 1
            dp[start][end] = sys.maxsize
            for k in range(start, end):
                # split and find for M[start..k] and M[k..end] and add them with the cost
                cost = dp[start][k] + dp[k + 1][end] + \
                       value[start - 1] * value[k] * value[end]
                if cost < dp[start][end]:
                    dp[start][end] = cost
    return dp[1][n - 1]


# input is 10 x 30 matrix, 30 x 5 matrix, 5 x 60 matrix
dimensions = [10, 30, 5, 60]
n = len(dimensions)
print(MatrixChainOrderingCost(dimensions))
