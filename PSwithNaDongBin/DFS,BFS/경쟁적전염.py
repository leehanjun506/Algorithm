#백준18405

# k개의 바이러스에 대해서 bfs 탐색 각각 하는거 중요! 
from collections import deque

n,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
s,X,Y = map(int,input().split())
virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j],i,j))
virus.sort()
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque(virus)
    time = 0
        
    while q:
        if time == s:
            break
        for i in range(len(q)):
            value,x,y = q.popleft()
            
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx>-1 and nx<n and ny>-1 and ny<n and graph[nx][ny] == 0 :
                    graph[nx][ny] = value
                    q.append((graph[nx][ny],nx,ny))
        time+=1

bfs()
if graph[X-1][Y-1] == 0:
    print(0)
else:
    print(graph[X-1][Y-1])
                