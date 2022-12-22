def solution(hp):
    x = hp//5
    y = hp%5//3
    z = hp%5%3//1
    return x+y+z