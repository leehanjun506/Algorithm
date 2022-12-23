import math
def solution(a, b):
    x = b//math.gcd(a,b) # x를 소인수 분해 했을때 2와 5만 존재
    l = []
    def sol(x):
        d=2
        while x!=1:
            if x%d == 0:
                l.append(d)
                x //= d
            else:
                d+=1
    sol(x) 
    l = list(set(l))
    if 2 in l:
        l.remove(2)
    if 5 in l:
        l.remove(5)
    return 1 if not l else 2 

