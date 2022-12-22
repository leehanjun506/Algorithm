n = int(input())
list = list(map(int,input().split()))
dp =[0]*1000001
max_v = 0
for i in list:
    dp[i] = dp[i-1]+1
    max_v = max(max_v,dp[i])
print(max_v)   