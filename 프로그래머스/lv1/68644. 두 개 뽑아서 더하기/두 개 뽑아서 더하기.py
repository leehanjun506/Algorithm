from itertools import combinations
def solution(numbers):
    answer = list(combinations(numbers,2))
    result = []
    for i in answer:
        if sum(i) not in result:
            result.append(sum(i))
    result.sort()
    return result