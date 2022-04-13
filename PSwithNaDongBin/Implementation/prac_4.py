# 내 풀이
n , m = map(int,input().split())
A,B,d = map(int,input().split())

place = [list(map(int,input().split())) for _ in range(n)]
can = 1
nx,ny = A,B
place[nx][ny] = 1
while(True):
    if place[nx+1][ny] ==1 and place[nx-1][ny] ==1 and place[nx][ny-1] ==1 and place[nx][ny+1] ==1:
        if d == 0:
            nx,ny = A+1,B
            if place[nx][ny] == 1:
                break
        elif d == 1:
            nx,ny = A,B-1
            if place[nx][ny] == 1:
                break
        elif d == 2:
            nx,ny = A-1,B
            if place[nx][ny] == 1:
                break
        else:
            nx,ny = A,B+1
            if place[nx][ny] == 1:
                break
            
    elif d == 0:
       if place[nx][ny-1] == 0 :
           place[nx][ny-1] = 1
           nx,ny = A,B-1
           can +=1
           d = 3
       else:
           d = 3
    
    elif d == 1:
        if place[nx-1][ny] == 0:
            place[nx-1][ny] = 1
            nx,ny = A-1,B
            can +=1
            d = 0
        else:
            d = 0
    elif d == 2:
        if place[nx][ny+1] == 0:
            place[nx][ny+1] = 1
            nx,ny = A,B+1
            can +=1
            d = 1
        else:
            d = 1
    else :
        if place[nx+1][ny] == 0:
            place[nx+1][ny] = 1
            nx,ny = A+1,B
            can +=1
            d = 2
        else:
            d = 2

print(can)


# 답안 

n,m = map(int,input().split())

# 방문한 위치 저장
d = [[0]*m for _ in range(n)]
# 현재 캐릭터 x,y,방향 
x,y,dir = map(int,input().split())
d[x][y]=1 #현재 좌표 방문 처리

# 전체 맵 정보 입력
array = [list(map(int,input().split())) for _ in range(n)]

#북, 동, 남, 서 방향 정의
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3

# 시뮬 시작
count = 1
turn_time = 0
while True:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]
    # 회전한 이후 정면에 가보지 않은 칸 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count+=1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time +=1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        # 뒤로 갈 수 있으면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
    



