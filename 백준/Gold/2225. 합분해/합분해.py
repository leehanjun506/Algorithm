n,k = map(int,input().split())
dp = [[0]*k for _ in range(n)]
# n,k 최대값은 0+ (n k-1로) , 1 + (n-1 k-1로) , 2 + (n-2 k-1로)
# dp[n][k] = dp[0][k-1] + dp[1][k-1] + dp[2][k-2] + ... dp[n][k-1]
# dp[n-1][k] = dp[0][k-1] + ... dp[n-1][k-1]

# dp[n][k] = dp[n-1][k] + dp[n]
for i in range(n):
    dp[i][0] = 1
for j in range(k):
    dp[0][j] = j+1
for i in range(1,n):
    for j in range(1,k):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000000
print(dp[n-1][k-1])
