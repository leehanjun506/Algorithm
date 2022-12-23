def solution(n):
    dp = [0]*100
    dp[0] = 1
    dp[1] = 2
    for i in range(2,100):
        dp[i] = dp[i-1]+1
        while(dp[i]%3 == 0 or '3' in str(dp[i])):
            dp[i] +=1
    return dp[n-1]