#백준18428
from itertools import combinations
import copy
n = int(input())
graph = [input().split() for _ in range(n)]

list_x = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'X':
            list_x.append((i,j))

comb = list(combinations(list_x,3))

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x,y,dir):
    nx = x+dx[dir]
    ny = y+dy[dir]
    if nx<0 or nx>=n or ny<0 or ny>=n:
        return
    if map[nx][ny] == 'O':
        return
    if map[nx][ny] == 'S':
        global poss
        poss = False
    dfs(nx,ny,dir)

for o in comb:
    poss = True
    map = copy.deepcopy(graph)
    
    o1,o2,o3 = o[0],o[1],o[2]
    map[o1[0]][o1[1]] = 'O'
    map[o2[0]][o2[1]] = 'O'
    map[o3[0]][o3[1]] = 'O'
    for i in range(n):
        for j in range(n):
            if map[i][j] == 'T':
                for dir in range(4):
                    dfs(i,j,dir)
    if poss == True:
        print("YES")
        break
if poss == False:
    print("NO")