#백준18352
from collections import deque
n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

depth = [0]*(n+1)
visited = [False]*(n+1)
q = deque()

def bfs(graph):
    q.append(x)
    visited[x] = True # 방문
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == False:
                depth[i] = depth[v]+1 ## 제일중요!
                q.append(i)
                visited[i] = True
bfs(graph)    
for i in range(n+1):
    if depth[i] == k:
        print(i)

if k not in depth:
    print(-1)