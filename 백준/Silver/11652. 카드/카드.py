import sys
input = sys.stdin.readline

n = int(input())
dic = {}
for i in range(n):
    x = int(input())
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1
dic = sorted(dic.items(),key=lambda x: (-x[1],x[0]))
print(dic[0][0])