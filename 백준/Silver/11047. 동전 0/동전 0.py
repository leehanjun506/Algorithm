n,k = map(int,input().split())
list = [int(input()) for _ in range(n)]
list.reverse()
count = 0

for i in list:
    if k//i==0:
        continue
    count += k//i
    k %= i
print(count)