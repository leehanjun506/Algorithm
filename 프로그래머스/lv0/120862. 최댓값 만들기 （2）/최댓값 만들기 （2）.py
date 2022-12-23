from itertools import combinations
def solution(numbers):
    new = []
    for i in combinations(numbers,2):
        new.append(i[0]*i[1])
    
    return max(new)