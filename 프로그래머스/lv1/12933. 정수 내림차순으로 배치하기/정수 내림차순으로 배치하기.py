def solution(n):
    s = [i for i in str(n)]
    s.sort(reverse=True)
    return int("".join(s))
