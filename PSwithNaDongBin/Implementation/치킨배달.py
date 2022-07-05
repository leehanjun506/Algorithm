# 백준 15686
from itertools import combinations

bhc = []
home = []
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            bhc.append((i,j))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i,j))

def distance(x,y):
    dis = abs(x[0]-y[0]) + abs(x[1]-y[1])
    return dis

ans_list = []

not_close_bhc = list(combinations(bhc,m))
for i in not_close_bhc: # i는 조합의 개수
    ans = 0
    for k in home:
        min_v = int(1e9)
        for j in i:
            min_v = min(min_v,distance(j,k))
        ans+=min_v
    ans_list.append(ans)
ans_list.sort()
print(ans_list[0])