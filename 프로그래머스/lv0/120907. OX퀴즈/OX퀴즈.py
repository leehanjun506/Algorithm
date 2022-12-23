def solution(quiz):
    l = len(quiz)
    answer = ["X"]*l
    for i,v in enumerate(quiz):
        r = v.split()
        if eval(r[0]+r[1]+r[2]) == int(r[4]):
            answer[i] = 'O'
    return answer