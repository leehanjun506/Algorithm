# n*n에 물고기 m마리, 상어 1마리
# 첨에 상어 크기2 1초에 상하좌우로 이동
# 상어는 자기보다 큰 물고기가 있는 칸 못감
# 자기보다 작은 물고기 먹음, 같은 크기의 물고기 못먹고 지나갈 수 있음
from collections import deque
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            sh = (i,j) # 상어의 위치

dx = [-1,1,0,0]
dy = [0,0,-1,1]
            
size = 2      
def bfs(i,j):
    q = deque()
    q.append((i,j))
    visit[i][j] = True
    eat = []
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n or arr[nx][ny]>size or visit[nx][ny] == True:
                continue
            distance[nx][ny] = distance[x][y] + 1
            visit[nx][ny] = True
            q.append((nx,ny)) # 안먹었을때는 eat리스트에 넣지 않음
            if arr[nx][ny] < size and arr[nx][ny] != 0:
                eat.append((nx,ny,distance[nx][ny])) # 먹었을때는 eat리스트에
    return eat
    
    
ans = 0
cnt = 0
while True:
    distance = [[0]*n for _ in range(n)]
    visit = [[False]*n for _ in range(n)]
    eat = bfs(sh[0],sh[1])
    if len(eat) == 0:
        break
    eat.sort(key=lambda x: (x[2],x[0],x[1]))
    arr[sh[0]][sh[1]] = 0
    x,y,dis = eat[0]
    ans+= eat[0][2]
    sh = (x,y)
    arr[sh[0]][sh[1]] = 0
    
    cnt+=1
    if cnt == size:
        size+=1
        cnt = 0

print(ans)