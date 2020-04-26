# Function to find maximum value of the expression
# (X[s] - X[r] + X[q] - X[p]) where s > r > q > p


def MaximizeExpressionValue(X, n):
    L1 = [-9999999 for _ in range(n + 1)]
    L2 = [-9999999 for _ in range(n)]
    L3 = [-9999999 for _ in range(n - 1)]
    L4 = [-9999999 for _ in range(n - 2)]

    # L1[] stores the maximum value of X[i]
    for i in range(n - 1, -1, -1):
        L1[i] = max(L1[i + 1], X[i])

    # L2[] stores the maximum value of X[l] - X[k]
    for i in range(n - 2, -1, -1):
        L2[i] = max(L2[i + 1], L1[i + 1] - X[i])

    # L3[] stores the maximum value of X[l] - X[k] + X[j]
    for i in range(n - 3, -1, -1):
        L3[i] = max(L3[i + 1], L2[i + 1] + X[i])

    # L4[] stores the maximum value of X[l] - X[k] + X[j] - X[i]
    for i in range(n - 4, -1, -1):
        L4[i] = max(L4[i + 1], L3[i + 1] - X[i])

    # maximum value would be present at L4[0]
    print(L1, L2, L3, L4)

    return L4[0]


X = [3, 9, 10, 1, 30, 40]
n = len(X)
if n >= 4:
    print(MaximizeExpressionValue(X, n))
