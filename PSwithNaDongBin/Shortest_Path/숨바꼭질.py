import heapq
from bisect import bisect_left,bisect_right
INF = int(1e9)
n,m = map(int,input().split())

distance = [INF]*(n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split()) # a에서 b로가는 비용1 b에서 a로 가는 비용1
    graph[a].append((b,1))
    graph[b].append((a,1))

start = 1
distance[start] = 0

def dij(start):
    q=[]
    heapq.heappush(q,(0,start))
    
    while q:
        dist,node = heapq.heappop(q)
        
        if distance[node] < dist:
            continue
        
        for i in graph[node]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


dij(start)
max_v = max(distance[1:])

# first = bisect_left(distance[1:],max_v)+1
# second = distance[first]
# third = distance[1:].count(second)
# print(f"{first} {second} {third}")


for i in range(1,n+1):
    if distance[i] == max_v:
        a = i
        break
b = distance[a]
c = distance.count(b)
print(a,b,c)