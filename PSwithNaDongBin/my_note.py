# 현재 좌표
x,y = 1,1

# 북,동,남,서 방향 정의
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 칸 이동
nx = x + dx[0]
ny = y + dy[0]

x = nx
y = ny

# count_by_range

from bisect import bisect_left,bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a,left_value,right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    print(right_index)
    print(left_index)
    return right_index-left_index

# 리스트 선언
a = [1,2,3,3,3,3,4,4,8,9]
# 값이 4인 데이터 개수 출력
print(count_by_range(a,4,4))

# 값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_by_range(a,-1,3))

# split() 사용 시 구분자가 연속해서 있을 때 연속한 구분자는 빈칸으로 만든다.

a = '12334566678'
print(a.split('3'))
print(a.split('6'))
print([i for i in a.split('3') if i])
print([i for i in a.split('6') if i])

# bfs 사용시 특정 거리 파악할때 depth 리스트 만들고 deque에 넣을때 거리도 같이 설정해주자.

# 플로이드 ->cost 2차원 리스트로 만들고 d[x][y] = min(d[x][y],d[x][k]+d[k][y]) 
# 다익스트라 -> 우선순위큐에 start부터 노드까지의 최소거리와 노드정보를 넣자

# 순서 무시 : 조합(combinations) 순서 고려 : 순열(permutations)

'''Spanning Tree : 모든 노드 포함하면서 사이클 존재하지 않는 부분 그래프

1. 모든 간선에 대하여 정렬 수행 뒤 가장 거리가 짧은 간선부터 집합에 포함
2. 사이클 발생시킬 수 있는 간선의 경우 집합에 포함x
3. 집합에 포함된 경우 최종 비용 더하기?
최소 신장 트리 : 간선의 개수 = 노드의 개수 -1
'''

'''topology-sort 
진입차수 : 특정한 노드로 들어오는 간선의 개수
1.진입차수가 0인 노드를 큐에 넣는다
2.큐가 빌때까지 다음 과정 반복
    * 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
    * 새롭게 진입차수가 0이 된 노드를 큐에 넣음
큐에서 빠져나간 노드가 위상 정렬 수행한 결과
위상 정렬은 답안이 여러 가지가 될 수 있음. 한 단계에서 큐에 새롭게 들어가는 원소가 2개 이상인 경우.
모든 원소 방문 전 큐가 비어버리면 사이클 발생한 것
위상 정렬 시간 복잡도는 O(V+E)
'''