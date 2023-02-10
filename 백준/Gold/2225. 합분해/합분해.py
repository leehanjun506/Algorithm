n,k = map(int,input().split())
dp = [[0]*k for _ in range(n)]
for i in range(n):
    dp[i][0] = 1
for j in range(k):
    dp[0][j] = j+1
for i in range(1,n):
    for j in range(1,k):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000000
print(dp[n-1][k-1])
