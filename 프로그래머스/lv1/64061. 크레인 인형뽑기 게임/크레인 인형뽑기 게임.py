def solution(board, moves):
    box = []
    ans = 0
    for i in range(len(moves)):
        column = moves[i]-1
        for j in range(len(board)):
            if board[j][column] == 0:
                continue
            else:
                if not box:
                    box.append(board[j][column])
                else:
                    if box[-1] == board[j][column]:
                        box.pop()
                        ans+=2
                    else:
                        box.append(board[j][column])
                board[j][column] = 0
                break
                
    return ans