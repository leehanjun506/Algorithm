def solution(order):
    o = str(order)
    result = 0
    for v in o:
        if int(v)%3 == 0 and int(v)!=0:
            result += 1
    return result