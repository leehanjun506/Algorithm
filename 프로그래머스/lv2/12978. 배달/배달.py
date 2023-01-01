def solution(n, road, K):

    INF = int(1e9) 
    m = len(road)
    start = 1
    graph = [[] for i in range(n+1)]
    visited = [False]*(n+1)
    distance = [INF]*(n+1)

    for i in range(m):
        a,b,c = road[i][0],road[i][1],road[i][2]
        graph[a].append((b,c))
        graph[b].append((a,c))
        

    def get_smallest_node():
        min_value = INF
        index = 0 
        for i in range(1,n+1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index

    def dijkstra(start):
        distance[start] = 0
        visited[start] = True
        for j in graph[start]:
            if j[1] < distance[j[0]]:
                distance[j[0]] = j[1]
        for _ in range(n-1): 
            now = get_smallest_node() 
            visited[now] = True
            for j in graph[now]:  
                cost = distance[now] + j[1]
                if cost < distance[j[0]]:
                    distance[j[0]] = cost
    dijkstra(start)

    ans=0
    for i in range(1,n+1):
        if distance[i] <= K:
            ans+=1
    return ans