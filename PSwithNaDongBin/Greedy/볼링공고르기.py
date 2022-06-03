'''
from itertools import combinations
n,m = map(int,input().split())
ball = list(map(int,input().split()))

count = 0

ball.sort()

result = len(list(combinations(ball,2)))
for i in range(1,m+1):
    if ball.count(i) == 2:
        count+=1

print(result-count)
'''

n,m = map(int,input().split())
ball = list(map(int,input().split()))

weight_list = [0]*(m+1)

for i in ball:
    weight_list[i]+=1

cnt = 0

for i in range(1,m+1):
    n-=weight_list[i]
    cnt+=n*weight_list[i]

print(cnt)