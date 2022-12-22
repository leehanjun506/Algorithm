import math
def solution(n):
    if (math.sqrt(n) - int(math.sqrt(n))) != 0:
        return -1
    else:
        return (math.sqrt(n)+1)**2
