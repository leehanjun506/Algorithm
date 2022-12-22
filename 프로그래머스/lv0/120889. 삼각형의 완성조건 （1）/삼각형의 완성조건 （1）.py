def solution(sides):
    sides.sort()
    l = sides[-1]
    return 1 if l< sum(sides)-l else 2