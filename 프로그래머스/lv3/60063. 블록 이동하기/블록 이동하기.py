from collections import deque
def possible_move(loc,map):
    loc = list(loc)
    x1,y1,x2,y2 = loc[0][0],loc[0][1],loc[1][0],loc[1][1]
    pos_list = []
    #상화좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx1 = x1 + dx[i]
        ny1 = y1 + dy[i]
        nx2 = x2 + dx[i]
        ny2 = y2 + dy[i]
        if map[nx1][ny1] == 0 and map[nx2][ny2] == 0:
            pos_list.append({(nx1,ny1),(nx2,ny2)})
    
    if x1==x2:
    #가로 위방향
        if map[x1-1][y1] == 0 and map[x2-1][y2] == 0:
            pos_list.append({(x1,y1),(x1-1,y1)})
            pos_list.append({(x2,y2),(x2-1,y2)})
    #가로 아래방향
        if map[x1+1][y1] == 0 and map[x2+1][y2] == 0:
            pos_list.append({(x1,y1),(x1+1,y1)})
            pos_list.append({(x2,y2),(x2+1,y2)})
    if y1==y2:
    #세로 왼쪽방향
        if map[x1][y1-1] == 0 and map[x2][y2-1] == 0:
            pos_list.append({(x1,y1),(x1,y1-1)})
            pos_list.append({(x2,y2),(x2,y2-1)})
    #세로 오른쪽방향
        if map[x1][y1+1] == 0 and map[x2][y2+1] == 0:
            pos_list.append({(x1,y1),(x1,y1+1)})
            pos_list.append({(x2,y2),(x2,y2+1)})
    return pos_list
            
    
def solution(board):
    board_len = len(board)
    map = [[1]*(board_len+2) for _ in range(board_len+2)]
    for i in range(board_len):
        for j in range(board_len):
            map[i+1][j+1] = board[i][j]
    visited = []
    q = deque()
    first = {(1,1),(1,2)}
    q.append((first,0)) # 첫번째 위치와 최소시간
    visited.append(first)
    while q:
        loc,cost = q.popleft()
        if (board_len,board_len) in loc:
            # return cost
            break
        
        for next_loc in possible_move(loc,map):
            if next_loc in visited:
                continue
            else:
                visited.append(next_loc)
                q.append((next_loc,cost+1)) # cost값 증가는 무조건 여기서! 만약 위쪽에 cost+=1로 증가시킨다면 다음 가능한 위치정보를 q에 넣을때 증가된 cost가 넣어진다.
    return cost
            
