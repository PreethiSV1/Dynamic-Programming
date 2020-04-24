# Common mistake
# Some people will be tempted to come up with a quick solution,
# which is unfortunately flawed (however can be corrected easily)
# Reverse S and become S', Find the longest common substring between SS and S'S
# example: S = "abacdfgdcaba", S' = "abacdgfdcaba".
#
# The longest common substring between S and S' is "abacd".
# Clearly, this is not a valid palindrome.
# We could see that the longest common substring method fails when there exists
# a reversed copy of a non-palindromic substring in some other part of S


def LongestPalindromicSubstring(X):
    n = len(X)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    # palindromes of length 1
    for i in range(n):
        dp[i][i] = 1
    startIndex = 0
    maxLength = 1
    # find all palindromes of length 2
    for i in range(n - 1):
        if X[i] == X[i + 1]:
            dp[i][i + 1] = True
            startIndex = i
            maxLength = 2
    # Palindromes of length from 3 to n
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # X(i to j) (abcba) is a palindrome iff X(i+1 to j-1) (bcb)
            # is palindrome and X[i] (a) = X[j] (a)
            if dp[i + 1][j - 1] and X[i] == X[j]:
                dp[i][j] = True
                if length > maxLength:
                    maxLength = length
                    startIndex = i
    return X[startIndex: startIndex + maxLength]


X = "abacdfgdcaba"
print(LongestPalindromicSubstring(X))
