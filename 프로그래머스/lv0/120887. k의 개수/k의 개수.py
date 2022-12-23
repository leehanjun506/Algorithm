def solution(i, j, k):
    answer = 0
    s = list(map(str,[i for i in range(i,j+1)]))
    new = "".join(s)
    for i in new:
        if i == str(k):
            answer+=1
    return answer