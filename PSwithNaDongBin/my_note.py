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