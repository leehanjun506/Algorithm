from bisect import bisect_left,bisect_right
def solution(array, height):
    array.sort()
    right = bisect_right(array,height)
    return len(array)-right