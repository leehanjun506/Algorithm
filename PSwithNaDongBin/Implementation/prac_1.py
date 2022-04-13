# 내 풀이
n = int(input())
move = input().split()

a,b=0,0
for i in range(len(move)):
    if move[i] == 'L':
        if b==0:
            continue
        b-=1
    elif move[i] == 'R':
        if b==n-1:
            continue
        b+=1
    elif move[i] == 'U':
        if a==0:
            continue
        a-=1
    else:
        if a==n-1:
            continue
        a+=1

print(a+1,b+1)

# 답안 예시

n = int(input())
x,y = 1,1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

# 이동 계획을 하나씩 확인
for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx<1 or nx>n or ny<1 or ny>n:
        continue
    x,y = nx,ny

print(x,y)        