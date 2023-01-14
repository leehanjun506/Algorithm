def solution(a, b, n):
    answer = 0
    while n>=a:
        pos = n//a #6 
        v = a*pos # 가져다 줄수 있는 개수
        n = n-a*pos+pos*b # 8
        answer+= pos*b # 6
        #a개를 가져오면 b개를 줌
    return answer