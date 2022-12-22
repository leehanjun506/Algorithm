def solution(slice, n):
    answer = 0
    if n%slice == 0:
        return n/slice
    else:
        return n//slice+1
    return answer