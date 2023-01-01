def solution(dots):
    def grad(n1,n2):
        x = dots[n1-1][0]-dots[n2-1][0]
        y = dots[n1-1][1]-dots[n2-1][1]
        return y/x
        
    if grad(1,2) == grad(3,4):
        return 1
    if grad(1,3) == grad(2,4):
        return 1
    if grad(1,4) == grad(2,3):
        return 1
    return 0