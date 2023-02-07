n = int(input())
arr = list(map(int,input().split()))
dp1 = [1]*n
dp2 = [1]*n
dp3 = [0]*n
for i in range(n):
    for j in range(i):
        if arr[j]<arr[i]:
            dp1[i] = max(dp1[i],dp1[j]+1)
    
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if arr[j]<arr[i]:
            dp2[i] = max(dp2[i],dp2[j]+1)

for i in range(n):
    dp3[i] = dp1[i]+dp2[i]
    
print(max(dp3)-1)