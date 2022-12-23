def solution(chicken):
    answer = 0
    coupon = 0
    while chicken != 0:

        answer += chicken//10
        coupon += chicken%10 
        if coupon >= 10:
            answer+=1
            coupon -=10
            chicken = (chicken+1)//10
        else:
            chicken = chicken//10 
    return answer
