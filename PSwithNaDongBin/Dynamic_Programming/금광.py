testcase = int(input())
for i in range(testcase):
    ans = []
    n,m = map(int,input().split())
    array = [[0]*m for _ in range(n)]
    gold = list(map(int,input().split()))
    row = 0
    column = 0
    for i in range(len(gold)):
        array[row][column] = gold[i]
        column+=1
        if (i+1)%m == 0:
            row +=1
            column = 0
    
    dp = [[0]*m for _ in range(n)]
    for i in range(n):
        dp[i][0] = array[i][0]
    for i in range(1,m): #열
        for j in range(n): #행
            if j == 0:
                dp[j][i] = max(dp[j][i-1],dp[j+1][i-1])+array[j][i]
            elif j == n-1:
                dp[j][i] = max(dp[j-1][i-1],dp[j][i-1])+array[j][i]
            else:
                dp[j][i] = max(dp[j-1][i-1],dp[j][i-1],dp[j+1][i-1])+array[j][i]
    
    for i in range(n):
        ans.append(dp[i][m-1])
    print(max(ans))