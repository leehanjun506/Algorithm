t = int(input())
ans = []

for _ in range(t):
    n,m = map(int,input().split())
    
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = 1
    
    for i in range(m):
        dp[0][i] = i+1
    
    for i in range(1,n):
        for j in range(i,m):
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    ans.append(dp[n-1][m-1])

for a in ans:
    print(a)