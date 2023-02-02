tc = int(input())
for i in range(tc):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]
    for i in range(n):
        if i == 0:
            dp[0][0],dp[1][0] = arr[0][0],arr[1][0]
        elif i == 1:
            dp[0][1],dp[1][1] = arr[1][0]+arr[0][1],arr[0][0]+arr[1][1]
        else:
            dp[0][i] = max(arr[0][i]+dp[1][i-1],arr[0][i]+dp[1][i-2])
            dp[1][i] += max(arr[1][i]+dp[0][i-1],arr[1][i]+dp[0][i-2])
    print(max(ans[n-1] for ans in dp))