def solution(sides):
    answer = 0
    v1 = max(sides) 
    v2 = min(sides)
    v3 = v1
    while v1<(v2+v3):
        answer+=1
        v3-=1
    v3 = v1+1
    while v3<(v1+v2):
        answer+=1
        v3+=1
    return answer
