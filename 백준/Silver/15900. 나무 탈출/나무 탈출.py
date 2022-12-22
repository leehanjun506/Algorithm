import sys
sys.setrecursionlimit(10**5)
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
sum = 0
dis = [0]*(n+1)
for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dis[i] = dis[v] + 1
            dfs(i)

dfs(1)
for i in range(2,n+1):
    if len(graph[i]) == 1:
        sum+= dis[i]
if sum % 2 == 0:
    print('No')
else:
    print('Yes')