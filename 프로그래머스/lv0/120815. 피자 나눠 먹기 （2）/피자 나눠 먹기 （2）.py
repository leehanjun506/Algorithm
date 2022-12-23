import math
def solution(n):
    x = 6//math.gcd(n,6)
    result = x*n//6
    return result