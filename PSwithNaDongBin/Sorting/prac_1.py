# 내 풀이
n = int(input())
list = [int(input()) for _ in range(n)]

list.sort(reverse=True)

for i in list:
    print(i,end=" ")