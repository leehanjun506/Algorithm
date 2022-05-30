from collections import deque

n = int(input())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
time = [0]*(n+1)
for i in range(1,n+1):
    data = list(map(int,input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] +=1
        graph[x].append(i)

def topology():
    q = deque()
    
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while(q):
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -=1
            if indegree[i] == 0:
                time[i] += time[now]
                q.append(i)
                
    for i in range(1,n+1):
        print(time[i])

topology()