# Python3 implementation to count the
# number of ways to divide N in
# groups such that each group
# has K number of elements

# DP Table
# Function to count the number of
# ways to divide the number N in groups


def countWaystoDivide(n, k):
	if(n < k):
		return 0

	dp = [[0 for i in range(k+1)] for i in range(n+1)]
	for i in range(1, n+1):
		dp[i][1] = 1
	dp[0][0] = 1
	for i in range(1, n+1):
		for j in range(2, k+1):
			if(i >= j):
				dp[i][j] = dp[i-1][j-1] + dp[i-j][j]

			else:
				dp[i][j] = dp[i-1][j-1]
	return dp[n][k]


# Driver Code
if __name__ == '__main__':
	N = 8
	K = 4

	print(countWaystoDivide(N, K))

# This code is contributed by Rajput-Ji
