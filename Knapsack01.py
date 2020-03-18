# Function to calculate total value that can be gained from the knapsack of given capacity
def Knapsack(value, weight, n, capacity):
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                # if that weight can be put inside the knapsack
                # maximum among the profits of including and excluding the current weight
                dp[i][w] = max(value[i - 1] + dp[i - 1][w - weight[i - 1]],  dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]


def contribution(weights, capacity):
    for i in range(n, 0, -1):
        if capacity < 0:
            break
        if dp[i][capacity] == dp[i - 1][capacity]:  # this item does not contribute to result
            continue
        else:
            print(str(weights[i - 1]), end=' ')
            capacity -= weights[i - 1]


values = [20, 5, 10, 40, 15, 25]
weights = [1, 2, 3, 8, 7, 4]
capacity = 10
n = len(values)
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
print(Knapsack(values, weights, n - 1, capacity))
contribution(weights, capacity)