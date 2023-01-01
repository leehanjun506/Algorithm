from collections import deque
def solution(maps):
    n,m = len(maps),len(maps[0])
    visited = [[False]*m for _ in range(n)]
    dis = [[0]*m for _ in range(n)]
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny]:
                q.append((nx,ny))
                dis[nx][ny] = dis[x][y]+1
                visited[nx][ny] = True
                if nx == n-1 and ny == m-1:
                    return dis[x][y]+2
    return -1