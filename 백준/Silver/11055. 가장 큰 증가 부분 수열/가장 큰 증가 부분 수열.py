import copy
n = int(input())
arr = list(map(int,input().split()))
dp = copy.deepcopy(arr)
sum = 0
for i in range(n):
    for j in range(i):
        if arr[j]<arr[i]:
            dp[i] = max(dp[i],dp[j]+arr[i])
print(max(dp))