n= int(input())
arr = []
dp = [0]*n
for _ in range(n):
    arr.append(int(input()))

dp[0] = arr[0]
if n >= 2:
    dp[1] = arr[0]+arr[1]
if n >= 3:
    dp[2] = max(arr[0]+arr[1],arr[0]+arr[2],arr[1]+arr[2])
for i in range(3,n):
    dp[i] = max(arr[i] + dp[i-2], arr[i] + arr[i-1]+ dp[i-3], dp[i-1])

print(dp[n-1])