from collections import deque
def solution(A, B):
    l = len(A)
    answer = 0
    q = deque(A)
    if A == B:
        return 0
    for _ in range(l-1):
        q.rotate(1)
        answer+=1
        if "".join(list(q)) == B:
            return answer
    return -1