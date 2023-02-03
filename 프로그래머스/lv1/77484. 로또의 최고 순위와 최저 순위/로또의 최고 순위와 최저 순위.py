def solution(lottos, win_nums):
    answer = []
    num = 0
    zero = lottos.count(0)
    print(zero)
    for lotto in lottos:
        if lotto in win_nums:
            num+=1
    if num+zero<2:
        answer.append(6)
    else:
        answer.append(7-num-zero)
    if num<2:
        answer.append(6)
    else:
        answer.append(7-num)
            
    return answer