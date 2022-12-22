def solution(rsp):
    answer = {"2":"0","0":"5","5":"2"}
    result = ''
    for i in rsp:
        result+=answer[i]
    
    return result