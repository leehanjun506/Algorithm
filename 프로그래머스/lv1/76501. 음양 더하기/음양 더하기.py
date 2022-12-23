def solution(absolutes, signs):
    answer = 0
    for i,v in enumerate(signs):
        if v == True:
            answer+=absolutes[i]
        else:
            answer-=absolutes[i]
    return answer