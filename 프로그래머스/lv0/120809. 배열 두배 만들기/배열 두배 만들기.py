def solution(numbers):
    answer = [0]*len(numbers)
    for i,j in enumerate(numbers):
        answer[i] = 2*j
    return answer