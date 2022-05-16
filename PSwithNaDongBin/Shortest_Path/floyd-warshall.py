INF = int(1e9) #무한이라는 의미로 10억 설정

# 노드의 개수 , 간선의 개수
n = int(input())
m = int(input())

# 2차원 리스트 만들고 , 모든 값 무한으로 초기화

graph = [[INF]*(n+1) for _ in range(n+1)]  #index 0 은 사용 x

# 자기 자신으로 가는 비용 0

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0
            
# 각 간선에 대한 정보 입력 후 리스트에 초기화

for _ in range(m):
    # a에서 b로가는 비용 c
    a,b,c = map(int,input().split())
    if c < graph[a][b]:
        graph[a][b] = c

# 플로이드 워셜 알고리즘    
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
            
# 결과 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        # 도달 할 수 없는 경우 무한출력
        if graph[a][b] == INF:
            print("0",end=" ")
        print(graph[a][b],end=" ")
    print()
