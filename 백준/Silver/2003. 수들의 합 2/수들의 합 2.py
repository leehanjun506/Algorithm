n,m = map(int,input().split())
arr = list(map(int,input().split()))
ans = 0
end = 0
s = 0
for start in range(n):
    while s<m and end<n:
        s+=arr[end]
        end+=1
    if s == m:
        ans+=1
    s-=arr[start]
print(ans)