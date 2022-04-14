# 내 풀이

n,m = map(int,input().split())

graph = [list(map(int,input())) for _ in range(n)]

visited  = [[0]*m for _ in range(n)]
count=0
def dfs(graph,vx,vy,visited):
    if vx<=-1 or vx>=n or vy<=-1 or vy>=m or visited[vx][vy]==1:
        return False
    if graph[vx][vy]==0 and visited[vx][vy]==0:
        visited[vx][vy]=1
        dfs(graph,vx+1,vy,visited)
        dfs(graph,vx-1,vy,visited)
        dfs(graph,vx,vy+1,visited)
        dfs(graph,vx,vy-1,visited)
        return True
    


for i in range(m):
    for j in range(n):
        if dfs(graph,i,j,visited) == True:
            count+=1
print(count)       

#답안 예시

n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))
    
#DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    # 현재 노드 방문하지 않았다면
    if graph[x][y]==0:
        #해당 노드 방문 처리
        graph[x][y] = 1
        #상하좌우 위치 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True

    return False

        
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 dfs 수행
        if dfs(i,j) == True:
            result+=1

print(result)