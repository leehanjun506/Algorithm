def solution(x, n):
    answer = [x]*n
    for i in range(1,n):
        answer[i] = answer[i-1]+x
    return answer