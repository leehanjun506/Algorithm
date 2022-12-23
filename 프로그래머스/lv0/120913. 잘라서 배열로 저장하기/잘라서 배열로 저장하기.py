def solution(my_str, n):
    q = len(my_str)//n
    r = len(my_str)%n
    answer = []
    for i in range(q):
        answer.append(my_str[n*i:n*(i+1)])
    if r != 0:
        answer.append(my_str[n*q:])
    return answer