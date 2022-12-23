def solution(before, after):
    return 1 if sorted([i for i in before]) == sorted([i for i in after]) else 0