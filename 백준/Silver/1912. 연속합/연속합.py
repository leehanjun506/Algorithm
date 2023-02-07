import copy
n = int(input())
arr = list(map(int,input().split()))
dp = copy.deepcopy(arr)

for i in range(1,n):
    dp[i] = max(dp[i-1]+arr[i],arr[i])
        
print(max(dp))