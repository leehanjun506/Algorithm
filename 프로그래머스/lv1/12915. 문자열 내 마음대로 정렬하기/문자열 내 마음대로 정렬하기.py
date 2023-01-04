def solution(strings, n):
    answer = []
    for v in strings:
        answer.append([v[n],v])
    answer.sort()
    
    return [answer[i][1] for i in range(len(strings))]