#백준 18353
n = int(input())
max_v = 1e7+1
array = [max_v]+list(map(int,input().split()))

dp = [0]*(n+1) #길이들
for i in range(1,n+1):
    for j in range(i):
        if array[i]<array[j]:
            dp[i] = max(dp[i],dp[j]+1)
            
print(n-max(dp))
        