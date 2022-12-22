a,b = list(map(int,input().split()))
array = []
for i in range(a):
    array.append(int(input()))

dp = [10001]*(b+1)
dp[0]=0

for i in range(a):
    for j in range(array[i],b+1):
        dp[j]= min(dp[j],dp[j-array[i]]+1)

if dp[b]==10001:
    print(-1)
else:
    print(dp[b])
