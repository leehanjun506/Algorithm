def solution(n):
    wa = "수박"
    ex = "수"
    return wa*(n//2) if n%2 == 0 else wa*(n//2)+ex
