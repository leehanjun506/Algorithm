n = int(input())
for i in range(n):
    r,s = input().split()
    r = int(r)
    ans = ''
    for i in s:
        ans+=i*r
    print(ans)