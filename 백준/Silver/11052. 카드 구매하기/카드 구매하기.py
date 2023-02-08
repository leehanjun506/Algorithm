import copy
n = int(input())
card = list(map(int,input().split()))
dp = copy.deepcopy(card)
dp[1] = max(2*card[0],card[1])
for i in range(2,n):
    for j in range(i):
        dp[i] = max(dp[i],dp[i-j-1]+dp[j]) 
print(dp[n-1])