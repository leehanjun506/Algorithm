n,m = map(int,input().split())
t = []
for i in range(n):
    t.append(int(input()))

l,r = min(t),max(t)*m
ans = r
while(l<=r):
    total = 0
    mid = (l+r)//2
    for time in t:
        total += mid//time
    if total >= m:
        r = mid-1
        ans = min(ans,mid)
    else :
        l = mid+1

print(ans)
