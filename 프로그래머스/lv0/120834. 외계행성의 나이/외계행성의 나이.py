def solution(age):
    answer = ''
    # a는 0
    
    age = str(age)
    for i in age:
        answer+=chr(int(i)+97)
    return answer