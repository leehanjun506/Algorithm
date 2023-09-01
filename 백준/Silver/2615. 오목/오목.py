# 검 : 1 흰 : 2 빈 : 0
graph = [list(map(int,input().split())) for _ in range(19)]

# 오른쪽, 아래, 오른쪽아래, 오른쪽 위
dx = [0,1,1,-1]
dy = [1,0,1,1]

def check(x,y,color):
    for i in range(4):
        cnt = 1
        nx = x + dx[i]
        ny = y + dy[i]
        while True:
            if nx <0 or nx>=19 or ny <0 or ny>=19 or graph[nx][ny] != color or graph[nx][ny] == 0:
                break
            cnt+=1
            # 오목일때 육목 확인
            # 초기 값 이전값이 원래색깔과 같을때
            # 마지막 값 다음값이 원래색깔과 같을때
            # 육목일때 없애버리기
            if cnt == 5:

                if x-dx[i]>=0 and x-dx[i]<19 and y-dy[i]>=0 and y-dy[i]<19 and graph[x-dx[i]][y-dy[i]] == color:
                    break
                if nx+dx[i]>=0 and nx+dx[i]<19 and ny+dy[i]>=0 and ny+dy[i]<19 and graph[nx+dx[i]][ny+dy[i]] == color:
                    break

                print(color)
                print(x+1,y+1)
                exit(0)

            nx += dx[i]
            ny += dy[i]

for i in range(19):
    for j in range(19):
        color = graph[i][j]
        check(i,j,color)
print(0)