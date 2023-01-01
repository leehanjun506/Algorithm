def solution(n):
    if n//2 == 1:
        return 0
    dp = [0]*5001
    dp[2] = 3
    dp[4] = 11
    dp[6] = 41
    x = [0]*5001
    x[6] = 1
    for i in range(8,n+1,2):
        x[i] = (dp[i-6] + x[i-2])%1000000007
        dp[i] = (3*dp[i-2] + 2*(dp[i-4]+x[i]))%1000000007
    
        
    return dp[n]