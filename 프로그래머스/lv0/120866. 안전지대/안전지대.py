def solution(board):
    visit = [[False]*len(board) for _ in range(len(board))]
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    danger = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1 :
                danger+=1
                if visit[i][j] == True:
                    danger-=1
                else:
                    visit[i][j] = True
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx >= 0 and nx < len(board) and ny >=0 and ny < len(board) and visit[nx][ny] == False:
                        visit[nx][ny] = True
                        danger+=1
                
    return len(board)*len(board)-danger