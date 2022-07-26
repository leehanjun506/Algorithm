#백준 16234 , 삼성 기출

n,l,r = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
move = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def open(x,y,nx,ny):
    if abs(graph[x][y]-graph[nx][ny])>=l and abs(graph[x][y]-graph[nx][ny])<=r:
        return True
    return False
def dfs(x,y):
    global sum
    visited[x][y] = True
    sum += graph[x][y]
    save.append((x,y))
    for i in range(4):
        nx = x+ dx[i]
        ny = y+ dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n or visited[nx][ny]==True or open(x,y,nx,ny)==False:
            continue
        dfs(nx,ny)
            

while True:
    visited = [[False]*n for _ in range(n)]
    tag = 0
    
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx = i+dx[k]
                ny = j+dy[k]
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    continue
                if open(i,j,nx,ny) == True:
                    tag+=1
    if tag >0:
        move+=1
    else:
        break
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                sum = 0
                save = []
                dfs(i,j)
                for k in save:
                    graph[k[0]][k[1]] = sum//len(save)
    


print(move)