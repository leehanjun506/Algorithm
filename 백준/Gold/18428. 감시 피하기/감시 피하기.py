import copy
from itertools import combinations
from bisect import bisect_left, bisect_right
# from collections import deque
# import heapq
n = int(input())
graph = [input().split() for _ in range(n)]
location = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'X':
            location.append((i,j))

loc_num = list(combinations(location,3))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,dir):
    global meet
    nx = x + dx[dir]
    ny = y + dy[dir]
    
    if nx<0 or nx>=n or ny<0 or ny>=n or new_graph[nx][ny] == 'O':
        return
    elif new_graph[nx][ny] == 'X' or new_graph[nx][ny] == 'T':
        dfs(nx,ny,dir)
    else:
        meet = True
# 선생님이 상화좌우로 쭉 퍼져나가는데 장애물 만나면 return True 학생만나면 False


for loc in loc_num:
    meet = False
    new_graph = copy.deepcopy(graph)
    
    for three in loc:
        new_graph[three[0]][three[1]] = 'O'

    for i in range(n):
        for j in range(n):
            if new_graph[i][j] == 'T':
                for dir in range(4): # k 상하좌우 쭉 탐색
                    dfs(i,j,dir)
    
    if meet == False:
        print('YES')
        break
    
    
if meet == True:
    print('NO')