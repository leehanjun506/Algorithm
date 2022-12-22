from collections import deque
n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
depth = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    #a에서 b로 이동한다.
    graph[a].append(b)

city = []
def bfs():
    q = deque()
    q.append(x)
    visited[x] = True
    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                depth[i] = depth[node]+1
                q.append(i)
                visited[i] = True
bfs()
for i in range(n+1):
        if depth[i] == k:
            print(i)
            
if k not in depth:
    print(-1)
