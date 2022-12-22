#백준 14502
from itertools import combinations
n,m = map(int,input().split())
temp = [list(map(int,input().split())) for _ in range(n)]
r = 3
list_a = []
for i in range(n):
    for j in range(m):
        list_a.append((i,j))

comb_list = []
l = len(list_a)

def comb(idx,n):
    if len(n) == r:
        comb_list.append(n[:])
    
    for i in range(idx,l):
        comb(i+1,n+[list_a[i]])
# comb(0,[])
h = list(combinations(list_a,r))
def dfs(x,y):
    if x<0 or x>n-1 or y<0 or y>m-1:
        return
    if graph[x][y] != 1 and visit[x][y] == 0:
        graph[x][y] = 2
        visit[x][y] = 1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
    return
count = 0
for i in h:
    tag = 0
    num = 0
    graph = [[0] * m for _ in range(n)]
    visit = [[0]*m for _ in range(n)]
    
    for row in range(n):
        for column in range(m):
            graph[row][column] = temp[row][column]
    for j in i:
        a,b = j[0], j[1]
        if graph[a][b] != 0:
            tag = 1
            break
        graph[a][b] = 1
    if tag == 1:
        continue
    for row in range(n):
        for column in range(m):
            if graph[row][column] == 2:
                dfs(row,column)
    
    for row in range(n):
        for column in range(m):
            if graph[row][column] == 0:
                num+=1
    count = max(count,num)

print(count)