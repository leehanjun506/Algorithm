def solution(keyinput, board):
    result = [0,0]
    def move(key):
        if key == 'left':
            result[0] -= 1
            if result[0] == -max_x-1:
                result[0] += 1
        elif key == 'right':
            result[0] += 1
            if result[0] == max_x+1:
                result[0] -= 1
        elif key == 'up':
            result[1] += 1
            if result[1] == max_y+1:
                result[1] -= 1
        else:
            result[1] -= 1
            if result[1] == -max_y-1:
                result[1] += 1
                
    max_x = board[0]//2
    max_y = board[1]//2
    
    for i in keyinput:
        move(i)
    
    return result