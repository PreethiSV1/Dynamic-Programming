# Given a rod of length n inches and an array of prices
# that contains prices of all pieces of size smaller than n.
# Determine the maximum value obtainable by cutting up the rod.
# Eg: [1, 5, 8, 9, 10, 17, 17, 20] => cut 8 as 2 + 6 => profit = 22


def RodCutting(value):
    n = len(value)
    maxProfit = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            # eg: i = 6, j = 2
            # maxProfit[6] = max(maxProfit[6], value[1] + maxProfit[4])
            # because index 1 contains value(price) of length 2 rod
            # index 4 contains maxProfit with length 4 rod
            maxProfit[i] = max(maxProfit[i], value[j - 1] + maxProfit[i - j])

    return maxProfit[n]


arr = [1, 5, 8, 9, 10, 17, 17, 20]
print(RodCutting(arr))
