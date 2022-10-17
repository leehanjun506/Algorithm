import heapq
t = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(t):
    n = int(input())
    INF = int(1e9)
    graph = [list(map(int,input().split())) for _ in range(n)]
        
    distance = [[INF]*n for _ in range(n)]
    start = (0,0)
    distance[0][0] = graph[0][0]
    q = []
    heapq.heappush(q,(distance[0][0],start))
    while q:
        
        dist,node = heapq.heappop(q)
        
        if distance[node[0]][node[1]] < dist:
            continue
        
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                cost = dist+graph[nx][ny]
                if cost<distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q,(cost,(nx,ny)))
    
    print(distance[n-1][n-1])