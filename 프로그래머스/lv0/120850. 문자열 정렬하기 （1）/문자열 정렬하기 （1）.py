def solution(my_string):
    answer = [i for i in my_string if i.isdigit()]
    answer = list(map(int,answer))
    answer.sort()
    return answer