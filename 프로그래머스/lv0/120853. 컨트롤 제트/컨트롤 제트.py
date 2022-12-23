def solution(s):
    stack = []
    s = s.split()
    for i in s:
        if i == 'Z':
            stack.pop()
        else:
            stack.append(i)
    answer = sum(list(map(int,stack)))
    return answer