#백준 14501
n = int(input())
dp_t = []
dp_p = []

for i in range(n):
    t,p = map(int,input().split())
    dp_t.append(t)
    dp_p.append(p)
dp = [0]*(n+1)
for i in range(n-1,-1,-1):
    if i+dp_t[i] >n:
        dp[i] = dp[i+1]
        continue
    if dp_t[i] == 1:
        dp[i] = dp_p[i] + dp[i+1]
        continue
    if dp_p[i] + dp[i+dp_t[i]] < max(dp[i+1:i+dp_t[i]]):
        dp[i] = dp[i+1]
    else:
        dp[i] = dp_p[i] + dp[i+dp_t[i]]
print(dp[0])