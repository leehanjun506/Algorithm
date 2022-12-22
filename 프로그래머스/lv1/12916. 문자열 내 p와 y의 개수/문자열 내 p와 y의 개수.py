def solution(s):
    s = s.lower()
    p = 0
    y = 0
    for i in s:
        if i == 'p':
            p+=1
        if i == 'y':
            y+=1
    return True if p == y else False