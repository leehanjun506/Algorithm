def solution(num, total):
    answer = [i+total+num for i in range(num) ]
    while(True):
        if sum(answer) == total:
            return answer
        for i in range(num):
            answer[i] -= 1
