def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            i = i.lower()
        else:
            i = i.upper()
        answer+=i
    return answer