def solution(cipher, code):
    answer = ''
    index = 1
    for i in cipher:
        if index%code == 0:
            answer+=i
        index+=1
    return answer