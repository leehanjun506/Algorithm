n = int(input())
list = list(map(int,input().split()))
dp =[0]*1000001
max_v = 0
for i in range(0,n):
    dp[list[i]] = max(dp[list[i]],dp[list[i]-1]+1)
    max_v = max(max_v,dp[list[i]])

print(max_v)   
    