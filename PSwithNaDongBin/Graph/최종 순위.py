# 백준 3665
# 사이클을 가진다면 impossible 출력
# indegree 0인 것 큐에 2개이상 들어가면 ?
from collections import deque

def topology():
    # for i in range(1,len(team)+1):
    #     if indegree[i]<0:
    #         return "IMPOSSIBLE"
    result = []
    q = deque()
    cycle = 0
    
    for i in range(1,len(team)+1):
        if indegree[i] == 0:
            q.append(i)
            if len(q) > 1:
                return '?'
    
    while q:
        node = q.popleft()
        result.append(node)
        tag = 0
        
        cycle += 1
        
        
        for i in graph[node]:
            indegree[i] -=1
            if indegree[i] == 0:
                tag+=1
                if tag>1:
                    return '?'
                q.append(i)
    if cycle < len(team):
        return "IMPOSSIBLE"
    return result

tc = int(input())

for i in range(tc):
    n = int(input())
    team = list(map(int,input().split()))
    m = int(input())
    graph = [[] for _ in range(len(team)+1)]
    indegree = [0]*(len(team)+1)
    for i in range(len(team)-1):
        for j in range(i+1,len(team)):
            graph[team[i]].append(team[j]) #i에서 j로 가는 경로
            indegree[team[j]]+=1
            
    for i in range(m):
        a,b = map(int,input().split()) # a,b순서 바꿈
        if a in graph[b]:
            graph[b].remove(a)
            graph[a].append(b)
            indegree[a]-=1
            indegree[b]+=1
        else:
            graph[a].remove(b)
            graph[b].append(a)
            indegree[b]-=1
            indegree[a]+=1            
            
    result = topology()
    if result == '?' or result == "IMPOSSIBLE":
        print(result)
    else:
        for i in result:
            print(i,end=" ")
        print()