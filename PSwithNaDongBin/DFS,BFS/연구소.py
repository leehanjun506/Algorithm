import copy
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def score(w):
    num = 0
    for i in range(n):
        for j in range(m):
            if w[i][j] == 0:
                num+=1
    return num
                
def dfs(x,y,w):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>n-1 or ny<0 or ny>m-1 :
            continue
        if w[nx][ny] == 0:
            w[nx][ny] = 2
            dfs(nx,ny,w)
        
total = 0
def wall(x):# 벽을 생성하는 combinations 코드 !!
    global total
    if x==3:
        w = copy.deepcopy(a)
        for i in range(n):
            for j in range(m):
                if w[i][j] == 2:
                    dfs(i,j,w)
        num = score(w)
        total = max(total,num)
        return 
    for i in range(n):
        for j in range(m):            
            if a[i][j] == 0:
                a[i][j] = 1
                wall(x+1)
                a[i][j] = 0
wall(0)
print(total)