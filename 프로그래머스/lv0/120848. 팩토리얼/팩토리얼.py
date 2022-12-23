def solution(n):
    answer = 0
    dp = [0]*12
    dp[0] = 0
    dp[1] = 1
    for i in range(2,12):
        dp[i] = i*dp[i-1]
        if dp[i] > n:
            return i-1
