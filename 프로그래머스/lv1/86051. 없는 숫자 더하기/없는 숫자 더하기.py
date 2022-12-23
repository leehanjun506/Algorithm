def solution(numbers):
    answer = [i for i in range(10)]
    for i in numbers:
        if i in answer:
            answer.remove(i)
    return sum(answer)