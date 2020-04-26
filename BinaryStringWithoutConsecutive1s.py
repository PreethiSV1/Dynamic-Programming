# Function to find all N-digit binary strings without any consecutive 1's
# Append 1 and recur only if last digit of partially formed number is 0
# That way, number will never have any consecutive 1's.


def BinaryStringWithoutConsecutive1s(N):
    dp = [[0, 0] for _ in range(N + 1)]
    dp[1][0] = 2  # if only 1 digit is left and previous digit is 0
    dp[1][1] = 1  # if only 1 digit is left and previous digit is 1

    for i in range(2, n + 1):
        # if last digit is 0, we can have both 0 and 1 at current position
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]

        # if last digit is 1, we can have only 0 at current position
        dp[i][1] = dp[i - 1][0]

    return dp[n][0]


def printCountStrings(N, result, lastDigit):
    if N == 0:
        print(result)
        return
    printCountStrings(N - 1, result + '0', 0)
    if lastDigit == 0:
        printCountStrings(N - 1, result + '1', 1)


n = 5
print(BinaryStringWithoutConsecutive1s(n))
printCountStrings(n, '', 0)
