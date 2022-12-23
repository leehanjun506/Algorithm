import math
def solution(denum1, num1, denum2, num2):
    answer = []
    g = math.gcd(num1,num2)
    l = g*(num1//g)*(num2//g)
    x=denum1*l//num1+denum2*l//num2
    gx = math.gcd(x,l)
    answer = [x//gx,l//gx]
    return answer