def solution(price):
    answer = 0
    if price>= 500000:
        dis = 20
    elif price>= 300000:
        dis = 10
    elif price >= 100000:
        dis = 5
    else:
        dis = 0
    answer = price*(100-dis)//100
    return answer